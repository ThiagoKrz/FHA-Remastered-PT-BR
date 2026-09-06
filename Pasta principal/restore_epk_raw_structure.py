from __future__ import annotations

import argparse
from pathlib import Path

from fix_epk_script_blocks import rebuild_file_bytes_preserving_structure, split_text_lines


def iter_target_files(pt_dir: Path, file_name: str | None) -> list[Path]:
    if file_name:
        return [pt_dir / file_name]
    return sorted(pt_dir.glob("*.epk_dec"))


def strip_malformed_trailers_for_edit(path: Path) -> bytes:
    cleaned_lines: list[bytes] = []
    for raw_line in path.read_bytes().splitlines():
        cleaned = raw_line.rstrip(b"\r")
        try:
            cleaned.decode("utf-8")
        except UnicodeDecodeError:
            if not cleaned[:1].isdigit():
                continue
        if cleaned[:1].isdigit():
            final_delimiter = cleaned.rfind(b"::")
            if final_delimiter >= 0:
                candidate = cleaned[: final_delimiter + 2]
                try:
                    candidate.decode("utf-8")
                except UnicodeDecodeError:
                    pass
                else:
                    cleaned = candidate
        cleaned_lines.append(cleaned)
    return b"\n".join(cleaned_lines) + b"\n"


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Reconstrói os .epk_dec traduzidos preservando os bytes estruturais "
            "do original (fim de linha, trailer e bytes especiais de EOF), sem "
            "alterar o texto lógico traduzido."
        )
    )
    parser.add_argument("--orig-dir", type=Path, default=Path("."))
    parser.add_argument(
        "--source-dir",
        type=Path,
        help="Pasta-fonte para ler o texto traduzido atual. Se omitido, usa --pt-dir.",
    )
    parser.add_argument("--pt-dir", type=Path, default=Path("scripts_pt-br"))
    parser.add_argument("--file")
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Grava as alterações nos arquivos traduzidos. Sem isso, roda em dry-run.",
    )
    parser.add_argument(
        "--prepare-edit",
        action="store_true",
        help=(
            "Remove apenas trailers binários após o :: final e normaliza LF para "
            "permitir edição manual; não altera o texto lógico traduzido."
        ),
    )
    args = parser.parse_args()
    source_dir = args.source_dir or args.pt_dir

    changed = 0
    skipped = 0
    targets = iter_target_files(args.pt_dir, args.file)

    mode = "APPLY" if args.apply else "DRY-RUN"
    print(mode)

    for translated_path in targets:
        source_path = source_dir / translated_path.name
        original_path = args.orig_dir / translated_path.name
        if not original_path.exists():
            print(f"[SEM ORIGINAL] {translated_path.name}")
            skipped += 1
            continue
        if not source_path.exists():
            print(f"[SEM FONTE] {translated_path.name}")
            skipped += 1
            continue

        if args.prepare_edit:
            cleaned_bytes = strip_malformed_trailers_for_edit(source_path)
            current_bytes = translated_path.read_bytes()
            if cleaned_bytes == current_bytes:
                continue
            changed += 1
            print(f"[PREPARE EDIT] {translated_path.name}")
            if args.apply:
                translated_path.write_bytes(cleaned_bytes)
            continue

        translated_lines = split_text_lines(
            source_path.read_text(encoding="utf-8", errors="replace"),
            keepends=True,
        )
        rebuilt_bytes = rebuild_file_bytes_preserving_structure(
            original_path, translated_lines
        )
        current_bytes = translated_path.read_bytes()

        if rebuilt_bytes == current_bytes:
            continue

        changed += 1
        print(f"[REBUILD] {translated_path.name}")
        if args.apply:
            translated_path.write_bytes(rebuilt_bytes)

    print()
    print(f"Arquivos analisados: {len(targets)}")
    print(f"Arquivos reestruturados: {changed}")
    print(f"Arquivos sem original: {skipped}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
