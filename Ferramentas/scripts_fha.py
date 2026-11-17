"""JSONs trilingues e exportação de .epk_dec para Fate/hollow ataraxia Remastered.

Python 3.10+. Organiza os scripts em Pasta principal/trabalho no padrão do projeto Mahoyo.
"""
from __future__ import annotations

import argparse
import collections
import csv
import hashlib
import json
from pathlib import Path
import re
import sys
import unicodedata

ROOT = Path(__file__).resolve().parents[1]
MAIN_DIR = ROOT / 'Pasta principal'
WORK = MAIN_DIR / 'trabalho'
DEFAULT_OUTPUT = MAIN_DIR / 'build' / 'epk_dec'
DEFAULT_SPREADSHEET = ROOT / 'Planilha_Progresso_FHA.xlsx'

ROTA_GROUPS = [
    ('Prólogo', '00_prologo'),
    ('Dia 1', '01_dia_1'),
    ('Dia 2', '02_dia_2'),
    ('Dia 3', '03_dia_3'),
    ('Dia 4', '04_dia_4'),
    ('Noite', '05_noite'),
    ('Caren', '06_caren'),
    ('Lancer', '07_lancer'),
    ('Acampamento', '08_acampamento'),
    ('Castelo Einzbern', '09_castelo_einzbern'),
    ('Especial', '10_especial'),
    ('Mapa Oculto', '11_mapa_oculto'),
    ('Santuário', '12_santuario'),
    ('Hanafuda', '13_hanafuda'),
    ('Sistema', '14_sistema'),
]
ROTA_TO_GROUP = dict(ROTA_GROUPS)
GROUP_TO_ROTA = {g: r for r, g in ROTA_GROUPS}

SYSTEM_FILES = {
    'bgm_data.epk_dec',
    'flaglist_data.epk_dec',
    'ir_item.epk_dec',
    'ir_quiz.epk_dec',
    'popup_data.epk_dec',
    'quiz_oni.epk_dec',
    'statictext.epk_dec',
    'uistring.epk_dec',
}

# Índice (0-based dentro das colunas após id e label) do campo principal de texto por schema
TEXT_COL_BY_SCHEMA = {
    'id=qid::label=str::text=lstr::': 0,
    'id=qid::label=str::chipidx=i::title_name=str::': 1,
    'id=qid::label=str::flag_index=i::sort=i::finename=str::title=lstr::': 3,
    'id=qid::label=str::name=lstr::caption=lstr::description=lstr::': 0,
    'id=qid::label=str::question=lstr::voice_kot=str::voice_tig=str::answer=B::': 0,
    'id=qid::label=str::maintext=lstr::subtext=lstr::flag=str::': 0,
    'id=qid::label=str::string=lstr::alternum=i::answer=B::': 0,
    'id=qid::label=str::string=lstr::string_jp=str::': 0,
}


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def read_json(path: Path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))


def write_json(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def decode_epk_bytes(raw: bytes) -> str:
    for enc in ('utf-8-sig', 'cp1252', 'latin-1'):
        try:
            return raw.decode(enc)
        except UnicodeDecodeError:
            continue
    return raw.decode('utf-8', errors='replace')


def parse_epk_dec(raw: bytes) -> tuple[str, str, list[tuple[str, str, list[str]]]]:
    """Lê um .epk_dec retornando (magic, schema, [(epk_id, label, rest_fields), ...])."""
    text = decode_epk_bytes(raw)
    lines = text.splitlines()
    if len(lines) < 2 or lines[0].strip() != 'DAT':
        raise ValueError('Cabeçalho DAT inválido.')
    magic = lines[0]
    schema = lines[1]
    raw_records: list[str] = []
    cur: list[str] = []
    for line in lines[2:]:
        if re.match(r'^\d+::', line):
            if cur:
                raw_records.append('\n'.join(cur))
            cur = [line]
        elif cur:
            cur.append(line)
    if cur:
        raw_records.append('\n'.join(cur))

    records: list[tuple[str, str, list[str]]] = []
    for rec in raw_records:
        cleaned = rec[:-2] if rec.endswith('::') else rec
        parts = cleaned.split('::')
        epk_id = parts[0]
        label = parts[1] if len(parts) > 1 else ''
        rest = parts[2:] if len(parts) > 2 else ['']
        records.append((epk_id, label, rest))
    return magic, schema, records


def group_for(filename: str, rota: str | None = None) -> str:
    if rota and rota in ROTA_TO_GROUP:
        return ROTA_TO_GROUP[rota]
    return '14_sistema' if filename in SYSTEM_FILES else '99_outros'


def _safe_slug(text: str, max_len: int = 42) -> str:
    norm = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')
    slug = re.sub(r'[^A-Za-z0-9]+', '_', norm).strip('_')
    return (slug[:max_len].rstrip('_') or 'cena')


def _load_spreadsheet_map(path: Path) -> dict[str, dict]:
    """Lê Título da Cena, Rota e ordem a partir de Planilha_Progresso_FHA.xlsx."""
    if not path.exists():
        return {}
    import openpyxl
    wb = openpyxl.load_workbook(path, data_only=True, read_only=True)
    ws = wb['Geral'] if 'Geral' in wb.sheetnames else wb.active
    mapping: dict[str, dict] = {}
    order = 0
    for row in ws.iter_rows(min_row=3, values_only=True):
        if not row or len(row) < 6 or not row[1]:
            continue
        order += 1
        title = str(row[0] or '').strip()
        script_name = str(row[1]).strip()
        rota = str(row[5] or '').strip()
        mapping[script_name] = {
            'title': title or Path(script_name).stem,
            'rota': rota,
            'order': order,
        }
    wb.close()
    return mapping


def _write_launcher_files(work: Path) -> None:
    cmd_content = (
        '@echo off\r\n'
        'setlocal\r\n'
        'cd /d "%~dp0"\r\n'
        'where pythonw.exe >nul 2>&1\r\n'
        'if not errorlevel 1 (\r\n'
        '    start "" pythonw.exe "%~dp0Painel.pyw"\r\n'
        '    exit /b\r\n'
        ')\r\n'
        'where python.exe >nul 2>&1\r\n'
        'if not errorlevel 1 (\r\n'
        '    start "" python.exe "%~dp0Painel.pyw"\r\n'
        '    exit /b\r\n'
        ')\r\n'
        'echo Python com Tkinter nao foi encontrado. Instale Python 3.10 ou superior.\r\n'
        'pause\r\n'
    )
    (work / 'Abrir painel.cmd').write_bytes(cmd_content.encode('utf-8'))

    root_cmd = (
        '@echo off\r\n'
        'setlocal\r\n'
        'cd /d "%~dp0Pasta principal\\trabalho"\r\n'
        'where pythonw.exe >nul 2>&1\r\n'
        'if not errorlevel 1 (\r\n'
        '    start "" pythonw.exe "%~dp0Pasta principal\\trabalho\\Painel.pyw"\r\n'
        '    exit /b\r\n'
        ')\r\n'
        'where python.exe >nul 2>&1\r\n'
        'if not errorlevel 1 (\r\n'
        '    start "" python.exe "%~dp0Pasta principal\\trabalho\\Painel.pyw"\r\n'
        '    exit /b\r\n'
        ')\r\n'
        'echo Python com Tkinter nao foi encontrado. Instale Python 3.10 ou superior.\r\n'
        'pause\r\n'
    )
    (ROOT / 'Abrir painel.cmd').write_bytes(root_cmd.encode('utf-8'))

    pyw_content = '''"""Abra este arquivo para revisar os textos de FHA e exportar os .epk_dec."""
from pathlib import Path
import sys
import traceback

root = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(root / 'Ferramentas'))
try:
    from painel_fha import main
    main()
except Exception:
    log = Path(__file__).resolve().parent / 'erro_ao_abrir_painel.log'
    log.write_text(traceback.format_exc(), encoding='utf-8')
    try:
        import tkinter as tk
        from tkinter import messagebox
        app = tk.Tk()
        app.withdraw()
        messagebox.showerror('Falha ao abrir o painel', f'Confira o log:\\n{log}\\n\\n{traceback.format_exc()}')
    except Exception:
        pass
'''
    (work / 'Painel.pyw').write_text(pyw_content, encoding='utf-8')

    readme = """# Revisão de scripts — Fate/hollow ataraxia Remastered (PT-BR)

Abra `Abrir painel.cmd` (ou `Painel.pyw`) para revisar os JSONs trilingues e exportar os `.epk_dec`.

- **`00_sistema_e_ui/`**: arquivos de interface e tabelas de sistema (`uistring`, `statictext`, `bgm_data`, etc.).
- **`01_cenas/`**: scripts de história/cenas.
- **`originais/`**: referências imutáveis (`jp`, `en`, `pt_inicial` e estrutura dos `.epk_dec`) usadas na validação e restauração.
- **`backups/` e `logs/`**: backups automáticos e logs de validação.
"""
    (work / 'LEIA-ME.md').write_text(readme, encoding='utf-8')
    (work / '.gitignore').write_text('backups/\nlogs/\n.preferencias.json\nerro_ao_abrir_painel.log\n', encoding='utf-8')


def prepare(args):
    work = args.trabalho.resolve()
    if work.exists() and any(work.iterdir()):
        raise ValueError(f'Pasta já existe e não está vazia; não será sobrescrita: {work}')

    jp_dir = (args.fontes / 'scripts_jp').resolve()
    en_dir = (args.fontes / 'scripts_en').resolve()
    pt_dir = (args.fontes / 'scripts_pt-br').resolve()

    pt_files = sorted(pt_dir.glob('*.epk_dec'))
    if not pt_files:
        raise ValueError(f'Nenhum .epk_dec encontrado em {pt_dir}')

    sheet_map = _load_spreadsheet_map(args.planilha.resolve())
    pt_files.sort(key=lambda f: (sheet_map.get(f.name, {}).get('order', 99999), f.name))

    jp_orig: list[str] = []
    en_orig: list[str] = []
    pt_orig: list[str] = []
    scenes: dict[str, dict] = {}
    epk_meta: dict[str, dict] = {}

    global_offset = 0
    for idx_file, pt_path in enumerate(pt_files, 1):
        fname = pt_path.name
        scene = pt_path.stem
        jp_path = jp_dir / fname
        en_path = en_dir / fname
        if not jp_path.exists() or not en_path.exists():
            raise ValueError(f'Arquivo ausente em JP ou EN: {fname}')

        magic, schema, recs_pt = parse_epk_dec(pt_path.read_bytes())
        _, _, recs_jp = parse_epk_dec(jp_path.read_bytes())
        _, _, recs_en = parse_epk_dec(en_path.read_bytes())

        if not (len(recs_pt) == len(recs_jp) == len(recs_en)):
            raise ValueError(f'Contagem diverge em {fname}: JP={len(recs_jp)}, EN={len(recs_en)}, PT={len(recs_pt)}')

        info = sheet_map.get(fname, {})
        title = info.get('title', scene)
        rota = info.get('rota', '')
        order = info.get('order', idx_file)
        text_col = TEXT_COL_BY_SCHEMA.get(schema, 0)
        group = group_for(fname, rota)
        slug = _safe_slug(title)
        offsets: list[int] = []
        rec_templates: list[dict] = []

        for (epk_id, label, rest_pt), (_, _, rest_jp), (_, _, rest_en) in zip(recs_pt, recs_jp, recs_en):
            jp_val = rest_jp[text_col] if text_col < len(rest_jp) else ''
            en_val = rest_en[text_col] if text_col < len(rest_en) else ''
            pt_val = rest_pt[text_col] if text_col < len(rest_pt) else ''

            jp_orig.append(jp_val)
            en_orig.append(en_val)
            pt_orig.append(pt_val)

            offsets.append(global_offset)
            rec_templates.append({
                'epk_id': epk_id,
                'label': label,
                'rest': rest_pt,
            })
            global_offset += 1

        scenes[scene] = {
            'group': group,
            'rota': rota or GROUP_TO_ROTA.get(group, 'Outros'),
            'title': title,
            'order': order,
            'filename': fname,
            'offsets': offsets,
            'path': f'{group}/{order:03d}_{slug}__{scene}.json',
        }
        epk_meta[scene] = {
            'magic': magic,
            'schema': schema,
            'text_col': text_col,
            'records': rec_templates,
        }

    work.mkdir(parents=True, exist_ok=True)
    orig_dir = work / 'originais'
    orig_dir.mkdir(exist_ok=True)

    refs_bytes = (json.dumps({'jp': jp_orig, 'en': en_orig, 'pt_inicial': pt_orig}, ensure_ascii=False) + '\n').encode('utf-8')
    (orig_dir / 'referencias.json').write_bytes(refs_bytes)

    meta_bytes = (json.dumps(epk_meta, ensure_ascii=False) + '\n').encode('utf-8')
    (orig_dir / 'epk_meta.json').write_bytes(meta_bytes)

    for scene, meta in scenes.items():
        pass

    # Escreve os JSONs por cena
    for scene, meta in scenes.items():
        start = meta['offsets'][0]
        recs = epk_meta[scene]['records']
        linhas = [
            {
                'en': en_orig[start + idx],
                'jp': jp_orig[start + idx],
                'Pt-br': pt_orig[start + idx],
                'id': start + idx + 1,
                'epk_id': rec['epk_id'],
                'label': rec['label'],
            }
            for idx, rec in enumerate(recs)
        ]
        write_json(work / meta['path'], {
            'cena': scene,
            'titulo': meta['title'],
            'rota': meta['rota'],
            'arquivo': meta['filename'],
            'linhas': linhas,
        })

    manifest = {
        'version': 2,
        'project': 'fha-remastered',
        'line_count': global_offset,
        'sources': {
            'referencias': {'filename': 'referencias.json', 'sha256': sha(refs_bytes)},
            'epk_meta': {'filename': 'epk_meta.json', 'sha256': sha(meta_bytes)},
        },
        'scenes': scenes,
    }
    write_json(work / 'manifesto.json', manifest)

    with (work / 'indice.tsv').open('w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerow(['linha_global', 'pasta', 'cena', 'arquivo_epk', 'epk_id', 'label'])
        for scene, meta in scenes.items():
            recs = epk_meta[scene]['records']
            for offset, rec in zip(meta['offsets'], recs):
                writer.writerow([offset + 1, meta['group'], scene, meta['filename'], rec['epk_id'], rec['label']])

    _write_launcher_files(work)

    print(json.dumps({
        'linhas': global_offset,
        'cenas': len(scenes),
        'rotas': len({s['group'] for s in scenes.values()}),
        'trabalho': str(work),
    }, ensure_ascii=False, indent=2))


def validate(args):
    from projeto_json_fha import require_valid
    inspection = require_valid(args.trabalho.resolve())
    print(json.dumps({
        'linhas': inspection.manifest['line_count'],
        'cenas': len(inspection.manifest['scenes']),
        'avisos': len(inspection.issues),
        'alinhamento': 'ok',
        'fontes_jp_en': 'intactas',
    }, ensure_ascii=False))


def compile_work(args):
    from projeto_json_fha import export_epk_dec, require_valid
    work = args.trabalho.resolve()
    inspection = require_valid(work)
    report = export_epk_dec(work, args.saida.resolve(), inspection=inspection)
    print(json.dumps(report, ensure_ascii=False))


def install_cmd(args):
    from projeto_json_fha import compile_and_install_epk, require_valid
    work = args.trabalho.resolve()
    inspection = require_valid(work)
    report = compile_and_install_epk(
        work,
        mod_epk_dir=args.mod_dir.resolve() if args.mod_dir else None,
        inspection=inspection,
    )
    print(json.dumps(report, ensure_ascii=False))


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--trabalho', type=Path, default=WORK)
    commands = parser.add_subparsers(dest='command', required=True)

    p = commands.add_parser('preparar', help='Cria Pasta principal/trabalho a partir dos .epk_dec.')
    p.add_argument('--fontes', type=Path, default=MAIN_DIR)
    p.add_argument('--planilha', type=Path, default=DEFAULT_SPREADSHEET)
    p.set_defaults(func=prepare)

    p = commands.add_parser('validar', help='Valida todos os JSONs, referências e tags.')
    p.set_defaults(func=validate)

    p = commands.add_parser('recompilar', help='Valida e exporta os .epk_dec atualizados.')
    p.add_argument('--saida', type=Path, default=DEFAULT_OUTPUT)
    p.set_defaults(func=compile_work)

    p = commands.add_parser('instalar', help='Valida, compila os .epk e instala na pasta do mod.')
    p.add_argument('--mod-dir', type=Path, default=None)
    p.set_defaults(func=install_cmd)

    args = parser.parse_args(argv)
    try:
        args.func(args)
    except (ValueError, OSError, KeyError) as exc:
        print(f'Erro: {exc}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
