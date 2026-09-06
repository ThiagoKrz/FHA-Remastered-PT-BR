from __future__ import annotations

import argparse
import csv
import re
import sys
from dataclasses import dataclass
from pathlib import Path


BRACKET_RE = re.compile(r"\[[^\]]*\]")
TOKEN_NAME_RE = re.compile(r"^\[([^\s=\]]+)")
RECORD_ID_RE = re.compile(r"^(?P<prefix>\d+)::(?P<record_id>\$\$\$[^:]+?\$\$\$)::")
REPLACEABLE_LINE_RE = re.compile(r"^\d+::")
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
]


@dataclass
class LineFix:
    line_number: int
    record_id: str
    before: str
    after: str


@dataclass
class ManualIssue:
    line_number: int
    record_id: str
    reason: str


@dataclass
class FileResult:
    source_path: Path
    output_path: Path
    fixes: list[LineFix]
    manual_issues: list[ManualIssue]
    written: bool
    strict_blocked: bool


def get_record_id(line: str) -> str | None:
    match = RECORD_ID_RE.match(line)
    if not match:
        return None
    return match.group("record_id")


def get_token_head(token: str) -> str:
    match = TOKEN_NAME_RE.match(token)
    if not match:
        return token[:2]
    return "[" + match.group(1)


def extract_tokens(line: str) -> list[str]:
    return [match.group(0) for match in BRACKET_RE.finditer(line)]


def split_line_parts(line: str, allow_unterminated: bool = False) -> tuple[str, str, str] | None:
    newline = ""
    if line.endswith("\r\n"):
        newline = "\r\n"
        line_core = line[:-2]
    elif line.endswith("\n"):
        newline = "\n"
        line_core = line[:-1]
    else:
        line_core = line

    record_match = RECORD_ID_RE.match(line_core)
    if not record_match:
        return None

    if line_core.endswith("::"):
        prefix = line_core[: record_match.end()]
        body = line_core[record_match.end() : -2]
        suffix = "::" + newline
        return prefix, body, suffix

    if not allow_unterminated:
        return None

    if line_core.count("[") != line_core.count("]"):
        return None

    prefix = line_core[: record_match.end()]
    body = line_core[record_match.end() :]
    suffix = newline
    return prefix, body, suffix


def replace_tokens_by_span(original_line: str, translated_line: str) -> tuple[str, bool]:
    original_matches = list(BRACKET_RE.finditer(original_line))
    translated_matches = list(BRACKET_RE.finditer(translated_line))

    if len(original_matches) != len(translated_matches):
        return translated_line, False

    fixed_line = translated_line
    changed = False
    offset = 0

    for original_match, translated_match in zip(original_matches, translated_matches):
        original_token = original_match.group(0)
        translated_token = translated_match.group(0)
        if original_token == translated_token:
            continue

        start = translated_match.start() + offset
        end = translated_match.end() + offset
        fixed_line = fixed_line[:start] + original_token + fixed_line[end:]
        offset += len(original_token) - len(translated_token)
        changed = True

    return fixed_line, changed


def token_equals(original_token: str, translated_token: str, use_heads: bool) -> bool:
    if use_heads:
        return get_token_head(original_token) == get_token_head(translated_token)
    return original_token == translated_token


def build_subsequence_alignment(
    original_tokens: list[str],
    translated_tokens: list[str],
    use_heads: bool,
) -> list[tuple[int, int]] | None:
    matches: list[tuple[int, int]] = []
    origin_cursor = 0

    for translated_index, translated_token in enumerate(translated_tokens):
        found = False
        for original_index in range(origin_cursor, len(original_tokens)):
            if token_equals(original_tokens[original_index], translated_token, use_heads):
                matches.append((original_index, translated_index))
                origin_cursor = original_index + 1
                found = True
                break
        if not found:
            return None

    return matches


def trim_suspicious_suffix(text: str) -> str:
    cut = None
    for index, char in enumerate(text):
        code = ord(char)
        if 127 < code < 160:
            cut = index
            break

    if cut is None:
        return text

    while cut > 0 and text[cut - 1] in ":]":
        cut -= 1
    return text[:cut]


def trim_suspicious_prefix(text: str) -> str:
    start = None
    for index, char in enumerate(text):
        code = ord(char)
        if 127 < code < 160:
            start = index
            break

    if start is None or start != 0:
        return text

    end = start
    while end < len(text) and (127 < ord(text[end]) < 160 or text[end] in ":[ ]"):
        end += 1
    return text[end:]


def split_translated_slice_by_weights(translated_text: str, weights: list[int]) -> list[str]:
    if not weights:
        return [translated_text]

    total_weight = sum(weights)
    parts: list[str] = []

    if total_weight == 0:
        return [""] * len(weights)

    cursor = 0
    translated_len = len(translated_text)
    cumulative_weight = 0

    for index, weight in enumerate(weights):
        cumulative_weight += weight
        if index == len(weights) - 1:
            next_cursor = translated_len
        else:
            next_cursor = round((cumulative_weight / total_weight) * translated_len)
        parts.append(translated_text[cursor:next_cursor])
        cursor = next_cursor

    return parts


def rebuild_missing_subsegment(original_subsegment: str, translated_text: str) -> str:
    missing_matches = list(BRACKET_RE.finditer(original_subsegment))
    if not missing_matches:
        return translated_text

    text_parts: list[str] = []
    missing_tokens: list[str] = []
    cursor = 0
    for match in missing_matches:
        text_parts.append(original_subsegment[cursor : match.start()])
        missing_tokens.append(match.group(0))
        cursor = match.end()
    text_parts.append(original_subsegment[cursor:])

    if text_parts and text_parts[0] == "":
        translated_text = trim_suspicious_prefix(translated_text)
    if text_parts and text_parts[-1] == "":
        translated_text = trim_suspicious_suffix(translated_text)

    weights = [len(part) for part in text_parts]
    translated_parts = split_translated_slice_by_weights(translated_text, weights)

    rebuilt: list[str] = []
    for index, token in enumerate(missing_tokens):
        rebuilt.append(translated_parts[index])
        rebuilt.append(token)
    rebuilt.append(translated_parts[-1])
    return "".join(rebuilt)


def rebuild_line_by_subsequence(
    original_line: str,
    translated_line: str,
    use_heads: bool,
) -> tuple[str, bool, bool]:
    original_parts = split_line_parts(original_line)
    translated_parts = split_line_parts(translated_line)
    if translated_parts is None:
        translated_parts = split_line_parts(translated_line, allow_unterminated=True)
    if original_parts is None or translated_parts is None:
        return translated_line, False, True

    original_prefix, original_body, original_suffix = original_parts
    translated_prefix, translated_body, translated_suffix = translated_parts

    if original_prefix != translated_prefix:
        return translated_line, False, True

    original_token_matches = list(BRACKET_RE.finditer(original_body))
    translated_token_matches = list(BRACKET_RE.finditer(translated_body))
    original_tokens = [match.group(0) for match in original_token_matches]
    translated_tokens = [match.group(0) for match in translated_token_matches]

    alignment = build_subsequence_alignment(original_tokens, translated_tokens, use_heads)
    if alignment is None:
        return translated_line, False, True

    rebuilt_body_parts: list[str] = []
    previous_original_end = 0
    previous_translated_end = 0

    for original_index, translated_index in alignment:
        original_match = original_token_matches[original_index]
        translated_match = translated_token_matches[translated_index]

        original_subsegment = original_body[previous_original_end : original_match.start()]
        translated_text = translated_body[previous_translated_end : translated_match.start()]
        rebuilt_body_parts.append(rebuild_missing_subsegment(original_subsegment, translated_text))
        rebuilt_body_parts.append(original_match.group(0))

        previous_original_end = original_match.end()
        previous_translated_end = translated_match.end()

    trailing_original = original_body[previous_original_end:]
    trailing_translated = translated_body[previous_translated_end:]
    rebuilt_body_parts.append(rebuild_missing_subsegment(trailing_original, trailing_translated))

    rebuilt_line = original_prefix + "".join(rebuilt_body_parts) + original_suffix
    changed = rebuilt_line != translated_line
    return rebuilt_line, changed, False


def replace_tokens_by_heads(original_line: str, translated_line: str) -> tuple[str, bool, bool]:
    original_tokens = extract_tokens(original_line)
    if not original_tokens:
        return translated_line, False, False

    fixed_line = translated_line
    changed = False
    cursor = 0

    for index, original_token in enumerate(original_tokens):
        current_head = get_token_head(original_token)
        start = fixed_line.find(current_head, cursor)
        if start == -1:
            return translated_line, False, True

        if index + 1 < len(original_tokens):
            next_head = get_token_head(original_tokens[index + 1])
            end = fixed_line.find(next_head, start + len(current_head))
            if end == -1:
                close = fixed_line.find("]", start)
                if close == -1:
                    return translated_line, False, True
                end = close + 1
        else:
            tail = fixed_line.rfind("::")
            if tail > start:
                end = tail
            else:
                close = fixed_line.find("]", start)
                if close == -1:
                    return translated_line, False, True
                end = close + 1

        candidate = fixed_line[start:end]
        if candidate != original_token:
            fixed_line = fixed_line[:start] + original_token + fixed_line[end:]
            changed = True

        cursor = start + len(original_token)

    return fixed_line, changed, False


def fix_line(original_line: str, translated_line: str) -> tuple[str, bool, bool]:
    original_tokens = extract_tokens(original_line)
    translated_tokens = extract_tokens(translated_line)

    if not original_tokens:
        return translated_line, False, False

    if len(original_tokens) == len(translated_tokens):
        fixed_line, changed = replace_tokens_by_span(original_line, translated_line)
        return fixed_line, changed, False

    fixed_line, changed, failed = rebuild_line_by_subsequence(
        original_line,
        translated_line,
        use_heads=False,
    )
    if not failed:
        return fixed_line, changed, False

    fixed_line, changed, failed = rebuild_line_by_subsequence(
        original_line,
        translated_line,
        use_heads=True,
    )
    if not failed:
        return fixed_line, changed, False

    return replace_tokens_by_heads(original_line, translated_line)


def index_original_lines(lines: list[str]) -> tuple[dict[str, str], set[str]]:
    record_map: dict[str, str] = {}
    duplicates: set[str] = set()

    for line in lines:
        record_id = get_record_id(line)
        if not record_id:
            continue
        if record_id in record_map:
            duplicates.add(record_id)
            continue
        record_map[record_id] = line

    return record_map, duplicates


def split_text_lines(text: str, keepends: bool = False) -> list[str]:
    raw_parts = text.split("\n")
    lines: list[str] = []

    for index, part in enumerate(raw_parts):
        is_last = index == len(raw_parts) - 1
        if not is_last:
            if part.endswith("\r"):
                core = part[:-1]
                ending = "\r\n"
            else:
                core = part
                ending = "\n"
            lines.append(core + ending if keepends else core)
            continue

        if part or text.endswith("\n"):
            lines.append(part if keepends else part)

    return lines


def read_lines(path: Path) -> list[str]:
    return split_text_lines(
        path.read_text(encoding="utf-8", errors="replace"),
        keepends=True,
    )


def is_replaceable_line(line: str, line_number: int) -> bool:
    if line_number <= 2:
        return True
    return bool(REPLACEABLE_LINE_RE.match(line))


def split_raw_line_ending(raw_line: bytes) -> tuple[bytes, bytes]:
    if raw_line.endswith(b"\r\n"):
        return raw_line[:-2], b"\r\n"
    if raw_line.endswith(b"\n"):
        return raw_line[:-1], b"\n"
    return raw_line, b""


def tail_looks_suspicious(text: str) -> bool:
    if not text:
        return False
    for char in text:
        if char == "\ufffd":
            return True
        code = ord(char)
        if code < 32 and char not in ("\t",):
            return True
    return False


def tail_starts_with_noise(text: str) -> bool:
    if not text:
        return False
    for index, char in enumerate(text):
        if char == "\ufffd":
            return index <= 2
        code = ord(char)
        if code < 32 and char not in ("\t",):
            return index <= 2
    return False


def split_visible_text_and_suffix(
    raw_line: bytes,
    decoded_line: str,
) -> tuple[str, bytes, bytes, str | None]:
    raw_core, line_ending = split_raw_line_ending(raw_line)
    visible_text = decoded_line
    selected_marker: str | None = None
    best_end = -1

    # Alguns EPKs terminam a última fala com bytes binários logo após um único
    # dois-pontos, sem um marcador textual final válido. Nesses casos, a
    # decodificação com ``errors="replace"`` não permite reencontrar o prefixo
    # nos bytes originais. O primeiro byte UTF-8 inválido é a fronteira segura
    # entre o texto visível e o trailer estrutural que precisa ser preservado.
    try:
        raw_core.decode("utf-8")
    except UnicodeDecodeError as error:
        prefix_bytes = raw_core[: error.start]
        try:
            prefix_text = prefix_bytes.decode("utf-8")
        except UnicodeDecodeError:
            pass
        else:
            suffix = raw_core[error.start :]
            if prefix_text[:1].isdigit() and suffix:
                for marker in VISIBLE_END_MARKERS:
                    if prefix_text.endswith(marker):
                        selected_marker = marker
                        break
                return prefix_text, suffix, line_ending, selected_marker

    for marker in VISIBLE_END_MARKERS:
        index = decoded_line.rfind(marker)
        if index < 0:
            continue
        end_index = index + len(marker)
        if end_index > best_end:
            best_end = end_index
            selected_marker = marker

    if selected_marker is not None:
        candidate_visible = decoded_line[:best_end]
        candidate_tail = decoded_line[best_end:]
        if candidate_tail and tail_starts_with_noise(candidate_tail):
            visible_text = candidate_visible
        else:
            selected_marker = None

    encoded_visible = visible_text.encode("utf-8")
    if not raw_core.startswith(encoded_visible):
        trimmed_visible = visible_text
        while trimmed_visible and tail_looks_suspicious(trimmed_visible[-1]):
            trimmed_visible = trimmed_visible[:-1]
        trimmed_encoded = trimmed_visible.encode("utf-8")
        if raw_core.startswith(trimmed_encoded):
            visible_text = trimmed_visible
            encoded_visible = trimmed_encoded

    suffix = b""
    if raw_core.startswith(encoded_visible):
        suffix = raw_core[len(encoded_visible) :]

    if suffix and selected_marker is None:
        for marker in VISIBLE_END_MARKERS:
            if visible_text.endswith(marker):
                selected_marker = marker
                break

    return visible_text, suffix, line_ending, selected_marker


def trim_translated_visible_text(translated_line: str, marker: str | None) -> str:
    translated_line = translated_line.rstrip("\r\n")
    if not marker:
        return translated_line

    marker_index = translated_line.rfind(marker)
    if marker_index >= 0:
        return translated_line[: marker_index + len(marker)]
    return translated_line


def normalize_trailing_colons(
    translated_visible: str,
    original_visible: str,
    has_suffix: bool,
) -> str:
    if not has_suffix:
        return translated_visible

    original_colons = len(original_visible) - len(original_visible.rstrip(":"))
    translated_colons = len(translated_visible) - len(translated_visible.rstrip(":"))
    if original_colons == translated_colons:
        return translated_visible
    return translated_visible.rstrip(":") + (":" * original_colons)


def rebuild_file_bytes_preserving_structure(original_path: Path, lines: list[str]) -> bytes:
    original_raw = original_path.read_bytes()
    original_raw_lines = original_raw.splitlines(keepends=True)
    original_text_lines = [
        split_raw_line_ending(raw_line)[0].decode("utf-8", errors="replace")
        for raw_line in original_raw_lines
    ]
    translated_text_lines = [line.rstrip("\r\n") for line in lines]

    original_replaceable = [
        (index, line)
        for index, line in enumerate(original_text_lines, start=1)
        if is_replaceable_line(line, index)
    ]
    translated_replaceable = [
        line
        for index, line in enumerate(translated_text_lines, start=1)
        if is_replaceable_line(line, index)
    ]

    if len(original_replaceable) != len(translated_replaceable):
        raise ValueError(
            "Quantidade de linhas lógicas não bate entre original e traduzido: "
            f"{len(original_replaceable)} != {len(translated_replaceable)}"
        )

    translated_iter = iter(translated_replaceable)
    rebuilt = bytearray()

    for index, raw_line in enumerate(original_raw_lines, start=1):
        decoded_line = original_text_lines[index - 1]
        if not is_replaceable_line(decoded_line, index):
            rebuilt.extend(raw_line)
            continue

        translated_line = next(translated_iter)
        original_visible, suffix, line_ending, marker = split_visible_text_and_suffix(
            raw_line, decoded_line
        )
        visible_translated = trim_translated_visible_text(translated_line, marker)
        visible_translated = normalize_trailing_colons(
            visible_translated, original_visible, bool(suffix)
        )
        rebuilt.extend(visible_translated.encode("utf-8"))
        rebuilt.extend(suffix)
        rebuilt.extend(line_ending)

    return bytes(rebuilt)


def write_lines(original_path: Path, path: Path, lines: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(rebuild_file_bytes_preserving_structure(original_path, lines))


def process_file(
    original_path: Path,
    translated_path: Path,
    output_path: Path,
    apply_changes: bool,
    strict: bool,
) -> FileResult:
    original_lines = read_lines(original_path)
    translated_lines = read_lines(translated_path)
    original_by_id, duplicate_ids = index_original_lines(original_lines)

    working_lines = translated_lines.copy()
    fixes: list[LineFix] = []
    manual_issues: list[ManualIssue] = []

    for idx, translated_line in enumerate(translated_lines, start=1):
        record_id = get_record_id(translated_line)
        if not record_id:
            continue

        if record_id in duplicate_ids:
            manual_issues.append(
                ManualIssue(
                    line_number=idx,
                    record_id=record_id,
                    reason="ID duplicado no arquivo original; alinhamento ambíguo",
                )
            )
            continue

        original_line = original_by_id.get(record_id)
        if original_line is None:
            manual_issues.append(
                ManualIssue(
                    line_number=idx,
                    record_id=record_id,
                    reason="ID não encontrado no arquivo original",
                )
            )
            continue

        original_tokens = extract_tokens(original_line)
        translated_tokens = extract_tokens(translated_line)
        if original_tokens == translated_tokens:
            continue

        fixed_line, changed, failed = fix_line(original_line, translated_line)
        if failed:
            manual_issues.append(
                ManualIssue(
                    line_number=idx,
                    record_id=record_id,
                    reason="Não foi possível localizar os blocos [] com segurança",
                )
            )
            continue

        if extract_tokens(fixed_line) != original_tokens:
            manual_issues.append(
                ManualIssue(
                    line_number=idx,
                    record_id=record_id,
                    reason="Pós-validação falhou; [] final não bate com o original",
                )
            )
            continue

        if changed:
            fixes.append(
                LineFix(
                    line_number=idx,
                    record_id=record_id,
                    before=translated_line.rstrip("\r\n"),
                    after=fixed_line.rstrip("\r\n"),
                )
            )
            working_lines[idx - 1] = fixed_line

    strict_blocked = strict and bool(manual_issues)
    written = False

    if apply_changes and fixes and not strict_blocked:
        write_lines(original_path, output_path, working_lines)
        written = True

    return FileResult(
        source_path=translated_path,
        output_path=output_path,
        fixes=fixes,
        manual_issues=manual_issues,
        written=written,
        strict_blocked=strict_blocked,
    )


def iter_target_files(pt_dir: Path, file_name: str | None) -> list[Path]:
    if file_name:
        return [pt_dir / file_name]
    return sorted(pt_dir.glob("*.epk_dec"))


def write_reports(out_dir: Path, results: list[FileResult]) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)

    manual_csv = out_dir / "manual_review.csv"
    with manual_csv.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(["arquivo", "linha_ptbr", "record_id", "motivo"])
        for result in results:
            for issue in result.manual_issues:
                writer.writerow(
                    [
                        result.source_path.name,
                        issue.line_number,
                        issue.record_id,
                        issue.reason,
                    ]
                )

    fixed_csv = out_dir / "fixed_files.csv"
    with fixed_csv.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(
            [
                "arquivo",
                "saida",
                "linhas_corrigidas",
                "linhas_revisao_manual",
                "gravado",
                "strict_bloqueou",
            ]
        )
        for result in results:
            writer.writerow(
                [
                    result.source_path.name,
                    result.output_path.name,
                    ";".join(str(item.line_number) for item in result.fixes),
                    ";".join(str(item.line_number) for item in result.manual_issues),
                    "sim" if result.written else "nao",
                    "sim" if result.strict_blocked else "nao",
                ]
            )


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Compara arquivos originais com scripts_pt-br usando o ID da mensagem, "
            "corrige apenas os blocos [] quebrados e grava as versões novas em "
            "uma pasta separada."
        )
    )
    parser.add_argument(
        "--orig-dir",
        type=Path,
        default=Path("."),
        help="Pasta com os arquivos originais .epk_dec",
    )
    parser.add_argument(
        "--pt-dir",
        type=Path,
        default=Path("scripts_pt-br"),
        help="Pasta com os arquivos traduzidos .epk_dec",
    )
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=Path("correções"),
        help="Pasta onde os arquivos corrigidos serão gravados",
    )
    parser.add_argument(
        "--file",
        help="Processa apenas um arquivo especifico",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Grava os arquivos corrigidos em --out-dir. Sem esta flag, roda em dry-run.",
    )
    parser.add_argument(
        "--no-strict",
        action="store_true",
        help="Permite gravar correções parciais mesmo se houver linhas para revisão manual.",
    )
    args = parser.parse_args()

    strict = not args.no_strict
    pt_files = iter_target_files(args.pt_dir, args.file)
    if not pt_files:
        print("Nenhum arquivo alvo encontrado.")
        return 1

    results: list[FileResult] = []
    total_written = 0
    total_fixed_lines = 0
    total_manual_lines = 0

    mode_label = "APPLY" if args.apply else "DRY-RUN"
    strict_label = "STRICT ON" if strict else "STRICT OFF"
    print(f"{mode_label} | {strict_label}")

    for translated_path in pt_files:
        if not translated_path.exists():
            print(f"[IGNORADO] Arquivo nao encontrado: {translated_path}")
            continue

        original_path = args.orig_dir / translated_path.name
        if not original_path.exists():
            print(f"[IGNORADO] Original nao encontrado para: {translated_path.name}")
            continue

        output_path = args.out_dir / translated_path.name
        result = process_file(
            original_path=original_path,
            translated_path=translated_path,
            output_path=output_path,
            apply_changes=args.apply,
            strict=strict,
        )
        results.append(result)

        if not result.fixes and not result.manual_issues:
            continue

        total_fixed_lines += len(result.fixes)
        total_manual_lines += len(result.manual_issues)
        if result.written:
            total_written += 1

        print(f"\nArquivo: {translated_path.name}")
        if result.fixes:
            verb = "seriam corrigidas" if not args.apply else "corrigidas"
            print(f"  Linhas que {verb}: {', '.join(str(item.line_number) for item in result.fixes)}")
        if result.manual_issues:
            print(
                "  Linhas para revisar manualmente: "
                + ", ".join(str(item.line_number) for item in result.manual_issues)
            )
        if result.strict_blocked:
            print("  Status: bloqueado pelo strict; arquivo nao foi gravado")
        elif result.written:
            print(f"  Status: gravado em {result.output_path}")

    if args.apply:
        write_reports(args.out_dir, results)

    print("\nResumo")
    print(f"Arquivos analisados: {len(results)}")
    print(f"Linhas corrigiveis detectadas: {total_fixed_lines}")
    print(f"Linhas para revisao manual: {total_manual_lines}")
    if args.apply:
        print(f"Arquivos gravados em {args.out_dir}: {total_written}")
        print(f"Planilha CSV de revisao manual: {args.out_dir / 'manual_review.csv'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
