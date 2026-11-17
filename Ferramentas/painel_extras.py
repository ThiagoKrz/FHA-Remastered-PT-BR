"""Recursos extras de equipe para o painel: busca global e conferência de glossário."""
from __future__ import annotations

import json
from pathlib import Path
import re
import tkinter as tk
from tkinter import ttk


def load_glossary_terms(glossary_path: Path, extra_sections: tuple[str, ...] = ()) -> list[tuple[str, str]]:
    if not glossary_path.exists():
        return []
    data = json.loads(glossary_path.read_text(encoding='utf-8-sig'))
    terms: dict[str, str] = {}
    for section in ('glossario_geral_type_moon', *extra_sections):
        block = data.get(section)
        if isinstance(block, dict):
            for en_term, pt_term in block.items():
                if isinstance(en_term, str) and isinstance(pt_term, str) and len(en_term.strip()) >= 3 and pt_term.strip():
                    terms[en_term.strip()] = pt_term.strip()
    return sorted(terms.items(), key=lambda x: -len(x[0]))


def check_scene_glossary(
    data: dict,
    scene: str,
    path: Path,
    terms: list[tuple[str, str]],
    issue_cls,
) -> list:
    issues = []
    if not isinstance(data, dict) or not isinstance(data.get('linhas'), list):
        return issues
    compiled = [
        (en_t, pt_t, re.compile(r'\b' + re.escape(en_t) + r'\b', re.IGNORECASE))
        for en_t, pt_t in terms
    ]
    for rec in data['linhas']:
        if not isinstance(rec, dict):
            continue
        en_val = str(rec.get('en', ''))
        pt_val = str(rec.get('Pt-br', ''))
        if not en_val or not pt_val.strip():
            continue
        pt_fold = pt_val.casefold()
        for en_t, pt_t, rx in compiled:
            if rx.search(en_val):
                # Aceita qualquer variante separada por "/" no glossário
                options = [opt.strip().casefold() for opt in pt_t.split('/') if opt.strip()]
                if options and not any(opt in pt_fold for opt in options):
                    issues.append(issue_cls(
                        f'Glossário: "{en_t}" -> esperado "{pt_t}"',
                        str(path),
                        scene,
                        rec.get('id'),
                        'Pt-br',
                        severity='aviso',
                    ))
    return issues


def open_global_search(panel, tree_scrollbars_fn) -> None:
    win = tk.Toplevel(panel.root)
    win.title('Busca global no projeto')
    win.geometry('920x560')
    p = getattr(panel, 'palette', {})
    if p:
        win.configure(background=p['bg'])

    top = ttk.Frame(win, padding=10)
    top.pack(fill='x')
    ttk.Label(top, text='Buscar em todas as cenas (PT-BR, EN, JP ou ID):', style='Muted.TLabel').pack(side='left')
    query_var = tk.StringVar()
    entry = ttk.Entry(top, textvariable=query_var)
    entry.pack(side='left', fill='x', expand=True, padx=8)

    body = ttk.Frame(win, padding=(10, 0, 10, 10))
    body.pack(fill='both', expand=True)
    tree = ttk.Treeview(body, columns=('scene', 'id', 'text'), show='headings', selectmode='browse')
    tree.heading('scene', text='Cena')
    tree.heading('id', text='ID')
    tree.heading('text', text='Trecho encontrado')
    tree.column('scene', width=220, stretch=False)
    tree.column('id', width=80, stretch=False)
    tree.column('text', width=580)
    tree_scrollbars_fn(body, tree)

    status_var = tk.StringVar(value='Digite um termo e pressione Enter.')
    ttk.Label(win, textvariable=status_var, style='Muted.TLabel', padding=(10, 0, 10, 8)).pack(anchor='w')

    hits: dict[str, tuple[str, int | None]] = {}

    def run_search(_=None):
        q = query_var.get().strip().casefold()
        tree.delete(*tree.get_children())
        hits.clear()
        if len(q) < 2:
            status_var.set('Digite pelo menos 2 caracteres.')
            return
        count = 0
        limit = 400
        for scene, meta in panel.manifest['scenes'].items():
            if not meta.get('offsets'):
                continue
            scene_path = panel.work / meta['path']
            if not scene_path.exists():
                continue
            try:
                scene_data = json.loads(scene_path.read_text(encoding='utf-8-sig'))
            except Exception:
                continue
            title = meta.get('title', scene)
            for rec in scene_data.get('linhas', []):
                if not isinstance(rec, dict):
                    continue
                haystack = ' '.join(str(rec.get(k, '')) for k in ('id', 'Pt-br', 'en', 'jp')).casefold()
                if q in haystack:
                    preview = (rec.get('Pt-br') or rec.get('en') or rec.get('jp') or '').replace('\n', ' ↵ ')
                    iid = tree.insert('', 'end', values=(f'{title}' if title == scene else f'{title} [{scene}]', rec.get('id', ''), preview))
                    hits[iid] = (scene, rec.get('id'))
                    count += 1
                    if count >= limit:
                        break
            if count >= limit:
                break
        status_var.set(f'{count} resultado(s)' + (' (limite de 400 atingido)' if count >= limit else '') + '. Duplo clique para abrir.')

    def jump(_=None):
        sel = tree.selection()
        if not sel:
            return
        scene, row_id = hits[sel[0]]
        if panel.open_scene(scene, row_id):
            panel.pt.focus_set()
            win.destroy()

    ttk.Button(top, text='Buscar', command=run_search, style='Primary.TButton').pack(side='left')
    entry.bind('<Return>', run_search)
    tree.bind('<Double-1>', jump)
    tree.bind('<Return>', jump)
    entry.focus_set()
