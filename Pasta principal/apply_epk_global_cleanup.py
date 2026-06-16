from __future__ import annotations

import argparse
import csv
import re
import sys
from dataclasses import dataclass
from pathlib import Path


BRACKET_RE = re.compile(r"\[[^\]]*\]")
MESSAGE_LABEL_RE = re.compile(r"^\$\$\$[^$]+\$\$\$$")
CONTROL_CHAR_RE = re.compile(r"[\x00-\x08\x0B\x0C\x0E-\x1F]")
WORD_RE = re.compile(r"[A-Za-z']+")
VISIBLE_END_MARKERS = [
    "[nolr]::",
    "[lr]::",
    "[r]::",
    "[p]::",
    "[nr]::",
    '"::',
    "'::",
    "[nolr]:",
    "[lr]:",
    "[r]:",
    "[p]:",
    "[nr]:",
    "[nolr]",
    "[lr]",
    "[r]",
    "[p]",
    "[nr]",
    "::",
    '"',
    "'",
]
ENGLISH_STOPWORDS = {
    "the",
    "and",
    "that",
    "this",
    "you",
    "your",
    "with",
    "have",
    "will",
    "can",
    "could",
    "would",
    "should",
    "there",
    "here",
    "what",
    "when",
    "where",
    "why",
    "how",
    "from",
    "about",
    "into",
    "like",
    "just",
    "only",
    "even",
    "then",
    "now",
    "not",
    "but",
    "for",
    "are",
    "was",
    "were",
    "has",
    "had",
    "his",
    "her",
    "him",
    "she",
    "they",
    "them",
    "their",
    "all",
    "one",
    "two",
    "more",
    "less",
    "going",
    "think",
    "know",
    "because",
    "i",
    "it",
    "we",
    "he",
}
REPLACEMENTS: list[tuple[str, re.Pattern[str], str]] = [
    ("Holy Grail War", re.compile(r"(?<![\w])Holy Grail War(?![\w])"), "Guerra do Santo Graal"),
    ("Noble Phantasms", re.compile(r"(?<![\w])Noble Phantasms(?![\w])"), "Fantasmas Nobres"),
    ("Noble Phantasm", re.compile(r"(?<![\w])Noble Phantasm(?![\w])"), "Fantasma Nobre"),
    ("Pergaminho Nobre", re.compile(r"(?<![\w])Pergaminho Nobre(?![\w])"), "Fantasma Nobre"),
    ("Pergaminhos Nobres", re.compile(r"(?<![\w])Pergaminhos Nobres(?![\w])"), "Fantasmas Nobres"),
    ("Blood Fort Andromeda", re.compile(r"(?<![\w])Blood Fort Andromeda(?![\w])"), "Forte de Sangue Andrômeda"),
    ("Mystic Eye Killers", re.compile(r"(?<![\w])Mystic Eye Killers(?![\w])"), "Supressores de Olhos Místicos"),
    ("Bounded Field", re.compile(r"(?<![\w])Bounded Field(?![\w])"), "Campo Limitado"),
    ("Campo Limitante", re.compile(r"(?<![\w])Campo Limitante(?![\w])"), "Campo Limitado"),
    ("Command Spells", re.compile(r"(?<![\w])Command Spells(?![\w])"), "Selos de Comando"),
    ("Command Spell", re.compile(r"(?<![\w])Command Spell(?![\w])"), "Selo de Comando"),
    ("Command Seals", re.compile(r"(?<![\w])Command Seals(?![\w])"), "Selos de Comando"),
    ("Command Seal", re.compile(r"(?<![\w])Command Seal(?![\w])"), "Selo de Comando"),
    ("True Names", re.compile(r"(?<![\w])True Names(?![\w])"), "Nomes Verdadeiros"),
    ("True Name", re.compile(r"(?<![\w])True Name(?![\w])"), "Nome Verdadeiro"),
    ("Heroic Spirits", re.compile(r"(?<![\w])Heroic Spirits(?![\w])"), "Espíritos Heroicos"),
    ("Heroic Spirit", re.compile(r"(?<![\w])Heroic Spirit(?![\w])"), "Espírito Heroico"),
    ("Holy Grail", re.compile(r"(?<![\w])Holy Grail(?![\w])"), "Santo Graal"),
    ("Masters", re.compile(r"(?<![\w])Masters(?![\w])"), "Mestres"),
    ("Master", re.compile(r"(?<![\w])Master(?![\w])"), "Mestre"),
    ("Servants", re.compile(r"(?<![\w])Servants(?![\w])"), "Servos"),
    ("Servant", re.compile(r"(?<![\w])Servant(?![\w])"), "Servo"),
    ("Einzberns", re.compile(r"(?<![\w])Einzberns(?![\w])"), "Einzbern"),
    ("summonado", re.compile(r"(?<![\w])summonado(?![\w])"), "invocado"),
    ("Gorgon Breaker", re.compile(r"(?<![\w])Gorgon Breaker(?![\w])"), "Breaker Gorgon"),
]


@dataclass
class LineChange:
    line_number: int
    kinds: list[str]
    before: str
    after: str


def read_lines(path: Path) -> list[str]:
    with path.open("r", encoding="utf-8", errors="replace", newline="") as fh:
        return fh.read().splitlines(keepends=True)


def split_line_ending(line: str) -> tuple[str, str]:
    if line.endswith("\r\n"):
        return line[:-2], "\r\n"
    if line.endswith("\n"):
        return line[:-1], "\n"
    return line, ""


def split_segments(text: str) -> list[list[object]]:
    segments: list[list[object]] = []
    cursor = 0
    for match in BRACKET_RE.finditer(text):
        if match.start() > cursor:
            segments.append([False, text[cursor : match.start()]])
        segments.append([True, match.group(0)])
        cursor = match.end()
    if cursor < len(text):
        segments.append([False, text[cursor:]])
    if not segments:
        segments.append([False, text])
    return segments


def join_segments(segments: list[list[object]]) -> str:
    return "".join(str(text) for _, text in segments)


def english_stopword_hits(text: str) -> int:
    return sum(1 for word in WORD_RE.findall(text) if word.lower() in ENGLISH_STOPWORDS)


def looks_like_suspicious_tail(text: str) -> bool:
    stripped = text.strip()
    if not stripped:
        return False
    if "\ufffd" in stripped:
        return True
    if CONTROL_CHAR_RE.search(stripped):
        return True
    if english_stopword_hits(stripped) >= 3:
        return True
    return False


def trim_suspicious_tail(core: str) -> tuple[str, bool]:
    best_end = -1
    for marker in VISIBLE_END_MARKERS:
        idx = core.rfind(marker)
        if idx < 0:
            continue
        end = idx + len(marker)
        if end > best_end:
            best_end = end

    if best_end <= 0 or best_end >= len(core):
        return core, False

    tail = core[best_end:]
    if not looks_like_suspicious_tail(tail):
        return core, False

    return core[:best_end], True


def apply_replacements_to_text(text: str) -> tuple[str, list[str]]:
    segments = split_segments(text)
    applied: list[str] = []

    for segment in segments:
        is_bracket, seg_text = segment
        if is_bracket:
            continue

        current = str(seg_text)
        for label, pattern, replacement in REPLACEMENTS:
            current, count = pattern.subn(replacement, current)
            if count:
                applied.extend([label] * count)
        segment[1] = current

    return join_segments(segments), applied


def cleanup_message_line(parts: list[str]) -> tuple[list[str], list[str]]:
    changes: list[str] = []
    if len(parts) < 3 or not MESSAGE_LABEL_RE.match(parts[1]):
        return parts, changes

    new_text, replacements = apply_replacements_to_text(parts[2])
    if replacements:
        parts[2] = new_text
        changes.extend(sorted(set(replacements)))

    if len(parts) >= 4 and parts[3] and looks_like_suspicious_tail(parts[3]):
        parts[3] = ""
        del parts[4:]
        changes.append("tail")
        return parts, changes

    if len(parts) > 4:
        extra_tail = "::".join(parts[3:])
        if looks_like_suspicious_tail(extra_tail):
            parts = [parts[0], parts[1], parts[2], ""]
            changes.append("tail")

    return parts, changes


def cleanup_generic_fields(parts: list[str]) -> tuple[list[str], list[str]]:
    changes: list[str] = []
    if len(parts) < 3:
        return parts, changes

    for index in range(2, len(parts)):
        if not parts[index]:
            continue
        new_text, replacements = apply_replacements_to_text(parts[index])
        if replacements and new_text != parts[index]:
            parts[index] = new_text
            changes.extend(sorted(set(replacements)))

    return parts, changes


def process_line(line: str) -> tuple[str, list[str]]:
    core, ending = split_line_ending(line)
    if "::" not in core:
        return line, []

    kinds: list[str] = []
    trimmed_core, trimmed = trim_suspicious_tail(core)
    if trimmed:
        core = trimmed_core
        kinds.append("tail")

    parts = core.split("::")
    if len(parts) >= 3 and MESSAGE_LABEL_RE.match(parts[1]):
        parts, part_kinds = cleanup_message_line(parts)
    else:
        parts, part_kinds = cleanup_generic_fields(parts)

    if part_kinds:
        kinds.extend(part_kinds)

    new_core = "::".join(parts)
    if not trimmed and not part_kinds:
        return line, []

    if new_core == split_line_ending(line)[0]:
        return line, []
    return new_core + ending, sorted(set(kinds))


def iter_target_files(pt_dir: Path, file_name: str | None) -> list[Path]:
    if file_name:
        return [pt_dir / file_name]
    return sorted(pt_dir.glob("*.epk_dec"))


def write_report(report_path: Path, results: list[tuple[Path, list[LineChange]]]) -> None:
    report_path.parent.mkdir(parents=True, exist_ok=True)
    with report_path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(["arquivo", "linha", "tipos", "before", "after"])
        for path, changes in results:
            for change in changes:
                writer.writerow(
                    [
                        path.name,
                        change.line_number,
                        ";".join(change.kinds),
                        change.before,
                        change.after,
                    ]
                )


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Aplica uma limpeza global aos scripts PT-BR: remove sufixos "
            "corrompidos/colas evidentes e normaliza um conjunto fechado de "
            "termos fora do glossário, sem retraduzir linhas."
        )
    )
    parser.add_argument("--pt-dir", type=Path, default=Path("scripts_pt-br"))
    parser.add_argument("--file")
    parser.add_argument("--apply", action="store_true")
    parser.add_argument(
        "--report",
        type=Path,
        default=Path("_codex_epk_stage/global_cleanup_report.csv"),
    )
    args = parser.parse_args()

    targets = iter_target_files(args.pt_dir, args.file)
    if not targets:
        print("Nenhum arquivo alvo encontrado.")
        return 1

    mode = "APPLY" if args.apply else "DRY-RUN"
    print(mode)

    results: list[tuple[Path, list[LineChange]]] = []
    changed_files = 0
    changed_lines = 0

    for path in targets:
        if not path.exists():
            print(f"[IGNORADO] Arquivo nao encontrado: {path}")
            continue

        lines = read_lines(path)
        working = lines.copy()
        changes: list[LineChange] = []

        for idx, line in enumerate(lines, start=1):
            new_line, kinds = process_line(line)
            if not kinds or new_line == line:
                continue

            changes.append(
                LineChange(
                    line_number=idx,
                    kinds=kinds,
                    before=line.rstrip("\r\n"),
                    after=new_line.rstrip("\r\n"),
                )
            )
            working[idx - 1] = new_line

        if changes:
            changed_files += 1
            changed_lines += len(changes)
            results.append((path, changes))
            print(f"{path.name}: {len(changes)} linha(s)")
            if args.apply:
                path.write_bytes("".join(working).encode("utf-8"))

    write_report(args.report, results)

    print("\nResumo")
    print(f"Arquivos analisados: {len(targets)}")
    print(f"Arquivos com alteracoes: {changed_files}")
    print(f"Linhas alteradas: {changed_lines}")
    print(f"Relatorio: {args.report}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
