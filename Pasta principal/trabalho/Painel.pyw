"""Abra este arquivo para revisar os textos de FHA e exportar os .epk_dec."""
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
        messagebox.showerror('Falha ao abrir o painel', f'Confira o log:\n{log}\n\n{traceback.format_exc()}')
    except Exception:
        pass
