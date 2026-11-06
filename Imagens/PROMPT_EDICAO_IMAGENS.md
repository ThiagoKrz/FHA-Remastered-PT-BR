# Prompt: edição das imagens do Fate/hollow ataraxia Remastered em PT-BR

> Copie este arquivo inteiro para a LLM que vai editar as imagens.

---

Você vai editar as imagens do **Fate/hollow ataraxia Remastered** (FHA) que mostram texto em inglês. O texto em inglês de cada imagem deve ser trocado pelo texto em português definido na planilha. Cada imagem pronta vai para a pasta de concluídas e precisa:

- manter **o mesmo nome**, o mesmo tamanho em pixels e o mesmo formato do original;
- manter a **mesma fonte, as mesmas cores, os mesmos efeitos e o mesmo alinhamento**.

O resultado tem que parecer feito pelo próprio estúdio.

## 1. Contexto

- **O projeto:** este é um patch de tradução feito por fãs. O texto do jogo já está traduzido; agora falta traduzir as imagens.
- **A raiz do projeto:** `C:\Users\Thiago\Desktop\FHA-Remastered-PT-BR`.
- **O texto de cada imagem já foi decidido.** Ele está na coluna **"Sugestão PT-BR"** da planilha. O dono do projeto revisou essa coluna.
  - Não retraduza e não "melhore" nada.
  - Se achar um erro evidente (digitação, acento faltando), não corrija sozinho: anote no relatório.
- **Os menus do FHA são os mesmos do Fate/stay night Remastered (FSN)**, que já foi traduzido por este grupo.
  - Os nomes de arquivo e as fontes são iguais aos do FSN, mas as cores às vezes mudam.
  - Algumas imagens já vieram prontas do FSN. Elas servem de **referência visual** para fonte, tamanho e acentos.

## 2. Regras que não podem ser quebradas

1. **Nunca altere nada em `Imagens\originais`, em `C:\Users\Thiago\Pictures\fpm` (pastas extraídas do jogo) nem nos scripts.** Tudo isso é só leitura.
2. **Grave as imagens editadas somente em `Imagens\imagens_prontas`.**
   - Use o **mesmo caminho relativo e o mesmo nome de arquivo** do original. A extensão `.webp` também é a mesma.
   - Exemplo: `originais\pack00m_gui\common\menu_scene_1@2x.webp` vira `imagens_prontas\pack00m_gui\common\menu_scene_1@2x.webp`.
3. **Não sobrescreva o que já está em `imagens_prontas`.** São 153 arquivos que vieram do FSN e foram conferidos. Para eles, falta só a versão 4x (ver a seção 8).
4. **Mantenha o canvas.** O tamanho em pixels, o modo de cor (RGBA/RGB) e o canal alfa ficam iguais aos do original. Nunca corte nem estique a imagem.
5. **Não mexa no hanafuda.** A pasta `Imagens\proxima_leva` fica de fora.
6. **Não use git.** Nada de commit, branch ou push.
7. **Não coloque atribuição de IA em lugar nenhum** (arquivos, metadados, relatório). A autoria do projeto é só do dono.
8. **Nomes de personagens não se traduzem.** O texto da planilha já respeita isso.

## 3. Onde está cada coisa

| O quê | Caminho |
| --- | --- |
| Planilha com o texto final | `Imagens\Planilha_Traducao_Imagens_FHA.xlsx` (aba **Traduções**) |
| Imagens originais (copiadas do jogo, só leitura) | `Imagens\originais\<pacote>\<caminho>` |
| Saída (concluídas) | `Imagens\imagens_prontas\<pacote>\<caminho>` |
| Script de conferência | `Imagens\validar_prontas.py` |
| Planejamento e decisões | `Imagens\PLANEJAMENTO.md` |
| Fontes do jogo (1x/2x) | `C:\Users\Thiago\Pictures\fpm\FHA\pack00mextraido\root\data\fuzz\release\root\resident\gui\font` |
| Fontes do jogo (4x) | `C:\Users\Thiago\Pictures\fpm\FHA\pack00dextraido\root\data\fuzz\release\root\resident\gui\font` |
| Fonte Jost (usada no FSN) | `C:\Users\Thiago\Pictures\fpm\FSN\ferramentas\cao_sensei\fontes\Jost-Variable.ttf` |
| Menus traduzidos do FSN (PNG, referência) | `C:\Users\Thiago\Pictures\fpm\FSN\patch00mextraido\root\data\fuzz\release\root\resident\gui\textures` |
| Scripts do jogo em PT (contexto) | `Pasta principal\scripts_pt-br\*.epk_dec` |
| Textos de interface e de imagem (contexto) | `Pasta principal\scripts_pt-br\uistring.epk_dec`. Os rótulos `g_…` têm o texto das imagens de história; os rótulos `m_`/`mp_`/`jj_` têm os menus, o mapa e o santuário. |
| Títulos das cenas (contexto) | `Pasta principal\scripts_pt-br\statictext.epk_dec` (rótulos `flowtext_…`) |
| Glossário | `Pasta principal\standards\type-moon\GLOSSARIO_TYPEMOON_OPERACIONAL.json` |
| Mapa script ↔ cena | `Planilha_Progresso_FHA.xlsx` (na raiz) |

Formato dos `.epk_dec`:

- linhas `id::rótulo::texto::`;
- no `uistring`, `id::rótulo::texto::texto_jp::`;
- o tab dentro do texto é quebra de linha.

Use esses arquivos só para entender o contexto de uma imagem. O texto que vai na imagem é sempre o da planilha.

Pacotes:

- `pack00m_gui`: menus em 1x e 2x;
- `pack00d_gui`: os mesmos menus em 4x;
- `pack10d` e `pack11d`: imagens do jogo (CGs, cartões, textos de cena), cada uma num tamanho só.

O Python 3.11 da máquina tem Pillow, numpy, pandas e openpyxl.

## 4. Como ler a planilha

Aba **Traduções**. Uma linha é um texto de uma imagem.

| Coluna | Uso |
| --- | --- |
| Pacote | `Menus (pack00m + pack00d)`, `pack10d` ou `pack11d` |
| Pasta | Pasta dentro do pacote (`common`, `02_title`…); `(raiz)` = sem pasta |
| Imagem(ns) | Nome do arquivo **sem** extensão e **sem** `@2x`/`@4x`. Várias imagens com o mesmo texto vêm separadas por vírgula, por exemplo `menu_save_1, menu_save_2, menu_save_3` |
| Texto em inglês (na imagem) | O texto que está lá hoje, para você localizar na imagem |
| **Sugestão PT-BR** | **O texto que vai na imagem** (final) |
| Atenção / Nota / Fonte / Revisado | Histórico da revisão; não muda o que você faz |
| Situação da imagem | `1x/2x prontas (FSN), falta 4x`, `só a 2x pronta (FSN)`, `pronta` ou vazio (= tudo a fazer) |

- **Imagem com vários textos** (listas, guias de controle, cartões): ela aparece em várias linhas seguidas com o mesmo valor em "Imagem(ns)". Cada linha é um texto da imagem; troque cada um no lugar dele.
- **Texto igual ao inglês** (nome próprio, por exemplo): se a "Sugestão PT-BR" for idêntica ao inglês, aquele texto fica como está.
- **Imagem sem nada para trocar:** se todos os textos dela ficarem iguais, não gere arquivo e anote no relatório.

Leitura sugerida:

```python
import pandas as pd
df = pd.read_excel(r'Imagens\Planilha_Traducao_Imagens_FHA.xlsx', sheet_name='Traduções')
for (pac, pasta, imgs), g in df.groupby(['Pacote', 'Pasta', 'Imagem(ns)'], sort=False):
    textos = list(zip(g['Texto em inglês (na imagem)'], g['Sugestão PT-BR']))
    for nome in [x.strip() for x in imgs.split(',')]:
        ...  # arquivos desta imagem: ver a seção 5
```

## 5. Do nome da planilha para os arquivos

**Menus (`Menus (pack00m + pack00d)`).** Para cada nome `X`, os arquivos são estes, mas só os que existirem em `originais`:

- `originais\pack00m_gui\<Pasta>\X.webp` (1x);
- `originais\pack00m_gui\<Pasta>\X@2x.webp` (2x);
- `originais\pack00d_gui\<Pasta>\X@4x.webp` (4x).

Variantes `@v1` fazem parte do nome. `btn_back@v1` vira `btn_back@v1.webp`, `btn_back@v1@2x.webp` e `btn_back@v1@4x.webp`.

**pack10d / pack11d.** O arquivo é `originais\<pacote>\X.webp`, porque a Pasta é `(raiz)`.

**O que gerar:** exatamente os arquivos que existem em `originais` e ainda não estão em `imagens_prontas`. Para ver a lista:

```
python Imagens\validar_prontas.py --faltando
```

## 6. Resoluções

- **Proporção dos menus:** a 2x tem **1,5×** o tamanho da 1x, e a 4x tem **3×** o tamanho da 1x (ou 2× a 2x). Não é 2× e 4×.
  - Exemplo: `menu_save_1` tem 320×64 em 1x, 480×96 em 2x e 960×192 em 4x.
- **Comece pela 4x.**
  1. Faça a 4x (`pack00d_gui`) primeiro, que é a versão de maior qualidade.
  2. Gere a 2x e a 1x **reduzindo a 4x**, sempre para o **tamanho exato do original de cada resolução**.
  3. Reduza com filtro LANCZOS e **alfa pré-multiplicado**: multiplique RGB pelo alfa, reduza e divida de volta. Assim não aparecem bordas escuras no brilho.
- **Exceções:**
  - **Só existe a 1x:** `btn_autoread*`, `btn_log*`, `btn_title*`, `btn_window*` (64×32), `hollow\tl_*`, `hollow\tk_*`, `hollow\mp_new3_a`, `special\jj_account_us`, `special\jj_back_us`, `special\jj_ema_us`, `special\jj_omikuji_us`, `guide\guide_08_us`, `60_endroll\149_edtext05`. Trabalhe direto no tamanho dela; se quiser, desenhe em 3× e reduza, para ficar mais suave.
  - **Não existe a 1x:** `07_config\07_cv_27c_us`, `common\dialog_com7_2`, `common\dialog_com7_3`. Elas só têm 2x (já pronta, do FSN) e 4x. Gere só a 4x.
  - **Proporção diferente:** `common\dialog_com6_2` tem 130×56 em 1x, 180×84 em 2x e 360×168 em 4x. A 1x é mais estreita; monte cada resolução pelo layout do próprio original.
  - **Sem 4x:** `menu_return_2`, `menu_return_3` e `sel_new1*` só têm 1x e 2x. Comece pela 2x.

## 7. Formato e metadados

Antes de gravar, confira o tipo do original. O script `validar_prontas.py` mostra a diferença se algo sair errado.

| Original | Como gravar (Pillow) |
| --- | --- |
| Menus (`pack00m_gui`, `pack00d_gui`): WebP **sem perda**, `VP8L` simples | `img.save(p, 'WEBP', lossless=True, quality=100, method=6, exact=True)` |
| pack11d, maioria: WebP estendido **sem perda** (`VP8X` + `VP8L`, mais um bloco `PSAI` do Photoshop) | Igual à linha de cima. O bloco `PSAI` não precisa ser recriado. |
| pack10d `wm_main01_us`: sem perda **com perfil de cor ICC** | Sem perda, passando também `icc_profile=Image.open(original).info.get('icc_profile')` |
| pack11d `dead_end`, `last`: WebP **com perda** (`VP8`), RGB | `img.save(p, 'WEBP', lossless=False, quality=95, method=6)` |
| pack11d `凛メモ字幕_us`: **com perda e com alfa** | `img.save(p, 'WEBP', lossless=False, quality=95, alpha_quality=100, method=6)` |

Em todos os casos:

- mantenha o **modo de cor** do original. Se o original for RGB, converta para RGB antes de gravar; se for RGBA, mantenha o alfa;
- não acrescente EXIF ou XMP.

## 8. Imagens que já vieram prontas do FSN

São 77 imagens de menu com a coluna Situação = `1x/2x prontas (FSN), falta 4x`.

- **O que já existe:** a 1x e a 2x delas estão em `imagens_prontas\pack00m_gui`. **Não toque nelas.**
- **O que fazer:** só a 4x (`pack00d_gui\…@4x.webp`), que tem que ficar **idêntica à 2x pronta**: mesmo texto, mesma posição, mesmo tamanho relativo de fonte e mesmos efeitos.
- **Como fazer a 4x:** redesenhe na 4x usando a 2x pronta como gabarito, com posições e tamanhos ×2. **Não amplie a 2x**, porque perde nitidez.
- **Exceção:** a `dialog_com4_1@v1` tem só a 2x pronta. Faça a 4x e a 1x seguindo a 2x.

Essas 2x prontas também são a melhor referência para os outros menus da mesma família. Elas mostram a fonte, o tamanho, o espaçamento e os acentos usados no FSN.

## 9. Fontes e estilo por família

A fonte precisa ser a mesma do original. A tabela abaixo é o ponto de partida, tirado de uma comparação visual.

**Antes de produzir uma família, confirme a fonte:**

1. Renderize o texto **em inglês** com a fonte candidata.
2. Sobreponha ao original.
3. Ajuste o tamanho até as letras coincidirem (formato do `a`, do `g`, do `R`, a espessura).

Se nenhuma candidata bater, procure nas fontes do jogo (as duas pastas da seção 3) e em `C:\Windows\Fonts`. Use a que ficar mais próxima e anote no relatório.

| Família (pasta/arquivos) | Fonte provável | Estilo a reproduzir |
| --- | --- | --- |
| `02_title\t_*`, `common\menu_*`, `menu_title_*`, `menu_to_title*`, `dialog_com*`, `mapdate\ec_bar-day*` | Futura Light. A mais próxima disponível é a **Jost, peso Light** (`Jost-Variable.ttf`, `font.set_variation_by_name('Light')`); a alternativa é `Futura Bk BT Book.ttf` | Texto fino. Cada variante (`_1`, `_2`, `_3`, `@v1`, `sel`/`on`) tem cor e brilho externo próprios (cinza neutro, azul, rosa, vermelho). Copie a cor de cada uma do próprio original. Alinhamento igual ao original (alguns à esquerda, títulos centralizados). Maiúsculas onde o original é maiúsculo. |
| `common\btn_*` (AUTO READ, LOG, GO TITLE, HIDE WINDOW, Back«, ▶Play), `config_test*` | Sans pequena; comparar com o `btn_back` pronto do FSN (`imagens_prontas\pack00m_gui\common\btn_back.webp`) | Botões muito pequenos (64×32). Se não couber, reduza o espaçamento e depois a fonte; nunca saia da área do botão. |
| `hollow\mp_place_*`, `hollow\mp_charbtn*` | Arredondada e grossa (mais próxima: `C:\Windows\Fonts\ARLRDBD.TTF`, Arial Rounded MT Bold; conferir) | Preenchimento em degradê vertical, contorno claro e brilho. As duas pílulas da imagem (normal e selecionada) têm cores diferentes. Copie as cores do original. |
| `hollow\tl_*`, `hollow\tk_title` | Serifada (identificar; candidatas: Bembo Book Bold do jogo, Times, Century) | `tl_*` são letras maiúsculas com várias cópias coloridas lado a lado na mesma imagem (estados do botão). Mantenha a mesma quantidade e a mesma posição de cada cópia. |
| `imgtext\*` (listas: `scene*`, `flisttxt*`, `libtxt*`, `mustxt*`, `pictxt*`, `scenetab*`, `contxt*`, `weptxt*`) | Sans pequena; comparar com `libtxt`/`weptxt`/`contxt` prontos do FSN | Listas em colunas. Cada linha da planilha é um item. Mantenha a posição, a coluna e a altura de cada item. A versão `sel` muda só a cor. |
| `guide\guide_*` | Sans das telas de controle; comparar com `guide_08_us` pronto (FSN) | Rótulos ao redor do desenho do controle. Não mexa no desenho. Rótulos em azul ("hold"/"segurar") mantêm o azul. |
| `08_date`, `map\ent_day2`, `common\ent_day1`, `mapdate\ec_day*` | Datas e "Dia N"; identificar pela comparação | Cartões de data. "AM/PM/Day" viram o texto da planilha. |
| `60_endroll\sbed_font*`, `149_edtext05` | Serifada clássica (Bembo/Garamond; candidatas: `BemboBookMTPro-Bold.otf` na pasta 4x do jogo, `C:\Windows\Fonts\GARA.TTF`) | Texto cinza-escuro sobre transparente, uma linha só. |
| pack11d, textos de cena (`074_*`, `076_*`, `088_*`, `100_*`, `107_*`, `136_*`, `143_*`, `147_*`, `070_*`, `093_*`, `023_*`, `090_*`, `097_*`) | **Bembo Book Bold** (`BemboBookMTPro-Bold.otf`, pasta de fontes 4x do jogo) | Branco com contorno ou sombra escura (ou o contrário). Copie a espessura do contorno e a cor do original. Mantenha a posição na imagem: elas são sobrepostas à cena no jogo. |
| pack11d, cartas e bilhetes (`040_letter*`, `凛メモ字幕_us`, `ジャプニカ暗殺帳*`, `36凛の魔術講座*`) | Pode ser manuscrita ou de giz; identificar | Escolha uma fonte com o mesmo jeito (manuscrita, se for) e anote. Não apague o fundo (papel, quadro). |
| pack11d, efeitos (`078_殺*`, `怨嗟*`, `17死の呪詛*`, `@voice_*`, `121_んん_us`, `クイズ鬼*`, `099_ミミックday*`, `next0*`, `bad_end_us`, `exit_end_us`, `dead_end`, `氷室恋愛探偵*`, `016_中華まん幟_us`, `jj_*`) | Variam: letreiros, tipos grossos ou condensados, palavras espalhadas | Reproduza o efeito: a repetição em padrão, a rotação, o tamanho de cada palavra espalhada, as maiúsculas e minúsculas alternadas do `@voice` e a cor. Em textos sobre CG, apague o inglês reconstruindo a arte por baixo (seção 10). |
| pack10d `wm_main01_us` | Igual às outras caixas de nome (`wm_main*`) | Só a palavra muda ("Recepcionista"). Mantenha o perfil ICC. |

**Acentos:** confira se a fonte escolhida tem ã, õ, ç, é, ê, á, í, ó, ú e â. A Jost e a Bembo têm. Nunca deixe caractere faltando, quadrado ou "tofu".

## 10. Como editar cada tipo de imagem

1. **Texto sobre fundo transparente** (quase todos os menus):
   - O cinza que aparece nas pré-visualizações não faz parte da imagem; o fundo é transparente.
   - Recrie a imagem num canvas transparente do mesmo tamanho.
   - Copie **pixel a pixel** do original os elementos que não são texto: setas «, ▶, molduras, ícones, pílulas, sublinhados.
   - Desenhe o texto em PT com a mesma fonte, a mesma cor, o mesmo brilho, o mesmo contorno e a mesma sombra.
   - O **brilho externo** sai assim: camada do texto → desfoque gaussiano → cor do brilho → opacidade. Meça o raio e a cor no original.
2. **Texto sobre painel liso ou em degradê:** apague o texto preenchendo com o padrão do painel (estendendo as linhas de cor ao redor) e escreva por cima.
3. **Texto sobre arte** (CG, papel, quadro, foto):
   - Apague só o texto, reconstruindo a arte por baixo com clonagem ou inpainting. Seja conservador.
   - Não borre nem repinte o resto da imagem.
   - Se não der para reconstruir bem, anote no relatório.
4. **Posição e alinhamento:** mantenha a linha de base, a posição e o alinhamento do original (centro, esquerda ou direita). Em listas, cada item fica na linha e na coluna dele.
5. **Quando o PT não cabe:**
   1. reduza um pouco o espaçamento entre letras;
   2. se ainda não couber, reduza a fonte o mínimo necessário, mantendo o mesmo tamanho nas imagens da mesma família;
   3. não quebre linha nem passe da área original sem necessidade;
   4. anote cada caso no relatório.
6. **Variantes de estado** (`_1`/`_2`/`_3`, `sel`/`on`/`@v1`): cada uma tem as cores dela. O texto é o mesmo e o layout também; mude só o que o original muda.

## 11. Conferência (obrigatória)

1. Rode a conferência:

   ```
   python Imagens\validar_prontas.py
   ```

   Tem que dar **0 com problema**. Ele confere nome e caminho, tamanho, modo de cor, tipo de WebP e perfil ICC contra o original.

2. Para cada imagem feita, monte uma **folha de comparação** com original e pronta lado a lado, nas três resoluções, sobre fundo escuro e claro. Olhe uma a uma:
   - não pode sobrar inglês;
   - acentos certos;
   - nada cortado;
   - brilho e contorno iguais;
   - 1x/2x/4x consistentes.
3. Rode a conferência de novo com `--faltando`, para ver o que ainda falta.

## 12. Entregáveis

1. As imagens em `Imagens\imagens_prontas\…`, com os nomes idênticos aos originais.
2. Um relatório em `Imagens\RELATORIO_EDICAO.md` com:
   - o que foi feito (imagem → arquivos gerados);
   - a fonte e o tamanho usados por família;
   - as imagens em que o texto precisou ser reduzido;
   - as imagens em que a arte teve de ser reconstruída;
   - as que não precisaram de arquivo (texto igual ao inglês);
   - as dúvidas;
   - o que ficou faltando.

Sem atribuição de IA no relatório.

## 13. Ordem de trabalho sugerida

1. **Calibrar:** pegue uma imagem de cada família de menu que tenha versão pronta do FSN, por exemplo `common\menu_save_1` e `dialog_com3_1`. Faça a 4x delas e compare com a 2x pronta. Assim você acerta fonte, tamanho e brilho antes de produzir em série.
2. As 77 imagens prontas do FSN (só a 4x).
3. `common` e `02_title` (botões e títulos).
4. `hollow` (mapa e título do hollow), `mapdate`, `map`, `special`.
5. `imgtext` (listas grandes: cenas, músicas, flags).
6. `guide` e `60_endroll`.
7. pack11d, textos de cena (Bembo Bold).
8. pack11d, efeitos, cartas e cartões, que são os mais trabalhosos.

Mostre o resultado da etapa 1 (calibração) ao dono do projeto antes de continuar com o resto.
