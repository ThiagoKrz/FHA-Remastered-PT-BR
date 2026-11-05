# Imagens em inglês: planejamento

Este documento lista as imagens do Fate/hollow ataraxia Remastered que mostram texto em inglês e explica como elas serão traduzidas. As pastas do fpm (`C:\Users\Thiago\Pictures\fpm\FHA`) não foram alteradas; tudo o que está aqui é cópia.

## Pastas e arquivos

| Item | O que é |
| --- | --- |
| `originais\<pacote>\<caminho original>` | As imagens **desta leva**: 471 imagens, 1.068 arquivos. |
| `imagens_prontas\<pacote>\<caminho original>` | Imagens **já em PT**, prontas para entrar no jogo. Hoje são 153 arquivos de menu vindos do FSN. |
| `proxima_leva\hanafuda\…` | O modo hanafuda, que ficou para depois. |
| `Planilha_Traducao_Imagens_FHA.xlsx` | As sugestões de tradução: uma linha por texto de cada imagem, para você corrigir. |

Os pacotes ficam assim:

- `pack00m_gui`: menus em 1x e 2x;
- `pack00d_gui`: os mesmos menus em 4x;
- `pack10d`: `ex_pack.dat`;
- `pack11d`: `ex_pack2.dat`.

O mge01 saiu inteiro da leva, porque o jogo não usa essas imagens.

Depois do pacote vem o mesmo caminho da pasta extraída, para cada arquivo voltar ao seu lugar.

### Como usar `imagens_prontas`

1. Ao terminar uma imagem, salve em `imagens_prontas` com o mesmo caminho, nome e tamanho em pixels do arquivo em `originais`. Exemplo: `originais\pack00m_gui\02_title\t_continue_1@2x.webp` vira `imagens_prontas\pack00m_gui\02_title\t_continue_1@2x.webp`.
2. Formato: os originais do FHA são WebP sem perda (`VP8L`, sem metadados extras) e quase todos são RGBA. Salve no mesmo formato.
3. Um menu só fica pronto quando as três resoluções estiverem lá: 1x e 2x em `pack00m_gui` e 4x em `pack00d_gui`.
4. Na recompilação, só entra o que estiver em `imagens_prontas`.

## Situação atual

A planilha de tradução tem 1.011 textos, das 471 imagens que ficaram em `originais`. Imagens com o mesmo texto aparecem juntas na mesma linha, por exemplo `menu_save_1`, `_2` e `_3`.

| Coluna | O que tem |
| --- | --- |
| **Sugestão PT-BR** | A sugestão de tradução. Pode corrigir direto nela. |
| **Atenção** | "⚠ revisar" (143 textos) quando posso ter traduzido mal; "❓ não sei" (15) quando não soube traduzir com segurança. |
| **Nota** | O motivo da marcação. |
| **Fonte** | De onde veio a sugestão: FSN (347), o texto que o jogo já usa no `uistring` (283) ou tradução minha (381). |
| **Revisado** | Uma setinha para marcar ✔ quando você conferir a linha. |

Por imagem, a situação é esta:

| Situação | Menus | pack10d | pack11d | Total |
| --- | ---: | ---: | ---: | ---: |
| Completa | 1 | 0 | 0 | 1 |
| Pronta do FSN, falta 4x | 77 | 0 | 0 | 77 |
| Pronta em parte | 1 | 0 | 0 | 1 |
| A fazer | 249 | 1 | 142 | 392 |
| **Total** | **328** | **1** | **142** | **471** |

- **Completa:** todos os arquivos da imagem já estão em `imagens_prontas`. Hoje é só o `guide_08_us`, que não tem 4x.
- **Pronta do FSN, falta 4x:** a 1x e a 2x vieram do FSN. A 4x ainda precisa ser feita.
- **Pronta em parte:** a `dialog_com4_1@v1`. O FSN só tinha a 2x dela, então faltam a 1x e a 4x.
- **A fazer:** a imagem precisa ser editada.

Saíram da leva 219 imagens, e as cópias delas já foram apagadas de `originais`:

- **167 que você apagou.**
- **52 que tirei depois, com o seu OK:**
  - texto igual em PT ("Config", "OK", "MENU", "Eclipse");
  - as 16 do mge01, que o jogo não usa;
  - títulos e nomes que o `uistring` mantém;
  - as imagens que tinham ficado com só parte das resoluções: `t_config_1`, `t_gallery_4` e `t_le_1` a `t_le_4`.

## O que veio pronto do FSN

São 153 arquivos em `imagens_prontas\pack00m_gui`, que cobrem 79 imagens. Só entraram imagens que são a mesma imagem do FSN:

- mesmo nome e mesmo tamanho em pixels;
- mesmo texto em inglês: todos os termos da planilha do FSN aparecem no FHA;
- mesma arte e mesmas cores, conferidas lado a lado.

Os PNG do FSN (`C:\Users\Thiago\Pictures\fpm\FSN\patch00mextraido`) foram convertidos para WebP sem perda, com o nome exato do FHA. Cada arquivo gerado foi conferido: tamanho igual ao original do FHA, formato `VP8L` e pixels idênticos aos do PNG do FSN.

Nenhuma dessas imagens está entre as que você excluiu.

**Quais são:**

- **02_title:** `t_continue_4`, `t_exit_4`, `t_newgame_4`;
- **07_config:** `07_cv_00c_us`, `07_cv_27b_us`, `07_cv_27c_us`;
- **08_date:** `day_subtitle00/01/02_us`;
- **common:**
  - `btn_back`, `btn_back2`, `btn_back3`;
  - os três `config_mute*_us`;
  - `dialog_com2` a `dialog_com7`;
  - `icon_savelavel_us` e `icon_savemode_us`;
  - os menus `Library`, `Picture`, `edlist`, `guide`, `load`, `movie`, `music`, `save`, `serv` e `wep`;
  - `menu_title_3/4/5`;
  - `dialog_com3_1@v1` e `dialog_com4_1@v1` (o original `@v1` delas é idêntico ao normal);
- **guide:** `guide_08_us`;
- **imgtext:** `contxt01*`, `libtxt01/02*`, `weptxt01*`.

**Ficaram de fora**, mesmo com o mesmo nome no FSN, porque no FHA a imagem é outra:

| Imagem | Diferença |
| --- | --- |
| `menu_flow` | FHA "Flag List", FSN "Flowchart" |
| `menu_to_title` | FHA "Save & Title", FSN "Return Top" |
| `menu_title_6` | FHA "ENTRANCE", FSN "FLOWCHART" |
| `pictxt01` | lista diferente |
| `selwin_txt` | sinopse diferente |
| `guide_01` a `guide_07` e `guide_09` | o FSN tem comandos a mais |
| `t_*_1` a `t_*_3` | outra altura; no FHA diz "Start" |
| `mustxt` | tamanho e texto diferentes |
| `sbed_font` | tamanho e texto diferentes |
| `weptxt` em 4x | a 4x do FSN não foi traduzida |
| outras variantes `@v1` | outro estilo |

## Padrão do texto

A sugestão de cada texto segue esta ordem:

1. **O texto do FSN**, quando a imagem é a mesma do FSN. Valem as decisões de lá: "Aperte Um Botão", "Dojô da Tigresa", FIM, "SAVE. RÁPIDO"…
2. **O texto que o jogo já usa no `uistring`.** Os rótulos `g_…` têm o texto das imagens de história; os rótulos `m_`/`mp_`/`jj_` têm os menus, o mapa e o santuário.
   - Quando achei a tradução do `uistring` fraca, a sugestão é outra e a nota mostra o que o `uistring` diz. Exemplo: "Sua diabinha maldita" para "You damned devil".
   - Se você ficar com a versão da planilha, vale corrigir o `uistring` também, para o texto e a imagem baterem.
3. **Tradução minha**, seguindo o glossário. Foi assim nos títulos das cenas, nas músicas, nas frases do final e em alguns botões.
   - Glossário: Brasão Mágico, Olhos Místicos, magia, Clube de Arco e Flecha, Guerra do Santo Graal.
   - Músicas: segui o padrão do FSN. Romaji vira PT, título em inglês fica e os parênteses são traduzidos.

**Outras regras:**

- **Nomes:** não se traduzem e ficam na ordem japonesa.
- **`uistring.epk_dec`:** as 99 strings de menu do FSN já foram aplicadas, ainda sem commit.

## Decisões

**Respondidas no chat:**

- não traduzir nomes;
- seguir o padrão do FSN;
- deixar o hanafuda fora;
- tirar da leva o mge01, as imagens sem mudança e as que estavam pela metade.

**Edição:** começar pela 4x e fazer a 2x e a 1x a partir dela. Nas 77 imagens que vieram prontas do FSN, a 4x é feita com o mesmo texto e o mesmo layout do FSN.

## Recompilação (quando for a hora)

O caminho é o mesmo do FSN (`C:\Users\Thiago\Pictures\fpm\FSN\LEIA-ME_COMPILACAO.md`), sempre a partir de `imagens_prontas`.

- **pack10d e pack11d:**
  1. Copie os arquivos para a pasta `…dat_extract`.
  2. Remonte o banco com o `ExtratorFSN.exe`. Ele está em `pack10dextraido\pack` e `pack11dextraido\pack`; o código fica em `Ferramentas\ExtratorFSN`.
  3. Leve juntos o `REPACK_<nome>.dat` e o `REPACK_fileinfo_<nome>.txt`, com o nome original.
- **Menus (pack00m e pack00d):** substitua os arquivos na pasta extraída e empacote com `fpm.exe pack`.
- **Patch separado:** o FHA aceita `patchXX.bin` por cima dos pacotes originais, como o FSN. Você já testou. Assim, o patch leva só os arquivos alterados.

## Limites

- O OCR não lê bem fontes estilizadas. Uma imagem com inglês muito estilizado pode ter escapado.
- Os títulos das listas (cenas, músicas) vieram do OCR. Se algum não bater com a imagem, confira nela.
  - No `scene01` acrescentei "Level Up?", que o OCR leu mal.
  - "Emiya Anmar" e "Not", no `scene10`, estão marcados como dúvida.
