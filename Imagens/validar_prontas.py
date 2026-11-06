"""Confere as imagens de Imagens/imagens_prontas contra Imagens/originais.

Uso:  python validar_prontas.py            (confere tudo)
      python validar_prontas.py --faltando  (lista também o que ainda não foi feito)

Para cada arquivo pronto, confere:
  - existe um original com o mesmo caminho e o mesmo nome (o pack00d só tem os @4x);
  - mesmo tamanho em pixels;
  - mesmo modo de cor (RGBA/RGB);
  - mesmo tipo de WebP: sem perda (VP8L) ou com perda (VP8);
  - perfil de cor ICC presente quando o original tem.
Não abre nem altera os originais além de ler.
"""
import os, sys, struct
from PIL import Image

AQUI = os.path.dirname(os.path.abspath(__file__))
ORI = os.path.join(AQUI, 'originais')
PRO = os.path.join(AQUI, 'imagens_prontas')


def chunks(path):
    d = open(path, 'rb').read()
    out, i = [], 12
    while i + 8 <= len(d):
        cid = d[i:i + 4].decode('latin1')
        sz = struct.unpack('<I', d[i + 4:i + 8])[0]
        out.append(cid)
        i += 8 + sz + (sz & 1)
    return out


def tipo(path):
    c = chunks(path)
    return ('sem perda (VP8L)' if 'VP8L' in c else 'com perda (VP8)' if 'VP8 ' in c else '?'), ('ICCP' in c)


def arquivos(raiz):
    for dp, dn, fn in os.walk(raiz):
        for f in fn:
            yield os.path.relpath(os.path.join(dp, f), raiz)


erros, ok = [], 0
for rel in sorted(arquivos(PRO)):
    p, o = os.path.join(PRO, rel), os.path.join(ORI, rel)
    if not os.path.exists(o):
        erros.append(f'{rel}: não existe original com esse caminho/nome em originais')
        continue
    a, b = Image.open(p), Image.open(o)
    prob = []
    if a.format != 'WEBP':
        prob.append(f'formato {a.format} (precisa ser WEBP)')
    if a.size != b.size:
        prob.append(f'tamanho {a.size} ≠ original {b.size}')
    if a.mode != b.mode:
        prob.append(f'modo {a.mode} ≠ original {b.mode}')
    ta, ia = tipo(p)
    tb, ib = tipo(o)
    if ta != tb:
        prob.append(f'WebP {ta} ≠ original {tb}')
    if ib and not ia:
        prob.append('original tem perfil ICC e o pronto não')
    if prob:
        erros.append(f'{rel}: ' + '; '.join(prob))
    else:
        ok += 1

print(f'Conferidos: {ok + len(erros)} | OK: {ok} | Com problema: {len(erros)}')
for e in erros:
    print('  ✗', e)
if '--faltando' in sys.argv:
    falta = [r for r in sorted(arquivos(ORI)) if not os.path.exists(os.path.join(PRO, r))]
    print(f'Ainda sem versão pronta: {len(falta)}')
    for r in falta:
        print('  ·', r)
