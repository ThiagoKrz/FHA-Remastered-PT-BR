from __future__ import annotations

import argparse
import csv
import re
import sys
from dataclasses import dataclass
from pathlib import Path

from fix_epk_script_blocks import (
    BRACKET_RE,
    get_record_id,
    index_original_lines,
    read_lines,
    rebuild_file_bytes_preserving_structure,
    split_line_parts,
)


TAG_RE = re.compile(r"__TAG\d+_?")
NO_THINK_RE = re.compile(r"/no_think")
MULTISPACE_RE = re.compile(r" {2,}")
ARTIFACT_AT_START_RE = re.compile(r"^\s*(?:__TAG\d+_?|/no_think)")
ARTIFACT_AT_END_RE = re.compile(r"(?:__TAG\d+_?|/no_think)\s*$")


@dataclass
class LineChange:
    line_number: int
    record_id: str
    change_kinds: list[str]
    before: str
    after: str


@dataclass
class FileResult:
    path: Path
    changes: list[LineChange]
    skipped: list[tuple[int, str, str]]
    written: bool


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


def extract_visible_text_from_segments(segments: list[list[object]]) -> str:
    return "".join(str(text) for is_bracket, text in segments if not is_bracket)


def count_leading_quotes(text: str) -> int:
    stripped = text.lstrip()
    count = 0
    while count < len(stripped) and stripped[count] == '"':
        count += 1
    return count


def count_trailing_quotes(text: str) -> int:
    stripped = text.rstrip()
    count = 0
    while count < len(stripped) and stripped[-(count + 1)] == '"':
        count += 1
    return count


def set_leading_quote_count(segments: list[list[object]], desired_count: int) -> bool:
    for segment in segments:
        is_bracket, text = segment
        if is_bracket:
            continue
        text = str(text)
        leading_ws_len = len(text) - len(text.lstrip())
        leading_ws = text[:leading_ws_len]
        core = text[leading_ws_len:]
        current_count = len(core) - len(core.lstrip('"'))
        if current_count == desired_count:
            return False
        segment[1] = leading_ws + ('"' * desired_count) + core[current_count:]
        return True
    return False


def set_trailing_quote_count(segments: list[list[object]], desired_count: int) -> bool:
    for segment in reversed(segments):
        is_bracket, text = segment
        if is_bracket:
            continue
        text = str(text)
        trailing_ws_len = len(text) - len(text.rstrip())
        trailing_ws = text[len(text) - trailing_ws_len :] if trailing_ws_len else ""
        core = text[: len(text) - trailing_ws_len] if trailing_ws_len else text
        current_count = len(core) - len(core.rstrip('"'))
        if current_count == desired_count:
            return False
        segment[1] = core[: len(core) - current_count] + ('"' * desired_count) + trailing_ws
        return True
    return False


def cleanup_artifacts_in_segment(text: str) -> tuple[str, list[str]]:
    original_text = text
    kinds: list[str] = []

    if TAG_RE.search(text):
        text = TAG_RE.sub("", text)
        kinds.append("tag")

    if NO_THINK_RE.search(text):
        text = re.sub(r"\s*/no_think\s*", " ", text)
        kinds.append("no_think")

    if kinds:
        text = MULTISPACE_RE.sub(" ", text)
        if ARTIFACT_AT_START_RE.search(original_text):
            text = text.lstrip(" ")
        if ARTIFACT_AT_END_RE.search(original_text):
            text = text.rstrip(" ")

    return text, kinds


def cleanup_artifacts_in_segments(segments: list[list[object]]) -> list[str]:
    kinds: list[str] = []
    for segment in segments:
        is_bracket, text = segment
        if is_bracket:
            continue
        cleaned_text, segment_kinds = cleanup_artifacts_in_segment(str(text))
        if segment_kinds:
            segment[1] = cleaned_text
            kinds.extend(segment_kinds)
    return kinds


def normalize_spurious_prefix_punctuation(
    segments: list[list[object]],
    original_visible: str,
) -> bool:
    original_core = original_visible.lstrip().lstrip('"')
    for segment in segments:
        is_bracket, text = segment
        if is_bracket:
            continue
        text = str(text)
        leading_ws_len = len(text) - len(text.lstrip())
        leading_ws = text[:leading_ws_len]
        core = text[leading_ws_len:]
        leading_quotes_len = len(core) - len(core.lstrip('"'))
        leading_quotes = core[:leading_quotes_len]
        remainder = core[leading_quotes_len:]

        changed = False
        while remainder.startswith("_"):
            remainder = remainder[1:]
            changed = True

        if remainder.startswith(":") and not original_core.startswith(":"):
            remainder = remainder[1:].lstrip()
            changed = True

        if remainder.startswith(".") and not remainder.startswith("...") and not original_core.startswith("."):
            remainder = remainder[1:].lstrip()
            changed = True

        if changed:
            segment[1] = leading_ws + leading_quotes + remainder
            return True
        return False
    return False


def sync_outer_quotes(
    original_segments: list[list[object]],
    translated_segments: list[list[object]],
) -> bool:
    original_visible = extract_visible_text_from_segments(original_segments)
    translated_visible = extract_visible_text_from_segments(translated_segments)

    changed = False
    desired_leading = count_leading_quotes(original_visible)
    desired_trailing = count_trailing_quotes(original_visible)

    if count_leading_quotes(translated_visible) != desired_leading:
        changed |= set_leading_quote_count(translated_segments, desired_leading)

    translated_visible = extract_visible_text_from_segments(translated_segments)
    if count_trailing_quotes(translated_visible) != desired_trailing:
        changed |= set_trailing_quote_count(translated_segments, desired_trailing)

    return changed


def cleanup_record_line(original_line: str, translated_line: str) -> tuple[str, list[str], str | None]:
    original_parts = split_line_parts(original_line, allow_unterminated=True)
    translated_parts = split_line_parts(translated_line, allow_unterminated=True)
    if original_parts is None or translated_parts is None:
        return translated_line, [], "nao foi possivel separar a linha com seguranca"

    original_prefix, original_body, _ = original_parts
    translated_prefix, translated_body, translated_suffix = translated_parts
    if original_prefix != translated_prefix:
        return translated_line, [], "prefixo da linha nao bate com o original"

    original_segments = split_segments(original_body)
    translated_segments = split_segments(translated_body)

    kinds = cleanup_artifacts_in_segments(translated_segments)
    if normalize_spurious_prefix_punctuation(
        translated_segments,
        extract_visible_text_from_segments(original_segments),
    ):
        kinds.append("prefix_punct")
    if sync_outer_quotes(original_segments, translated_segments):
        kinds.append("quotes")

    cleaned_body = join_segments(translated_segments)
    cleaned_line = translated_prefix + cleaned_body + translated_suffix
    unique_kinds = sorted(set(kinds))
    return cleaned_line, unique_kinds, None


def write_report(path: Path, results: list[FileResult]) -> None:
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(
            ["arquivo", "linha", "record_id", "tipos", "before", "after"]
        )
        for result in results:
            for change in result.changes:
                writer.writerow(
                    [
                        result.path.name,
                        change.line_number,
                        change.record_id,
                        ";".join(change.change_kinds),
                        change.before,
                        change.after,
                    ]
                )


def write_skipped_report(path: Path, results: list[FileResult]) -> None:
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(["arquivo", "linha", "record_id", "motivo"])
        for result in results:
            for line_number, record_id, reason in result.skipped:
                writer.writerow([result.path.name, line_number, record_id, reason])


def process_file(
    original_path: Path,
    translated_path: Path,
    apply_changes: bool,
) -> FileResult:
    original_lines = read_lines(original_path)
    translated_lines = read_lines(translated_path)
    original_by_id, duplicate_ids = index_original_lines(original_lines)

    working_lines = translated_lines.copy()
    changes: list[LineChange] = []
    skipped: list[tuple[int, str, str]] = []

    for idx, translated_line in enumerate(translated_lines, start=1):
        record_id = get_record_id(translated_line)
        if not record_id:
            continue

        if record_id in duplicate_ids:
            skipped.append((idx, record_id, "record_id duplicado no original"))
            continue

        original_line = original_by_id.get(record_id)
        if original_line is None:
            skipped.append((idx, record_id, "record_id nao encontrado no original"))
            continue

        cleaned_line, kinds, error = cleanup_record_line(original_line, translated_line)
        if error:
            skipped.append((idx, record_id, error))
            continue

        if not kinds or cleaned_line == translated_line:
            continue

        changes.append(
            LineChange(
                line_number=idx,
                record_id=record_id,
                change_kinds=kinds,
                before=translated_line.rstrip("\r\n"),
                after=cleaned_line.rstrip("\r\n"),
            )
        )
        working_lines[idx - 1] = cleaned_line

    written = False
    if apply_changes and changes:
        translated_path.write_bytes(
            rebuild_file_bytes_preserving_structure(original_path, working_lines)
        )
        written = True

    return FileResult(
        path=translated_path,
        changes=changes,
        skipped=skipped,
        written=written,
    )


def iter_target_files(pt_dir: Path, file_name: str | None) -> list[Path]:
    if file_name:
        return [pt_dir / file_name]
    return sorted(pt_dir.glob("*.epk_dec"))


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Primeiro lote de limpeza dos .epk_dec: remove __TAG, remove /no_think "
            "e sincroniza aspas externas das falas por record_id, preservando a "
            "estrutura bruta do arquivo."
        )
    )
    parser.add_argument("--orig-dir", type=Path, default=Path("."))
    parser.add_argument("--pt-dir", type=Path, default=Path("scripts_pt-br"))
    parser.add_argument("--file")
    parser.add_argument("--apply", action="store_true")
    parser.add_argument(
        "--report",
        type=Path,
        default=Path("first_lot_cleanup_report.csv"),
    )
    parser.add_argument(
        "--skipped-report",
        type=Path,
        default=Path("first_lot_cleanup_skipped.csv"),
    )
    args = parser.parse_args()

    targets = iter_target_files(args.pt_dir, args.file)
    if not targets:
        print("Nenhum arquivo alvo encontrado.")
        return 1

    mode = "APPLY" if args.apply else "DRY-RUN"
    print(mode)

    results: list[FileResult] = []
    changed_files = 0
    changed_lines = 0
    kind_counts = {"tag": 0, "no_think": 0, "quotes": 0, "prefix_punct": 0}
    skipped_total = 0

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
            apply_changes=args.apply,
        )
        results.append(result)

        if not result.changes and not result.skipped:
            continue

        skipped_total += len(result.skipped)
        if result.changes:
            changed_files += 1
            changed_lines += len(result.changes)
            for change in result.changes:
                for kind in change.change_kinds:
                    kind_counts[kind] = kind_counts.get(kind, 0) + 1

            verb = "seriam corrigidas" if not args.apply else "corrigidas"
            line_list = ", ".join(str(item.line_number) for item in result.changes[:30])
            if len(result.changes) > 30:
                line_list += ", ..."
            print(f"\nArquivo: {translated_path.name}")
            print(f"  Linhas {verb}: {line_list}")
            if result.written:
                print("  Status: gravado")

        if result.skipped:
            if not result.changes:
                print(f"\nArquivo: {translated_path.name}")
            skipped_preview = ", ".join(str(line_number) for line_number, _, _ in result.skipped[:15])
            if len(result.skipped) > 15:
                skipped_preview += ", ..."
            print(f"  Linhas puladas: {skipped_preview}")

    write_report(args.report, results)
    write_skipped_report(args.skipped_report, results)

    print("\nResumo")
    print(f"Arquivos analisados: {len(results)}")
    print(f"Arquivos com alteracoes: {changed_files}")
    print(f"Linhas alteradas: {changed_lines}")
    print(f"  tag removido: {kind_counts['tag']}")
    print(f"  /no_think removido: {kind_counts['no_think']}")
    print(f"  aspas sincronizadas: {kind_counts['quotes']}")
    print(f"  prefixo limpo: {kind_counts['prefix_punct']}")
    print(f"Linhas puladas: {skipped_total}")
    print(f"Relatorio: {args.report}")
    print(f"Puladas: {args.skipped_report}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
