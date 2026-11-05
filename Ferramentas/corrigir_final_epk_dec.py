"""
Corrige o FINAL dos arquivos .epk_dec antes de compilar.

Problema: o `main.exe dec` estraga os últimos bytes do arquivo (o `::` + quebras
de linha do último registro viram lixo) quando o tamanho não é múltiplo de 8.
O `main.exe enc` grava esses bytes como estão, e o jogo lê além do fim do texto.
Resultado no jogo: a última fala do arquivo aparece como `$$$message_XXXX$$$`.

Regra aplicada: todo arquivo precisa terminar com o último registro fechado em
`::` seguido de `\n\n` (igual aos arquivos oficiais).

Uso (por padrão NÃO grava nada, só mostra onde aplicaria):
    python corrigir_final_epk_dec.py <pasta_ou_arquivo> [--ref <pasta_scripts_EN>]
    python corrigir_final_epk_dec.py <pasta_ou_arquivo> --ref <pasta_EN> --aplicar
    python corrigir_final_epk_dec.py <pasta> --csv relatorio.csv

--ref     pasta com os scripts de referência descriptografados (EN/JP) com os
          mesmos nomes de arquivo. Serve para reconhecer exatamente o lixo que a
          tradução herdou. Sem ela, só o lixo "óbvio" (bytes inválidos, �,
          controle) é cortado automaticamente; o resto vai para REVISAR.
--aplicar grava as correções automáticas. Itens REVISAR nunca são gravados.

Classes do relatório:
    OK                 já termina em `::\n\n`
    SEM_QUEBRA         termina em `::` sem nenhuma quebra de linha (bugou no FHA)
    UMA_QUEBRA         termina em `::\n` (baixo risco, só padroniza para `::\n\n`)
    LIXO_DEPOIS_DO_FIM registro fechado, mas com lixo depois do `::` final
    SEM_TERMINADOR     último registro sem `::` final (texto + lixo)
    REVISAR            não dá para separar texto de lixo com segurança
"""
import argparse
import csv
import os
import re
import sys

FFFD = "\ufffd".encode()
REC_START = re.compile(rb"(?:^|\n)(\d+::)")
PUNCT = ".!?…"


def cols_from_header(b):
    lines = b.split(b"\n", 2)
    if len(lines) < 2 or not lines[0].lstrip(b"\xef\xbb\xbf").rstrip(b"\r") == b"DAT":
        return None
    return len([c for c in lines[1].rstrip(b"\r").split(b"::") if c])


def ref_garbage(ref_bytes):
    """Lixo que o dec deixou no fim da referência (só existe quando len % 8 está entre 1 e 4)."""
    if not ref_bytes:
        return b""
    r = len(ref_bytes) % 8
    return ref_bytes[-r:] if 1 <= r <= 4 else b""


def valid_utf8_end(t):
    for k in range(1, 5):
        if len(t) < k:
            break
        try:
            t[-k:].decode("utf-8")
            return True
        except UnicodeDecodeError:
            pass
    return False


def strip_obvious_junk(t):
    """Corta só o que com certeza é lixo: bytes inválidos, �, controle, espaços, ':'."""
    while t:
        if t.endswith(FFFD):
            t = t[:-3]
            continue
        c = t[-1]
        if c in b"\r\n \t:" or c < 0x20 or (c >= 0x80 and not valid_utf8_end(t)):
            t = t[:-1]
            continue
        break
    return t


def char_kind(ch):
    if not ch:
        return "vazio"
    if ch in "\"”'’":
        return "aspas"
    if ch == "]":
        return "tag"
    if ch in PUNCT or ch == ")":
        return "pontuacao"
    return "texto"


def last_text_char(b):
    try:
        s = b.decode("utf-8", "replace")
    except Exception:
        return ""
    s = s.rstrip(" \r\n:\ufffd")
    return s[-1:] if s else ""


def analyze(b, ref=None):
    """Retorna (classe, novo_conteudo_ou_None, label_do_ultimo_registro, observacao)."""
    if b.endswith(b"::\n\n") or b.endswith(b"::\r\n\r\n"):
        return "OK", None, "", ""
    ncols = cols_from_header(b)
    if ncols is None:
        return "REVISAR", None, "", "sem cabeçalho DAT"
    starts = [m.start(1) for m in REC_START.finditer(b)]
    if not starts:
        return "REVISAR", None, "", "nenhum registro encontrado"

    # procura, de trás pra frente, o último registro que começa direito
    for idx in range(len(starts) - 1, -1, -1):
        st = starts[idx]
        line = b[st:]
        fields = line.split(b"::")
        if len(fields) >= ncols:  # tem id + label + texto (+ colunas)
            break
    else:
        return "REVISAR", None, "", "último registro não reconhecido"

    head = b[:st]
    junk_after = b""
    if idx < len(starts) - 1:
        # linhas depois disso não formam registro (ex.: "32781::o"): é lixo
        junk_after = b[starts[idx + 1]:]
        line = b[st:starts[idx + 1]]
    fields = line.split(b"::")
    label = fields[1].decode("utf-8", "replace") if len(fields) > 1 else ""

    # Caso 1: registro já fechado com '::' e só falta a quebra / tem lixo depois
    body = b"::".join(fields[:ncols])
    tail = b"::".join(fields[ncols:])  # o que vem depois do '::' final
    if len(fields) > ncols:
        tail_clean = tail.strip(b"\r\n ")
        if not tail and not junk_after:
            return "SEM_QUEBRA", head + body + b"::\n\n", label, "risco: lixo do enc cola na última fala"
        if not tail_clean and not junk_after:
            return "UMA_QUEBRA", head + body + b"::\n\n", label, "baixo risco: só padronização"
        return "LIXO_DEPOIS_DO_FIM", head + body + b"::\n\n", label, f"cortado: {(tail + junk_after)[:20]!r}"

    # Caso 2: último campo sem '::' final -> texto + lixo
    text = fields[-1]
    prefix = b"::".join(fields[:-1]) + b"::"
    G = ref_garbage(ref) if ref is not None else b""
    exact = False
    if G and text.endswith(G):
        text = text[: -len(G)]
        exact = True
    cleaned = strip_obvious_junk(text)
    removed = text[len(cleaned):]
    new = head + prefix + cleaned + b"::\n\n"

    note = f"cortado: {(text[len(cleaned):] if not exact else G + removed)[:20]!r}"
    # confere com a referência: o texto deve terminar com o mesmo "tipo" de caractere
    if ref is not None:
        ref_text = ref[: -len(G)] if G else ref
        want = char_kind(last_text_char(ref_text))
        if char_kind(last_text_char(cleaned)) != want and G:
            # a tradução copiou só parte do lixo (ou trocou a ordem): corta bytes que pertencem ao lixo da referência
            t2 = cleaned
            while t2 and (t2[-1] in G or t2[-1] in b"\r\n \t:" or t2.endswith(FFFD)):
                t2 = t2[:-3] if t2.endswith(FFFD) else t2[:-1]
            t2 = strip_obvious_junk(t2)
            if char_kind(last_text_char(t2)) == want:
                return "SEM_TERMINADOR", head + prefix + t2 + b"::\n\n", label, f"cortado: {text[len(t2):][:20]!r} (lixo parcial da referência)"
        if char_kind(last_text_char(cleaned)) != want:
            return "REVISAR", new, label, note + f" | fim PT {last_text_char(cleaned)!r} x ref {last_text_char(ref_text)!r}"
    if exact or not removed.strip(b" \r\n:"):
        return "SEM_TERMINADOR", new, label, note
    # removeu algo que não era lixo óbvio e não foi confirmado pela referência
    try:
        removed.decode("utf-8")
        printable = True
    except UnicodeDecodeError:
        printable = False
    if printable and re.search(rb"[A-Za-z0-9]", removed):
        return "REVISAR", new, label, note + " | letras no lixo sem confirmação"
    return "SEM_TERMINADOR", new, label, note


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("alvo", help="pasta com .epk_dec ou um arquivo")
    ap.add_argument("--ref", help="pasta de referência descriptografada (ex.: scripts_EN)")
    ap.add_argument("--aplicar", action="store_true", help="grava as correções automáticas")
    ap.add_argument("--csv", help="salva o relatório em CSV")
    ap.add_argument("--todos", action="store_true", help="mostra também os arquivos OK")
    a = ap.parse_args()

    if os.path.isdir(a.alvo):
        files = sorted(os.path.join(a.alvo, f) for f in os.listdir(a.alvo) if f.endswith(".epk_dec"))
    else:
        files = [a.alvo]

    rows, counts = [], {}
    for p in files:
        b = open(p, "rb").read()
        ref = None
        if a.ref:
            rp = os.path.join(a.ref, os.path.basename(p))
            ref = open(rp, "rb").read() if os.path.exists(rp) else None
        cls, new, label, note = analyze(b, ref)
        counts[cls] = counts.get(cls, 0) + 1
        if cls == "OK" and not a.todos:
            continue
        before = b[-40:]
        after = new[-40:] if new else b""
        rows.append((os.path.basename(p), cls, label, before, after, note))
        if a.aplicar and new is not None and cls not in ("OK", "REVISAR"):
            open(p, "wb").write(new)

    out = sys.stdout
    for name, cls, label, before, after, note in rows:
        out.write(f"[{cls}] {name} {label}\n")
        out.write(f"    antes:  {before!r}\n")
        if after:
            out.write(f"    depois: {after!r}\n")
        if note:
            out.write(f"    {note}\n")
    out.write("\nResumo: " + ", ".join(f"{k}={v}" for k, v in sorted(counts.items())) + "\n")
    out.write("Gravado: SIM (exceto REVISAR)\n" if a.aplicar else "Gravado: NÃO (simulação). Use --aplicar para gravar.\n")

    if a.csv:
        with open(a.csv, "w", newline="", encoding="utf-8-sig") as f:
            w = csv.writer(f, delimiter=";")
            w.writerow(["arquivo", "classe", "ultimo_label", "fim_antes", "fim_depois", "obs"])
            for name, cls, label, before, after, note in rows:
                w.writerow([name, cls, label, repr(before), repr(after), note])


if __name__ == "__main__":
    main()
