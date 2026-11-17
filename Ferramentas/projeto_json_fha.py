"""Validação completa, restauração e exportação de .epk_dec para FHA Remastered."""
from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile

import scripts_fha as scripts


@dataclass
class Issue:
    message: str
    file: str = ''
    scene: str = ''
    row_id: int | None = None
    field: str = ''
    json_line: int | None = None
    column: int | None = None
    severity: str = 'erro'


@dataclass
class Inspection:
    manifest: dict = field(default_factory=dict)
    values: dict = field(default_factory=dict)
    original: dict = field(default_factory=dict)
    epk_meta: dict = field(default_factory=dict)
    locations: dict = field(default_factory=dict)
    fingerprints: dict = field(default_factory=dict)
    issues: list = field(default_factory=list)

    @property
    def errors(self):
        return [i for i in self.issues if i.severity == 'erro']


def no_duplicate_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f'Chave JSON duplicada: {key}')
        result[key] = value
    return result


def parse_json(text: str):
    return json.loads(text, object_pairs_hook=no_duplicate_keys)


def read_scene(path: Path):
    return parse_json(path.read_text(encoding='utf-8-sig'))


def check_brackets(text: str) -> str | None:
    depth = 0
    for ch in text:
        if ch == '[':
            depth += 1
        elif ch == ']':
            if depth == 0:
                return 'Colchete "]" sem "[" correspondente.'
            depth -= 1
    if depth > 0:
        return 'Colchete "[" não fechado com "]".'
    return None


def inspect_project(work: Path) -> Inspection:
    work = work.resolve()
    result = Inspection()

    def error(message, path='', scene='', row_id=None, field='', **extra):
        result.issues.append(Issue(message, str(path), scene, row_id, field, **extra))

    try:
        result.manifest = read_scene(work / 'manifesto.json')
        manifest = result.manifest
        if manifest.get('version') != 2:
            raise ValueError('Versão esperada: 2 (JSON trilingue).')
        count = manifest['line_count']
        if type(count) is not int or count < 1 or not isinstance(manifest['scenes'], dict):
            raise ValueError('Manifesto com contagem ou cenas inválidas.')

        refs_meta = manifest['sources']['referencias']
        refs_path = work / 'originais' / refs_meta['filename']
        refs_raw = refs_path.read_bytes()
        if scripts.sha(refs_raw) != refs_meta['sha256']:
            error('Backup original (referencias.json) foi alterado.', refs_path)
        refs_data = json.loads(refs_raw.decode('utf-8-sig'))
        for key, lang in [('jp', 'JP'), ('en', 'EN'), ('pt_inicial', 'PT-BR')]:
            if len(refs_data.get(key, [])) != count:
                raise ValueError(f'Contagem original diverge em {lang}.')
            result.original[lang] = refs_data[key]

        meta_info = manifest['sources']['epk_meta']
        meta_path = work / 'originais' / meta_info['filename']
        meta_raw = meta_path.read_bytes()
        if scripts.sha(meta_raw) != meta_info['sha256']:
            error('Metadados originais (epk_meta.json) foram alterados.', meta_path)
        result.epk_meta = json.loads(meta_raw.decode('utf-8-sig'))
    except (OSError, ValueError, KeyError, TypeError) as exc:
        error(f'Não foi possível ler as fontes do projeto: {exc}', work / 'manifesto.json')
        return result

    result.values = {language: [None] * count for language in ['JP', 'EN', 'PT-BR']}
    seen: dict[int, str] = {}
    expected_paths: set[Path] = set()

    for scene, meta in manifest['scenes'].items():
        offsets = meta.get('offsets', [])
        if not offsets:
            continue
        path = (work / meta['path']).resolve()
        if not path.is_relative_to(work) or path.suffix != '.json':
            error('Caminho de cena inválido no manifesto.', path, scene)
            continue
        expected_paths.add(path)
        expected = {offset + 1 for offset in offsets}
        if len(expected) != len(offsets) or any(type(n) is not int or not 1 <= n <= count for n in expected):
            error('IDs inválidos ou repetidos no manifesto.', path, scene)
            continue
        try:
            raw = path.read_bytes()
            result.fingerprints[str(path)] = scripts.sha(raw)
            data = parse_json(raw.decode('utf-8-sig'))
        except json.JSONDecodeError as exc:
            error(f'JSON inválido: {exc.msg}', path, scene, json_line=exc.lineno, column=exc.colno)
            continue
        except (OSError, UnicodeError, ValueError) as exc:
            error(f'Falha ao ler a cena: {exc}', path, scene)
            continue

        if not isinstance(data, dict) or data.get('cena') != scene or not isinstance(data.get('linhas'), list):
            error('Esperado objeto com "cena" correta e lista "linhas".', path, scene)
            continue

        records = data['linhas']
        if len(records) != len(expected):
            error(f'Contagem incorreta: esperado {len(expected)}, encontrado {len(records)}.', path, scene)

        file_seen: set[int] = set()
        for local, record in enumerate(records):
            if not isinstance(record, dict):
                error(f'Registro {local + 1} não é um objeto JSON.', path, scene)
                continue
            row_id = record.get('id')
            if type(row_id) is not int:
                error(f'Registro {local + 1}: "id" precisa ser inteiro.', path, scene, field='id')
                continue
            file_seen.add(row_id)
            if row_id not in expected:
                error('ID não pertence a esta cena.', path, scene, row_id, 'id')
                continue
            if row_id in seen:
                error(f'ID duplicado; já aparece em {seen[row_id]}.', path, scene, row_id, 'id')
                continue
            seen[row_id] = scene
            offset = row_id - 1
            result.locations[offset] = (scene, local, meta)

            for key, language in [('en', 'EN'), ('jp', 'JP'), ('Pt-br', 'PT-BR')]:
                if key not in record:
                    error(f'Campo obrigatório "{key}" ausente.', path, scene, row_id, key)
                    continue
                value = record[key]
                if not isinstance(value, str):
                    error(f'Campo "{key}" precisa ser texto, inclusive quando vazio.', path, scene, row_id, key)
                    continue
                result.values[language][offset] = value
                if language in ('JP', 'EN'):
                    if value != result.original[language][offset]:
                        error(f'Fonte {language} mudou; restaure a referência original.', path, scene, row_id, key)
                else:
                    if any(c in value for c in '\r\x00\u2028\u2029'):
                        error('Caractere de controle inválido dentro do registro.', path, scene, row_id, key)
                    if '::' in value:
                        error('Sequência "::" não permitida (separador de colunas do .epk_dec).', path, scene, row_id, key)
                    if not value.strip() and result.original['PT-BR'][offset].strip():
                        error('Tradução PT-BR vazia.', path, scene, row_id, key)
                    bracket_err = check_brackets(value)
                    if bracket_err:
                        error(bracket_err, path, scene, row_id, key, severity='aviso')

        for row_id in sorted(expected - file_seen):
            error('Linha ausente; restaure este ID.', path, scene, row_id, 'id')

    for path in work.glob('[0-9]*/*.json'):
        if path.resolve() not in expected_paths:
            error('JSON não catalogado; será ignorado na exportação.', path)

    if not result.errors and (set(seen) != set(range(1, count + 1)) or any(v is None for a in result.values.values() for v in a)):
        error('Há posições não cobertas pelo manifesto.', work / 'manifesto.json')

    return result


def require_valid(work: Path) -> Inspection:
    result = inspect_project(work)
    if result.errors:
        issue = result.errors[0]
        raise ValueError(f'{len(result.errors)} erro(s). {issue.file}; ID {issue.row_id}: {issue.message}')
    return result


def atomic_write(path: Path, raw: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(dir=path.parent, prefix='.' + path.name, suffix='.tmp', delete=False) as f:
            temporary = Path(f.name)
            f.write(raw)
            f.flush()
            os.fsync(f.fileno())
        os.replace(temporary, path)
    finally:
        if temporary is not None and temporary.exists():
            temporary.unlink()


def backup_file(work: Path, path: Path, category: str) -> Path | None:
    if not path.exists():
        return None
    raw = path.read_bytes()
    target = work / 'backups' / category / (scripts.sha(raw)[:20] + '_' + path.name)
    if not target.exists():
        atomic_write(target, raw)
    return target


def save_scene(work: Path, path: Path, data: dict, expected_hash: str | None = None) -> str:
    if path.exists() and expected_hash and scripts.sha(path.read_bytes()) != expected_hash:
        raise ValueError('Arquivo alterado fora do painel. Recarregue a cena antes de salvar.')
    raw = (json.dumps(data, ensure_ascii=False, indent=2) + '\n').encode('utf-8')
    if path.exists() and path.read_bytes() == raw:
        return scripts.sha(raw)
    backup_file(work, path, 'json')
    atomic_write(path, raw)
    return scripts.sha(raw)


def export_epk_dec(work: Path, output_dir: Path, inspection: Inspection | None = None) -> dict:
    work = work.resolve()
    output_dir = output_dir.resolve()
    result = inspection or require_valid(work)
    if result.errors:
        raise ValueError('A exportação está bloqueada por erros de validação.')
    if output_dir.is_relative_to(work / 'originais'):
        raise ValueError('A pasta de saída deve ficar fora de originais/.')
    for file_str, fingerprint in result.fingerprints.items():
        if scripts.sha(Path(file_str).read_bytes()) != fingerprint:
            raise ValueError(f'Cena mudou durante a validação: {file_str}. Valide novamente.')

    output_dir.mkdir(parents=True, exist_ok=True)
    exported = 0
    for scene, meta in result.manifest['scenes'].items():
        epk_info = result.epk_meta[scene]
        text_col = epk_info['text_col']
        lines = [epk_info['magic'], epk_info['schema']]
        for offset, rec in zip(meta['offsets'], epk_info['records']):
            rest = list(rec['rest'])
            pt_val = result.values['PT-BR'][offset]
            if text_col < len(rest):
                rest[text_col] = pt_val
            lines.append(f"{rec['epk_id']}::{rec['label']}::{'::'.join(rest)}::")
        raw = ('\n'.join(lines) + '\n').encode('utf-8')
        target = output_dir / meta['filename']
        atomic_write(target, raw)
        exported += 1

    report = {
        'pasta_saida': str(output_dir),
        'arquivos': exported,
        'linhas': result.manifest['line_count'],
    }
    scripts.write_json(output_dir / 'validacao.json', report)
    return report


def find_mod_epk_dir() -> Path:
    """Procura a pasta de mod typemoon/hollow/.../epk no PC; se não existir, aponta para o AppData Local do usuário atual."""
    local_app = Path(os.environ.get('LOCALAPPDATA') or (Path.home() / 'AppData' / 'Local'))
    preferred = local_app / 'typemoon' / 'hollow' / 'data' / 'root' / 'data' / 'locale' / 'us' / 'epk'
    if preferred.exists():
        return preferred
    users_dir = Path('C:/Users')
    if users_dir.exists():
        for user_dir in users_dir.iterdir():
            candidate = user_dir / 'AppData' / 'Local' / 'typemoon' / 'hollow' / 'data' / 'root' / 'data' / 'locale' / 'us' / 'epk'
            if candidate.exists():
                return candidate
    return preferred


def _find_epk_compiler() -> tuple[Path, Path]:
    candidates = [
        (scripts.MAIN_DIR / 'main.exe', scripts.MAIN_DIR / 'SomeKey.bin'),
        (scripts.ROOT / 'Ferramentas' / 'EpkRecompiladorEdit' / 'main.exe', scripts.ROOT / 'Ferramentas' / 'EpkRecompiladorEdit' / 'SomeKey.bin'),
    ]
    for exe, key in candidates:
        if exe.exists() and key.exists():
            return exe, key
    raise FileNotFoundError('main.exe e SomeKey.bin não encontrados para compilar .epk.')


def compile_and_install_epk(
    work: Path,
    mod_epk_dir: Path | None = None,
    dec_dir: Path | None = None,
    inspection: Inspection | None = None,
) -> dict:
    """Valida, gera os .epk_dec, compila para .epk com main.exe e instala na pasta do mod."""
    work = work.resolve()
    target_dir = (mod_epk_dir or find_mod_epk_dir()).resolve()
    dec_out = (dec_dir or scripts.DEFAULT_OUTPUT).resolve()
    result = inspection or require_valid(work)
    if result.errors:
        raise ValueError('A geração está bloqueada por erros de validação.')

    export_report = export_epk_dec(work, dec_out, inspection=result)
    main_exe, some_key = _find_epk_compiler()

    target_dir.mkdir(parents=True, exist_ok=True)
    dec_files = [dec_out / meta['filename'] for meta in result.manifest['scenes'].values()]

    with tempfile.TemporaryDirectory(prefix='fha_epk_') as tmp:
        tmp_dir = Path(tmp)
        shutil.copy2(main_exe, tmp_dir / 'main.exe')
        shutil.copy2(some_key, tmp_dir / 'SomeKey.bin')

        def encode_one(src_dec: Path) -> Path:
            local_dec = tmp_dir / src_dec.name
            shutil.copy2(src_dec, local_dec)
            proc = subprocess.run(
                [str(tmp_dir / 'main.exe'), 'enc', str(local_dec)],
                cwd=str(tmp_dir),
                capture_output=True,
                text=True,
                creationflags=getattr(subprocess, 'CREATE_NO_WINDOW', 0),
            )
            enc_path = tmp_dir / f'{src_dec.stem}.epk_enc'
            if proc.returncode != 0 or not enc_path.exists():
                raise RuntimeError(f'Falha ao compilar {src_dec.name}: {proc.stderr or proc.stdout}')
            return enc_path

        workers = min(8, os.cpu_count() or 4)
        with ThreadPoolExecutor(max_workers=workers) as pool:
            enc_paths = list(pool.map(encode_one, dec_files))

        for enc_path in enc_paths:
            dest = target_dir / f'{enc_path.stem}.epk'
            atomic_write(dest, enc_path.read_bytes())

    report = {
        'pasta_mod': str(target_dir),
        'pasta_dec': str(dec_out),
        'arquivos_epk': len(dec_files),
        'linhas': export_report['linhas'],
    }
    scripts.write_json(dec_out / 'instalacao_epk.json', report)
    return report


def restore_record(work: Path, scene: str, row_id: int) -> dict:
    manifest = scripts.read_json(work / 'manifesto.json')
    meta = manifest['scenes'][scene]
    if row_id - 1 not in meta['offsets']:
        raise ValueError('O ID não pertence a esta cena.')
    refs_meta = manifest['sources']['referencias']
    refs_path = work / 'originais' / refs_meta['filename']
    raw = refs_path.read_bytes()
    if scripts.sha(raw) != refs_meta['sha256']:
        raise ValueError('Backup original (referencias.json) alterado.')
    refs_data = json.loads(raw.decode('utf-8-sig'))
    epk_meta = scripts.read_json(work / 'originais' / manifest['sources']['epk_meta']['filename'])
    idx = row_id - 1
    local_idx = meta['offsets'].index(idx)
    rec_meta = epk_meta[scene]['records'][local_idx]
    return {
        'en': refs_data['en'][idx],
        'jp': refs_data['jp'][idx],
        'Pt-br': refs_data['pt_inicial'][idx],
        'id': row_id,
        'epk_id': rec_meta['epk_id'],
        'label': rec_meta['label'],
    }


def save_log(work: Path, inspection: Inspection, generated: dict | None = None) -> Path:
    now = datetime.now(timezone.utc)
    path = work / 'logs' / (now.strftime('%Y%m%dT%H%M%S%fZ') + '.json')
    scripts.write_json(path, {
        'data_utc': now.isoformat(),
        'erros': [asdict(i) for i in inspection.issues],
        'gerado': generated,
        'linhas': inspection.manifest.get('line_count'),
    })
    return path
