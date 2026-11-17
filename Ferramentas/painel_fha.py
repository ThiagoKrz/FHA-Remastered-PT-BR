"""Painel local para revisar os JSONs de Fate/hollow ataraxia e exportar os .epk_dec."""
from pathlib import Path
import json
import os
import queue
import threading
import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

import scripts_fha as scripts
import projeto_json_fha as project
import painel_extras as extras


class ReviewPanel(ttk.Frame):
    def __init__(self, root, work=scripts.WORK):
        super().__init__(root, padding=12)
        self.root = root
        self.work = Path(work).resolve()
        self.manifest = scripts.read_json(self.work / 'manifesto.json')
        self.data = None
        self.current_scene = None
        self.path = None
        self.fingerprint = None
        self.current_index = None
        self.dirty = False
        self.raw_dirty = False
        self.rendering = False
        self.busy = False
        self.messages = queue.Queue()
        self.issue_map = {}
        self.scene_nodes = {}
        self.autosave_job = None
        try:
            self.theme = scripts.read_json(self.work / '.preferencias.json').get('tema', 'escuro')
        except (OSError, ValueError):
            self.theme = 'escuro'
        if self.theme not in ('claro', 'escuro'):
            self.theme = 'escuro'
        self.pack(fill='both', expand=True)
        self._build()
        self.apply_theme()
        self.root.title('Fate/hollow ataraxia — revisão de scripts')
        self.root.geometry('1440x960')
        self.root.minsize(1060, 760)
        self.root.protocol('WM_DELETE_WINDOW', self.close)
        self.root.bind('<Control-s>', lambda _: self.save_current())
        self.root.bind('<F5>', lambda _: self.run_validation())
        self.root.bind('<Control-Return>', lambda _: self.run_validation(True))
        self.root.bind('<Control-Shift-F>', lambda _: self.open_global_search())
        self.root.after(80, self.poll)
        first = next(iter(self.scene_nodes), None)
        if first:
            self.open_scene(first)
            self.scene_tree.selection_set(self.scene_nodes[first])
        self.root.after(400, self.run_validation)

    def _build(self):
        self.style = ttk.Style(self.root)
        self.style.theme_use('clam')

        header = ttk.Frame(self)
        header.pack(fill='x', pady=(2, 14))
        heading = ttk.Frame(header)
        heading.pack(side='left')
        ttk.Label(heading, text='Fate/hollow ataraxia', style='Title.TLabel').pack(anchor='w')
        count = self.manifest['line_count']
        scenes = len(self.manifest['scenes'])
        ttk.Label(
            heading,
            text=f'Revisão de tradução  •  {count:,} linhas em {scenes} arquivos'.replace(',', '.'),
            style='Muted.TLabel',
        ).pack(anchor='w', pady=(2, 0))

        self.theme_button = ttk.Button(header, command=self.toggle_theme)
        self.theme_button.pack(side='right', anchor='n', pady=7)
        self.validation_state = tk.StringVar(value='Aguardando validação')
        self.validation_label = ttk.Label(header, textvariable=self.validation_state, style='Muted.TLabel')
        self.validation_label.pack(side='right', padx=18, pady=13, anchor='n')

        actions = ttk.Frame(self)
        actions.pack(fill='x', pady=(0, 10))
        self.save_button = ttk.Button(actions, text='Salvar cena  Ctrl+S', command=self.save_current)
        self.save_button.pack(side='left')
        self.validate_button = ttk.Button(actions, text='Validar projeto  F5', command=self.run_validation)
        self.validate_button.pack(side='left', padx=8)
        ttk.Button(actions, text='Recarregar cena', command=self.reload_scene).pack(side='left')
        ttk.Button(actions, text='Busca global', command=self.open_global_search).pack(side='left', padx=(8, 0))
        ttk.Button(actions, text='Conferir glossário', command=self.check_glossary).pack(side='left', padx=(8, 0))
        self.generate_button = ttk.Button(
            actions,
            text='Gerar e instalar .epk',
            command=lambda: self.run_validation(True),
            style='Primary.TButton',
        )
        self.generate_button.pack(side='right')

        output_frame = ttk.Frame(self)
        output_frame.pack(fill='x', pady=(0, 14))
        ttk.Label(output_frame, text='Pasta do mod (.epk)', style='Muted.TLabel').pack(side='left')
        self.output = tk.StringVar(value=str(project.find_mod_epk_dir()))
        ttk.Entry(output_frame, textvariable=self.output).pack(side='left', fill='x', expand=True, padx=(8, 0))

        workspace = ttk.Panedwindow(self, orient='vertical')
        workspace.pack(fill='both', expand=True)
        main = ttk.Panedwindow(workspace, orient='horizontal')
        workspace.add(main, weight=5)
        left = ttk.Frame(main, padding=(10, 10), style='Surface.TFrame')
        right = ttk.Frame(main, padding=(12, 0, 0, 0))
        main.add(left, weight=1)
        main.add(right, weight=5)

        ttk.Label(left, text='Rotas e cenas', style='Section.TLabel').pack(anchor='w', pady=(0, 6))
        self.scene_filter = tk.StringVar()
        ttk.Entry(left, textvariable=self.scene_filter).pack(fill='x', pady=(0, 8))
        self.scene_filter.trace_add('write', lambda *_: self.populate_scene_tree())
        scene_frame = ttk.Frame(left)
        scene_frame.pack(fill='both', expand=True)
        self.scene_tree = ttk.Treeview(scene_frame, show='tree', selectmode='browse')
        self.scene_tree.column('#0', width=320, minwidth=220)
        self.tree_scrollbars(scene_frame, self.scene_tree)
        self.populate_scene_tree()
        self.scene_tree.bind('<<TreeviewSelect>>', self.on_scene_select)

        self.notebook = ttk.Notebook(right)
        self.notebook.pack(fill='both', expand=True)
        editor = ttk.Frame(self.notebook, padding=12, style='Surface.TFrame')
        raw_frame = ttk.Frame(self.notebook, padding=12, style='Surface.TFrame')
        self.notebook.add(editor, text='Revisão')
        self.notebook.add(raw_frame, text='JSON da cena')

        searchbar = ttk.Frame(editor)
        searchbar.pack(fill='x')
        ttk.Label(searchbar, text='Buscar nesta cena', style='Muted.TLabel').pack(side='left')
        self.search = tk.StringVar()
        ttk.Entry(searchbar, textvariable=self.search).pack(side='left', fill='x', expand=True, padx=(10, 0))
        self.search.trace_add('write', lambda *_: self.fill_rows())

        rows_frame = ttk.Frame(editor)
        rows_frame.pack(fill='x', pady=(10, 12))
        self.rows_tree = ttk.Treeview(rows_frame, columns=('id', 'pt'), show='headings', height=6, selectmode='browse')
        self.rows_tree.heading('id', text='ID global')
        self.rows_tree.heading('pt', text='PT-BR')
        self.rows_tree.column('id', width=95, stretch=False)
        self.rows_tree.column('pt', width=600)
        self.tree_scrollbars(rows_frame, self.rows_tree)
        self.rows_tree.bind('<<TreeviewSelect>>', self.on_row_select)

        self.line_label = ttk.Label(editor, text='', style='Section.TLabel')
        self.line_label.pack(anchor='w', pady=(0, 7))
        references = ttk.Frame(editor)
        references.pack(fill='x', pady=(0, 8))
        jp_frame = ttk.Frame(references)
        jp_frame.pack(side='left', fill='both', expand=True, padx=(0, 6))
        en_frame = ttk.Frame(references)
        en_frame.pack(side='left', fill='both', expand=True, padx=(6, 0))
        self.jp = self.make_text(jp_frame, 'Japonês · referência', 3, False, ('Yu Gothic UI', 11))
        self.en = self.make_text(en_frame, 'Inglês · referência', 3, False)
        self.pt = self.make_text(editor, 'Português brasileiro', 4, True)
        self.pt.bind('<<Modified>>', self.on_pt_modified)
        ttk.Label(
            editor,
            text='Salvamento automático após uma pausa. Ctrl+S também salva. Preserve as tags [wait...], [l], [lr] e evite "::".',
            style='Muted.TLabel',
        ).pack(anchor='w', pady=(7, 0))

        raw_actions = ttk.Frame(raw_frame)
        raw_actions.pack(fill='x', pady=(0, 6))
        ttk.Button(raw_actions, text='Aplicar JSON ao editor', command=self.apply_raw).pack(side='left')
        ttk.Button(raw_actions, text='Atualizar JSON com o editor', command=self.sync_raw).pack(side='left', padx=8)
        ttk.Label(raw_actions, text='Corrija campos, IDs e sintaxe.', style='Muted.TLabel').pack(side='left')
        self.raw = ScrolledText(raw_frame, wrap='none', undo=True, font=('Consolas', 11))
        self.raw.pack(fill='both', expand=True)
        self.raw.bind('<<Modified>>', self.on_raw_modified)
        self.notebook.bind('<<NotebookTabChanged>>', self.on_tab_changed)

        bottom = ttk.Frame(workspace, padding=(10, 9), style='Surface.TFrame')
        workspace.add(bottom, weight=1)
        log_header = ttk.Frame(bottom)
        log_header.pack(fill='x', pady=(0, 7))
        ttk.Label(log_header, text='Validação e erros', style='Section.TLabel').pack(side='left')
        ttk.Label(log_header, text='Duplo clique para ir até o trecho', style='Muted.TLabel').pack(side='right')
        issues_frame = ttk.Frame(bottom)
        issues_frame.pack(fill='both', expand=True)
        self.issues = ttk.Treeview(issues_frame, columns=('id', 'scene', 'field', 'message'), show='headings', height=3)
        for key, title, width in [('id', 'ID / JSON', 95), ('scene', 'Cena', 180), ('field', 'Campo', 80), ('message', 'Mensagem', 700)]:
            self.issues.heading(key, text=title)
            self.issues.column(key, width=width, stretch=key == 'message')
        self.tree_scrollbars(issues_frame, self.issues)
        self.issues.bind('<Double-1>', self.jump_issue)

        log_actions = ttk.Frame(bottom)
        log_actions.pack(fill='x', pady=(5, 0))
        ttk.Button(log_actions, text='Ir para o erro', command=self.jump_issue).pack(side='left')
        ttk.Button(log_actions, text='Restaurar linha / referência', command=self.restore_selected).pack(side='left', padx=8)
        ttk.Button(log_actions, text='Pasta de logs', command=self.open_logs).pack(side='right')

        footer = ttk.Frame(self)
        footer.pack(fill='x', pady=(9, 0))
        self.status = tk.StringVar(value='Carregando projeto…')
        status_label = ttk.Label(footer, textvariable=self.status, anchor='w', style='Muted.TLabel', wraplength=1000)
        status_label.pack(side='left', fill='x', expand=True)
        footer.bind('<Configure>', lambda event: status_label.configure(wraplength=max(350, event.width - 150)))
        self.progress = ttk.Progressbar(footer, mode='indeterminate', length=120)
        self.progress.pack(side='right', padx=(12, 0))
        self.root.after_idle(lambda: main.sashpos(0, 275))

    def populate_scene_tree(self):
        query = self.scene_filter.get().strip().casefold() if hasattr(self, 'scene_filter') else ''
        self.scene_tree.delete(*self.scene_tree.get_children())
        self.scene_nodes.clear()
        groups = {}
        for scene, meta in sorted(self.manifest['scenes'].items(), key=lambda x: (x[1]['group'], x[1].get('order', 99999), x[0])):
            if not meta.get('offsets'):
                continue
            group = meta['group']
            title = meta.get('title', scene)
            group_label = self.group_title(group)
            if query and query not in title.casefold() and query not in scene.casefold() and query not in group_label.casefold():
                continue
            if group not in groups:
                groups[group] = self.scene_tree.insert('', 'end', text=group_label, open=bool(query) or group.startswith('00'))
            node = self.scene_tree.insert(
                groups[group],
                'end',
                text=f'{title}  [{scene}]  ({len(meta["offsets"])})',
                values=(scene,),
            )
            self.scene_nodes[scene] = node

    def open_global_search(self):
        extras.open_global_search(self, self.tree_scrollbars)

    def check_glossary(self):
        if self.busy or not self.current_scene or self.data is None:
            return
        glossary_path = scripts.ROOT / 'Guias' / 'GLOSSARIO_TYPEMOON_OPERACIONAL.json'
        terms = extras.load_glossary_terms(glossary_path)
        if not terms:
            self.log('Glossário não encontrado em Guias/GLOSSARIO_TYPEMOON_OPERACIONAL.json.')
            return
        self.issues.delete(*self.issues.get_children())
        self.issue_map.clear()
        found = extras.check_scene_glossary(self.data, self.current_scene, self.path, terms, project.Issue)
        for issue in found:
            self.log(issue.message, issue)
        if not found:
            self.log(f'Glossário OK em {self.current_scene}: nenhum desvio encontrado.', ok=True)
        self.status.set(f'Glossário conferido em {self.current_scene}: {len(found)} aviso(s).')

    @staticmethod
    def group_title(group: str) -> str:
        if group in scripts.GROUP_TO_ROTA:
            return scripts.GROUP_TO_ROTA[group]
        return group.replace('_', ' ').capitalize()

    def toggle_theme(self):
        self.theme = 'claro' if self.theme == 'escuro' else 'escuro'
        self.apply_theme()
        try:
            project.atomic_write(self.work / '.preferencias.json', (json.dumps({'tema': self.theme}) + '\n').encode('utf-8'))
        except OSError as exc:
            self.status.set(f'Tema aplicado, mas não foi possível salvar a preferência: {exc}')

    def apply_theme(self):
        dark = self.theme == 'escuro'
        p = ({'bg': '#171d2a', 'surface': '#20293a', 'field': '#273247', 'readonly': '#1d2636',
              'text': '#e6edf8', 'muted': '#acb8cd', 'border': '#3b4860', 'accent': '#b5c5ff',
              'button': '#546db5', 'hover': '#647ec8', 'selected': '#3d527b', 'error': '#ffacb1', 'ok': '#98d5ba'}
             if dark else
             {'bg': '#edf1f7', 'surface': '#ffffff', 'field': '#ffffff', 'readonly': '#f1f4f9',
              'text': '#25324a', 'muted': '#5e6d83', 'border': '#cbd4e3', 'accent': '#405ba0',
              'button': '#405da2', 'hover': '#344e8d', 'selected': '#dce5fa', 'error': '#af303e', 'ok': '#27694e'})
        self.palette = p
        style = self.style
        self.root.configure(background=p['bg'])
        style.configure('.', font=('Segoe UI', 10), background=p['bg'], foreground=p['text'],
                        bordercolor=p['border'], lightcolor=p['border'], darkcolor=p['border'],
                        troughcolor=p['bg'], focuscolor=p['accent'])
        style.configure('TFrame', background=p['bg'])
        style.configure('Surface.TFrame', background=p['surface'])
        style.configure('TLabel', background=p['surface'], foreground=p['text'])
        style.configure('Muted.TLabel', foreground=p['muted'], background=p['bg'])
        style.configure('Section.TLabel', font=('Segoe UI', 10, 'bold'), foreground=p['accent'], background=p['surface'])
        style.configure('Title.TLabel', font=('Segoe UI', 25, 'bold'), foreground=p['text'], background=p['bg'])
        style.configure('Error.TLabel', background=p['bg'], foreground=p['error'])
        style.configure('Success.TLabel', background=p['bg'], foreground=p['ok'])
        style.configure('TButton', padding=(12, 7), background=p['surface'], foreground=p['text'], borderwidth=1)
        style.map('TButton', background=[('active', p['field']), ('pressed', p['selected'])], foreground=[('disabled', p['muted'])])
        style.configure('Primary.TButton', background=p['button'], foreground='#ffffff', font=('Segoe UI', 10, 'bold'))
        style.map('Primary.TButton', background=[('disabled', p['border']), ('active', p['hover']), ('pressed', p['button'])], foreground=[('disabled', p['muted']), ('!disabled', '#ffffff')])
        style.configure('TEntry', fieldbackground=p['field'], foreground=p['text'], padding=6, insertcolor=p['text'])
        style.map('TEntry', selectbackground=[('!disabled', p['selected'])], selectforeground=[('!disabled', p['text'])])
        style.configure('Treeview', background=p['surface'], fieldbackground=p['surface'], foreground=p['text'],
                        rowheight=28, font=('Segoe UI', 10), borderwidth=0)
        style.map('Treeview', background=[('selected', p['selected'])], foreground=[('selected', p['text'])])
        style.configure('Treeview.Heading', background=p['field'], foreground=p['muted'], font=('Segoe UI', 9, 'bold'), padding=(8, 6), relief='flat')
        style.map('Treeview.Heading', background=[('active', p['selected'])])
        style.configure('TNotebook', background=p['bg'], borderwidth=0, tabmargins=(0, 0, 0, 0))
        style.configure('TNotebook.Tab', background=p['bg'], foreground=p['muted'], padding=(19, 10))
        style.map('TNotebook.Tab', background=[('selected', p['surface']), ('active', p['field'])], foreground=[('selected', p['text'])])
        style.configure('TPanedwindow', background=p['bg'])
        style.configure('Sash', sashthickness=7, background=p['bg'])
        style.configure('TScrollbar', background=p['border'], arrowcolor=p['muted'], troughcolor=p['surface'], borderwidth=0)
        style.map('TScrollbar', background=[('active', p['selected'])])
        style.configure('TProgressbar', background=p['button'], troughcolor=p['bg'], borderwidth=0)
        for widget in (self.jp, self.en, self.pt, self.raw):
            readonly = widget in (self.jp, self.en)
            widget.configure(background=p['readonly'] if readonly else p['field'], foreground=p['text'],
                             insertbackground=p['text'], selectbackground=p['selected'], selectforeground=p['text'],
                             relief='flat', borderwidth=0, highlightthickness=1,
                             highlightbackground=p['border'], highlightcolor=p['accent'])
            widget.frame.configure(background=p['surface'])
            widget.vbar.configure(background=p['border'], activebackground=p['selected'], troughcolor=p['surface'], borderwidth=0, highlightthickness=0)
        self.issues.tag_configure('erro', foreground=p['error'])
        self.issues.tag_configure('ok', foreground=p['ok'])
        self.issues.tag_configure('aviso', foreground='#edc784' if dark else '#845400')
        self.theme_button.configure(text='Modo claro' if dark else 'Modo noturno')
        if os.name == 'nt':
            self.root.after_idle(self.theme_titlebar)

    def theme_titlebar(self):
        try:
            import ctypes
            user32 = ctypes.windll.user32
            user32.GetParent.restype = ctypes.c_void_p
            user32.GetParent.argtypes = [ctypes.c_void_p]
            handle = user32.GetParent(self.root.winfo_id())
            value = ctypes.c_int(self.theme == 'escuro')
            ctypes.windll.dwmapi.DwmSetWindowAttribute(ctypes.c_void_p(handle), 20, ctypes.byref(value), 4)
        except (AttributeError, OSError):
            pass

    @staticmethod
    def tree_scrollbars(parent, tree):
        vertical = ttk.Scrollbar(parent, orient='vertical', command=tree.yview)
        horizontal = ttk.Scrollbar(parent, orient='horizontal', command=tree.xview)
        tree.configure(yscrollcommand=vertical.set, xscrollcommand=horizontal.set)
        tree.grid(row=0, column=0, sticky='nsew')
        vertical.grid(row=0, column=1, sticky='ns')
        horizontal.grid(row=1, column=0, sticky='ew')
        parent.rowconfigure(0, weight=1)
        parent.columnconfigure(0, weight=1)

    def make_text(self, parent, title, height, editable, font=('Segoe UI', 11)):
        ttk.Label(parent, text=title, style='Section.TLabel' if editable else 'Muted.TLabel').pack(anchor='w', pady=(3, 5))
        widget = ScrolledText(parent, width=30, height=height, wrap='word', undo=editable, font=font, padx=12, pady=9, spacing1=2, spacing3=3)
        widget.pack(fill='both', expand=editable)
        if not editable:
            widget.configure(state='disabled', background='#edf1f5')
        return widget

    def set_text(self, widget, text, readonly=False):
        widget.configure(state='normal')
        widget.delete('1.0', 'end')
        widget.insert('1.0', text)
        widget.edit_modified(False)
        if readonly:
            widget.configure(state='disabled')

    def log(self, message, issue=None, ok=False):
        node = self.issues.insert(
            '',
            'end',
            values=(issue.row_id or issue.json_line or '' if issue else '', issue.scene if issue else '', issue.field if issue else '', message),
            tags=('ok' if ok else issue.severity if issue else '',),
        )
        if issue:
            self.issue_map[node] = issue
        self.issues.see(node)

    def on_scene_select(self, _=None):
        selection = self.scene_tree.selection()
        if selection:
            values = self.scene_tree.item(selection[0], 'values')
            if values and values[0] != self.current_scene:
                self.open_scene(values[0])

    def open_scene(self, scene, row_id=None):
        if self.busy:
            return False
        if not self.save_current():
            return False
        self.current_scene = scene
        self.path = self.work / self.manifest['scenes'][scene]['path']
        self.current_index = None
        self.dirty = self.raw_dirty = False
        self.rendering = True
        try:
            raw = self.path.read_bytes()
            self.fingerprint = scripts.sha(raw)
            text = raw.decode('utf-8-sig')
            self.set_text(self.raw, text)
            self.data = project.parse_json(text)
            self.notebook.select(0)
        except Exception as exc:
            self.data = None
            self.fingerprint = scripts.sha(self.path.read_bytes()) if self.path.exists() else None
            self.set_text(self.raw, self.path.read_text(encoding='utf-8-sig', errors='replace') if self.path.exists() else '')
            self.notebook.select(1)
            self.log(f'{scene}: {exc}')
        self.rendering = False
        self.search.set('')
        self.fill_rows(row_id)
        self.status.set(f'{scene} — {self.path}')
        if scene in self.scene_nodes:
            self.scene_tree.selection_set(self.scene_nodes[scene])
            self.scene_tree.see(self.scene_nodes[scene])
        return True

    def fill_rows(self, row_id=None):
        self.rows_tree.delete(*self.rows_tree.get_children())
        if not isinstance(self.data, dict) or not isinstance(self.data.get('linhas'), list):
            return
        query = self.search.get().casefold()
        for index, record in enumerate(self.data['linhas']):
            if not isinstance(record, dict):
                continue
            if query and query not in ' '.join(str(record.get(k, '')) for k in ['id', 'epk_id', 'label', 'jp', 'en', 'Pt-br']).casefold():
                continue
            self.rows_tree.insert('', 'end', iid=str(index), values=(record.get('id', '?'), str(record.get('Pt-br', '[campo ausente]')).replace('\n', ' ↵ ')))
        target = next((str(i) for i, r in enumerate(self.data['linhas']) if isinstance(r, dict) and r.get('id') == row_id), None)
        children = self.rows_tree.get_children()
        if target in children:
            self.rows_tree.selection_set(target)
            self.rows_tree.see(target)
            self.select_record(int(target))
        elif children:
            self.rows_tree.selection_set(children[0])
            self.select_record(int(children[0]))

    def on_row_select(self, _=None):
        selection = self.rows_tree.selection()
        if selection:
            self.select_record(int(selection[0]))

    def select_record(self, index):
        if self.data is None:
            return
        record = self.data['linhas'][index]
        self.current_index = index
        self.rendering = True
        self.set_text(self.jp, str(record.get('jp', '')), True)
        self.set_text(self.en, str(record.get('en', '')), True)
        self.set_text(self.pt, str(record.get('Pt-br', '')))
        title = self.manifest['scenes'].get(self.current_scene, {}).get('title', self.current_scene)
        self.line_label.configure(
            text=f"{title} [{self.current_scene}] — ID {record.get('id', '?')} (epk {record.get('epk_id', '?')}) — registro {index + 1}/{len(self.data['linhas'])}"
        )
        self.rendering = False

    def on_pt_modified(self, _=None):
        if not self.pt.edit_modified():
            return
        self.pt.edit_modified(False)
        if self.rendering or self.current_index is None or self.busy:
            return
        new_val = self.pt.get('1.0', 'end-1c')
        self.data['linhas'][self.current_index]['Pt-br'] = new_val
        self.dirty = True
        node = str(self.current_index)
        if self.rows_tree.exists(node):
            self.rows_tree.set(node, 'pt', new_val.replace('\n', ' ↵ '))
        self.status.set(f'{self.current_scene}: alterações ainda não salvas')
        self.validation_state.set('Alterações pendentes')
        self.validation_label.configure(style='Muted.TLabel')
        self.schedule_autosave()

    def on_raw_modified(self, _=None):
        if self.raw.edit_modified():
            self.raw.edit_modified(False)
            if not self.rendering:
                self.raw_dirty = True
                self.schedule_autosave()

    def schedule_autosave(self):
        self.cancel_autosave()
        if not self.busy:
            self.autosave_job = self.root.after(1500, self.autosave_current)

    def cancel_autosave(self):
        if self.autosave_job is not None:
            self.root.after_cancel(self.autosave_job)
            self.autosave_job = None

    def autosave_current(self):
        self.autosave_job = None
        if self.busy or not (self.dirty or self.raw_dirty):
            return
        if self.raw_dirty:
            try:
                data = project.parse_json(self.raw.get('1.0', 'end-1c'))
                if not isinstance(data, dict) or not isinstance(data.get('linhas'), list):
                    raise ValueError('Estrutura JSON incompleta.')
            except (ValueError, TypeError):
                self.status.set('JSON incompleto: o salvamento automático aguarda uma estrutura válida.')
                return
        raw_position = (self.raw.index('insert'), self.raw.yview()[0], self.raw.xview()[0]) if self.raw_dirty else None
        if self.save_current():
            if raw_position:
                self.raw.mark_set('insert', raw_position[0])
                self.raw.yview_moveto(raw_position[1])
                self.raw.xview_moveto(raw_position[2])
            self.status.set(f'Cena salva automaticamente: {self.current_scene}')

    def sync_raw(self):
        if self.data is not None:
            self.rendering = True
            self.set_text(self.raw, json.dumps(self.data, ensure_ascii=False, indent=2) + '\n')
            self.rendering = False
            self.raw_dirty = False

    def apply_raw(self):
        try:
            data = project.parse_json(self.raw.get('1.0', 'end-1c'))
            if not isinstance(data, dict) or not isinstance(data.get('linhas'), list):
                raise ValueError('Use um objeto com a lista "linhas".')
            self.data = data
            self.dirty = True
            self.raw_dirty = False
            self.validation_state.set('Alterações pendentes')
            self.validation_label.configure(style='Muted.TLabel')
            self.current_index = None
            self.fill_rows()
            self.status.set('JSON aplicado ao editor. Salve e valide o projeto.')
            return True
        except Exception as exc:
            issue = project.Issue(
                f'JSON não aplicado: {exc}',
                str(self.path),
                self.current_scene or '',
                json_line=getattr(exc, 'lineno', None),
                column=getattr(exc, 'colno', None),
            )
            self.log(issue.message, issue)
            project.save_log(self.work, project.Inspection(issues=[issue]))
            if issue.json_line:
                self.raw.see(f'{issue.json_line}.{max(0, (issue.column or 1) - 1)}')
            self.root.bell()
            self.status.set('Corrija a sintaxe do JSON antes de salvar.')
            return False

    def on_tab_changed(self, _=None):
        if self.rendering:
            return
        if self.notebook.index('current') == 1 and not self.raw_dirty:
            self.sync_raw()
        elif self.notebook.index('current') == 0 and self.raw_dirty:
            if not self.apply_raw():
                self.notebook.select(1)

    def save_current(self):
        self.cancel_autosave()
        if self.busy:
            return False
        if self.raw_dirty and not self.apply_raw():
            return False
        if self.data is None or not self.dirty:
            return True
        try:
            self.fingerprint = project.save_scene(self.work, self.path, self.data, self.fingerprint)
            self.dirty = False
            self.sync_raw()
            self.status.set(f'Cena salva: {self.current_scene}')
            return True
        except Exception as exc:
            issue = project.Issue(f'Falha ao salvar: {exc}', str(self.path), self.current_scene or '')
            self.log(issue.message, issue)
            try:
                project.save_log(self.work, project.Inspection(issues=[issue]))
            except OSError:
                pass
            self.status.set('A cena não foi salva. Veja o log; suas alterações continuam no editor.')
            return False

    def reload_scene(self):
        if self.busy or not self.current_scene:
            return
        self.cancel_autosave()
        if self.dirty or self.raw_dirty:
            raw = (self.raw.get('1.0', 'end-1c') if self.raw_dirty else json.dumps(self.data, ensure_ascii=False, indent=2)).encode('utf-8')
            backup = self.work / 'backups' / 'editor_nao_salvo' / f'{scripts.sha(raw)[:20]}_{self.path.name}'
            project.atomic_write(backup, raw)
            self.log(f'Alterações do editor preservadas em {backup.name}.')
        self.dirty = self.raw_dirty = False
        self.open_scene(self.current_scene)

    def set_busy(self, state):
        self.busy = state
        if state:
            self.progress.start(12)
            self.validation_state.set('Validando projeto…')
            self.validation_label.configure(style='Muted.TLabel')
        else:
            self.progress.stop()
        for button in [self.save_button, self.validate_button, self.generate_button]:
            button.configure(state='disabled' if state else 'normal')
        self.pt.configure(state='disabled' if state else 'normal')
        self.raw.configure(state='disabled' if state else 'normal')

    def run_validation(self, generate=False):
        if self.busy or not self.save_current():
            return
        self.issues.delete(*self.issues.get_children())
        self.issue_map.clear()
        self.set_busy(True)
        self.status.set('Conferindo todos os JSONs, compilando .epk e instalando no mod…' if generate else 'Conferindo todos os JSONs, IDs, referências e tags…')
        output = Path(self.output.get())

        def worker():
            try:
                result = project.inspect_project(self.work)
                generated = project.compile_and_install_epk(self.work, mod_epk_dir=output, inspection=result) if generate and not result.errors else None
                log = project.save_log(self.work, result, generated)
                self.messages.put(('validated', result, generated, log))
            except Exception as exc:
                try:
                    failure = project.Inspection(issues=[project.Issue(str(exc))])
                    log = project.save_log(self.work, failure)
                    self.messages.put(('failed', f'{exc} — log: {log.name}'))
                except Exception:
                    self.messages.put(('failed', str(exc)))

        threading.Thread(target=worker, daemon=True).start()

    def poll(self):
        try:
            while True:
                message = self.messages.get_nowait()
                self.set_busy(False)
                if message[0] == 'failed':
                    self.root.bell()
                    self.validation_state.set('Operação interrompida')
                    self.validation_label.configure(style='Error.TLabel')
                    self.log(message[1])
                    self.status.set('Operação interrompida. Veja o log.')
                    continue
                _, result, generated, log = message
                for issue in result.issues:
                    self.log(issue.message, issue)
                if result.errors:
                    self.root.bell()
                    self.validation_state.set(f'{len(result.errors)} erro(s)')
                    self.validation_label.configure(style='Error.TLabel')
                    first = self.issues.get_children()[0]
                    self.issues.selection_set(first)
                    self.issues.see(first)
                    self.status.set(f'{len(result.errors)} erro(s). Exportação bloqueada. Log: {log.name}')
                elif generated:
                    self.validation_state.set('.epk instalados no mod')
                    self.validation_label.configure(style='Success.TLabel')
                    self.log(f'Compilados e instalados {generated["arquivos_epk"]} arquivos .epk em {generated["pasta_mod"]}.', ok=True)
                    self.status.set(f'Mod atualizado: {generated["pasta_mod"]}')
                else:
                    notices = len(result.issues)
                    self.validation_state.set(f'Projeto válido • {notices} aviso(s)' if notices else 'Projeto válido')
                    self.validation_label.configure(style='Muted.TLabel' if notices else 'Success.TLabel')
                    self.log(f'Validação concluída: {result.manifest["line_count"]} linhas, sem erros estruturais.', ok=True)
                    self.status.set(f'Projeto válido. Log salvo em {log.name}')
        except queue.Empty:
            pass
        self.root.after(80, self.poll)

    def selected_issue(self):
        selection = self.issues.selection()
        return self.issue_map.get(selection[0]) if selection else None

    def jump_issue(self, _=None):
        issue = self.selected_issue()
        if not issue:
            return
        scene = issue.scene
        if not scene and issue.file:
            scene = next(
                (s for s, m in self.manifest['scenes'].items() if str((self.work / m['path']).resolve()) == issue.file),
                None,
            )
        if scene and self.open_scene(scene, issue.row_id):
            if issue.json_line or issue.field == 'id' or self.data is None:
                self.notebook.select(1)
                if issue.json_line:
                    index = f'{issue.json_line}.{max(0, (issue.column or 1) - 1)}'
                    self.raw.see(index)
                    self.raw.mark_set('insert', index)
                elif issue.row_id:
                    self.status.set(f'ID {issue.row_id}: corrija/restaure o registro no JSON ou use Restaurar linha.')
                self.raw.focus_set()
            else:
                self.pt.focus_set()

    def restore_selected(self):
        issue = self.selected_issue()
        if not issue or not issue.scene:
            self.log('Selecione um erro que indique cena e ID de linha.')
            return
        if not self.save_current():
            return
        try:
            meta = self.manifest['scenes'][issue.scene]
            path = self.work / meta['path']
            if not path.exists():
                data = {
                    'cena': issue.scene,
                    'arquivo': meta['filename'],
                    'linhas': [project.restore_record(self.work, issue.scene, n + 1) for n in meta['offsets']],
                }
                project.save_scene(self.work, path, data)
                self.dirty = self.raw_dirty = False
                self.open_scene(issue.scene, issue.row_id)
                self.log(f'Cena {issue.scene} restaurada das fontes originais; revise o PT-BR.', ok=True)
                return
            if not issue.row_id:
                self.log('Este erro não indica um ID restaurável. Corrija o arquivo na aba JSON da cena.')
                return
            data = project.read_scene(path)
            restored = project.restore_record(self.work, issue.scene, issue.row_id)
            existing = next((r for r in data['linhas'] if isinstance(r, dict) and r.get('id') == issue.row_id), None)
            if existing:
                existing['jp'] = restored['jp']
                existing['en'] = restored['en']
                if not isinstance(existing.get('Pt-br'), str):
                    existing['Pt-br'] = restored['Pt-br']
            else:
                data['linhas'].append(restored)
                data['linhas'].sort(key=lambda r: r.get('id', 0))
            project.save_scene(self.work, path, data)
            self.dirty = self.raw_dirty = False
            self.open_scene(issue.scene, issue.row_id)
            self.log(f'ID {issue.row_id} restaurado das fontes originais; revise o PT-BR antes de exportar.', ok=True)
        except Exception as exc:
            self.log(f'Falha na restauração: {exc}')

    def open_logs(self):
        folder = self.work / 'logs'
        folder.mkdir(exist_ok=True)
        if os.name == 'nt':
            os.startfile(folder)

    def close(self):
        if self.busy:
            self.status.set('Aguarde a operação terminar para fechar.')
            return
        if self.save_current():
            self.root.destroy()


def main():
    root = tk.Tk()
    ReviewPanel(root)
    root.mainloop()


if __name__ == '__main__':
    main()
