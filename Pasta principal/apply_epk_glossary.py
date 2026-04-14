from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

from fix_epk_script_blocks import (
    BRACKET_RE,
    read_lines,
    rebuild_file_bytes_preserving_structure,
)


GENERIC_SINGLE_WORD_TYPES = {"Atributos", "Habilidade", "Geral"}
MANUAL_DENY_TERMS = {
    "Man",
    "Magic",
    "Heaven",
    "Gift",
    "Riding",
    "Mist",
    "Avenger",
    "Holy Grail",
    "Red Branch",
}

SPECIAL_REPLACEMENTS: list[tuple[str, re.Pattern[str], str | callable]] = [
    (
        "Noble Phantasms",
        re.compile(r"(?<![\w])Noble Phantasms(?![\w])"),
        "Fantasmas Nobres",
    ),
    (
        "Sua Noble Phantasm",
        re.compile(r"(?<![\w])Sua Noble Phantasm(?![\w])"),
        "Seu Fantasma Nobre",
    ),
    (
        "sua Noble Phantasm",
        re.compile(r"(?<![\w])sua Noble Phantasm(?![\w])"),
        "seu Fantasma Nobre",
    ),
    (
        "Uma Noble Phantasm",
        re.compile(r"(?<![\w])Uma Noble Phantasm(?![\w])"),
        "Um Fantasma Nobre",
    ),
    (
        "uma Noble Phantasm",
        re.compile(r"(?<![\w])uma Noble Phantasm(?![\w])"),
        "um Fantasma Nobre",
    ),
]


@dataclass(frozen=True)
class GlossaryEntry:
    english: str
    portuguese: str
    term_type: str
    source_row: int


@dataclass
class LineChange:
    line_number: int
    before: str
    after: str
    replacements: list[str]


@dataclass
class FileResult:
    path: Path
    changes: list[LineChange]
    written: bool


def iter_target_files(pt_dir: Path, file_name: str | None) -> list[Path]:
    if file_name:
        return [pt_dir / file_name]
    return sorted(pt_dir.glob("*.epk_dec"))


def split_segments(body: str) -> list[list[object]]:
    segments: list[list[object]] = []
    cursor = 0
    for match in BRACKET_RE.finditer(body):
        if match.start() > cursor:
            segments.append([False, body[cursor : match.start()]])
        segments.append([True, match.group(0)])
        cursor = match.end()
    if cursor < len(body):
        segments.append([False, body[cursor:]])
    if not segments:
        segments.append([False, body])
    return segments


def join_segments(segments: list[list[object]]) -> str:
    return "".join(str(text) for _, text in segments)


def load_glossary_rows(csv_path: Path) -> list[GlossaryEntry]:
    entries: list[GlossaryEntry] = []
    with csv_path.open("r", encoding="utf-8-sig", newline="") as fh:
        reader = csv.reader(fh)
        next(reader, None)
        for row_number, row in enumerate(reader, start=2):
            if len(row) < 3:
                continue
            english = row[1].strip()
            portuguese = row[2].strip()
            term_type = row[4].strip() if len(row) > 4 else ""
            if not english or not portuguese or english == portuguese:
                continue
            entries.append(
                GlossaryEntry(
                    english=english,
                    portuguese=portuguese,
                    term_type=term_type,
                    source_row=row_number,
                )
            )
    return entries


def looks_like_glossary_csv(csv_path: Path) -> bool:
    try:
        with csv_path.open("r", encoding="utf-8-sig", newline="") as fh:
            reader = csv.reader(fh)
            header = next(reader, [])
    except Exception:
        return False

    if len(header) < 3:
        return False

    normalized = [cell.strip().lower() for cell in header[:3]]
    return normalized == ["japonês", "inglês", "português"]


def find_default_glossary_path() -> Path | None:
    candidates = sorted(Path(".").glob("*.csv"))
    for candidate in candidates:
        if looks_like_glossary_csv(candidate):
            return candidate
    return None


def choose_safe_glossary_entries(entries: list[GlossaryEntry]) -> tuple[list[GlossaryEntry], dict[str, list[GlossaryEntry]]]:
    grouped: dict[str, list[GlossaryEntry]] = defaultdict(list)
    for entry in entries:
        grouped[entry.english].append(entry)

    safe: list[GlossaryEntry] = []
    ambiguous: dict[str, list[GlossaryEntry]] = {}

    for english, variants in grouped.items():
        portuguese_set = {item.portuguese for item in variants}
        if len(portuguese_set) > 1:
            ambiguous[english] = variants
            continue

        chosen = variants[0]
        if not is_entry_safe(chosen):
            continue
        safe.append(chosen)

    safe.sort(key=lambda item: (-len(item.english), item.english.lower()))
    return safe, ambiguous


def is_entry_safe(entry: GlossaryEntry) -> bool:
    if entry.english in MANUAL_DENY_TERMS:
        return False

    word_count = len(entry.english.split())
    if word_count >= 2:
        return True

    if len(entry.english) < 5:
        return False

    if entry.term_type in GENERIC_SINGLE_WORD_TYPES:
        return False

    return entry.english[:1].isupper()


def build_pattern(entry: GlossaryEntry) -> re.Pattern[str]:
    escaped = re.escape(entry.english)
    if entry.english == "Holy Grail":
        return re.compile(r"(?<![\w])" + escaped + r"(?![\w]|\s+War\b)")
    return re.compile(r"(?<![\w])" + escaped + r"(?![\w])")


def replace_in_segments(
    segments: list[list[object]],
    compiled_entries: list[tuple[GlossaryEntry, re.Pattern[str]]],
) -> list[str]:
    replacements: list[str] = []
    for segment in segments:
        is_bracket, text = segment
        if is_bracket:
            continue

        current = str(text)
        for label, pattern, replacement in SPECIAL_REPLACEMENTS:
            if not pattern.search(current):
                continue
            current, count = pattern.subn(replacement, current)
            if count:
                replacements.extend([label] * count)

        for entry, pattern in compiled_entries:
            if not pattern.search(current):
                continue
            current, count = pattern.subn(entry.portuguese, current)
            if count:
                replacements.extend([entry.english] * count)
        segment[1] = current
    return replacements


def process_file(
    original_path: Path,
    translated_path: Path,
    compiled_entries: list[tuple[GlossaryEntry, re.Pattern[str]]],
    apply_changes: bool,
) -> FileResult:
    translated_lines = read_lines(translated_path)
    working_lines = translated_lines.copy()
    changes: list[LineChange] = []

    for idx, line in enumerate(translated_lines, start=1):
        if "::" not in line:
            continue

        line_core = line.rstrip("\r\n")
        line_ending = line[len(line_core) :]
        parts = line_core.split("::", 3)
        if len(parts) < 3:
            continue

        body = parts[2]
        segments = split_segments(body)
        replacements = replace_in_segments(segments, compiled_entries)
        if not replacements:
            continue

        new_body = join_segments(segments)
        new_line_core = parts[0] + "::" + parts[1] + "::" + new_body
        if len(parts) == 4:
            new_line_core += "::" + parts[3]

        new_line = new_line_core + line_ending
        if new_line == line:
            continue

        changes.append(
            LineChange(
                line_number=idx,
                before=line_core,
                after=new_line_core,
                replacements=replacements,
            )
        )
        working_lines[idx - 1] = new_line

    written = False
    if apply_changes and changes:
        translated_path.write_bytes(
            rebuild_file_bytes_preserving_structure(original_path, working_lines)
        )
        written = True

    return FileResult(
        path=translated_path,
        changes=changes,
        written=written,
    )


def write_report(
    report_path: Path,
    results: list[FileResult],
    glossary_path: Path,
    applied_entries: list[GlossaryEntry],
    ambiguous_entries: dict[str, list[GlossaryEntry]],
) -> None:
    with report_path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(
            ["arquivo", "linha", "replacements", "before", "after"]
        )
        for result in results:
            for change in result.changes:
                writer.writerow(
                    [
                        result.path.name,
                        change.line_number,
                        ";".join(change.replacements),
                        change.before,
                        change.after,
                    ]
                )

    meta_path = report_path.with_name(report_path.stem + "_meta.csv")
    with meta_path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(["tipo", "english", "portuguese", "term_type", "source_row"])
        for entry in applied_entries:
            writer.writerow(
                ["aplicavel", entry.english, entry.portuguese, entry.term_type, entry.source_row]
            )
        for english, variants in sorted(ambiguous_entries.items()):
            for entry in variants:
                writer.writerow(
                    ["ambiguo", english, entry.portuguese, entry.term_type, entry.source_row]
                )
        writer.writerow(["glossary_path", str(glossary_path), "", "", ""])


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Aplica um glossário CSV aos .epk_dec, alterando apenas o texto visível "
            "e preservando a estrutura bruta do arquivo."
        )
    )
    parser.add_argument("--orig-dir", type=Path, default=Path("."))
    parser.add_argument("--pt-dir", type=Path, default=Path("scripts_pt-br"))
    parser.add_argument("--glossary", type=Path)
    parser.add_argument("--file")
    parser.add_argument("--apply", action="store_true")
    parser.add_argument(
        "--report",
        type=Path,
        default=Path("epk_glossary_apply_report.csv"),
    )
    args = parser.parse_args()

    glossary_path = args.glossary
    if glossary_path is None:
        glossary_path = find_default_glossary_path()
        if glossary_path is None:
            print("Nenhum CSV de glossário encontrado.")
            return 1

    glossary_entries = load_glossary_rows(glossary_path)
    safe_entries, ambiguous_entries = choose_safe_glossary_entries(glossary_entries)
    compiled_entries = [(entry, build_pattern(entry)) for entry in safe_entries]

    mode = "APPLY" if args.apply else "DRY-RUN"
    print(mode)
    print(f"Glossario: {glossary_path}")
    print(f"Entradas lidas: {len(glossary_entries)}")
    print(f"Entradas seguras: {len(safe_entries)}")
    print(f"Entradas ambiguas puladas: {len(ambiguous_entries)}")

    targets = iter_target_files(args.pt_dir, args.file)
    results: list[FileResult] = []
    changed_files = 0
    changed_lines = 0
    term_counts: dict[str, int] = defaultdict(int)

    for translated_path in targets:
        if not translated_path.exists():
            print(f"[IGNORADO] Arquivo nao encontrado: {translated_path}")
            continue

        original_path = args.orig_dir / translated_path.name
        if not original_path.exists():
            print(f"[IGNORADO] Original nao encontrado para: {translated_path.name}")
            continue

        result = process_file(
            original_path=original_path,
            translated_path=translated_path,
            compiled_entries=compiled_entries,
            apply_changes=args.apply,
        )
        results.append(result)

        if not result.changes:
            continue

        changed_files += 1
        changed_lines += len(result.changes)
        for change in result.changes:
            for replacement in change.replacements:
                term_counts[replacement] += 1

        line_list = ", ".join(str(item.line_number) for item in result.changes[:30])
        if len(result.changes) > 30:
            line_list += ", ..."
        verb = "seriam alteradas" if not args.apply else "alteradas"
        print(f"\nArquivo: {translated_path.name}")
        print(f"  Linhas {verb}: {line_list}")
        if result.written:
            print("  Status: gravado")

    write_report(args.report, results, glossary_path, safe_entries, ambiguous_entries)

    print("\nResumo")
    print(f"Arquivos analisados: {len(results)}")
    print(f"Arquivos com alteracoes: {changed_files}")
    print(f"Linhas alteradas: {changed_lines}")
    print("Top termos aplicados:")
    for english, count in sorted(term_counts.items(), key=lambda item: (-item[1], item[0]))[:20]:
        print(f"  {english}: {count}")
    print(f"Relatorio: {args.report}")
    print(f"Meta: {args.report.with_name(args.report.stem + '_meta.csv')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
