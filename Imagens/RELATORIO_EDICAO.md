# Relatório de edição das imagens

<!-- FASE_7_INICIO -->
## Situação atual — fase 7 concluída em 06/11/2026

**Escopo autorizado:** os 97 arquivos restantes desta leva: 96 em `pack11d` e a caixa de nome `wm_main01_us`, de `pack10d`.

**1.065 arquivos prontos, 1.065 OK e zero com problema.** Foram acrescentados **97 arquivos**. **Não resta arquivo com edição necessária nesta leva.** Os três faltantes da lista bruta são `btn_log`, `btn_log2` e `btn_log3`, dispensados nas fases anteriores.

Os **1.068 originais**, os **968 arquivos anteriormente prontos** e a **planilha** foram preservados: **2.037 hashes iguais** aos do início da fase. A imagem com **Artoria**, concluída na fase 6, permanece intacta.

### Arquivos por família

| Família | Novos arquivos |
| --- | ---: |
| Caixa de nome | 1 |
| Faixa de bolinhos | 1 |
| Cartas de Shinto | 3 |
| Campo vermelho 078 | 4 |
| Cartões DIA | 4 |
| RPG 118 | 9 |
| Hum? | 1 |
| Maldições 17 | 3 |
| Diagramas de Rin | 5 |
| Vozes | 8 |
| Textos FK | 4 |
| Encerramentos | 3 |
| Santuário | 25 |
| Último Interlúdio | 1 |
| Próximo | 8 |
| Quiz | 2 |
| Capas Japunika | 2 |
| Abertura | 1 |
| Bilhete de Rin | 1 |
| Palavras vermelhas espalhadas | 5 |
| Himuro | 6 |
| **Total** | **97** |

### Texto e composição

- Texto da coluna Sugestão PT-BR utilizado sem retradução. A planilha foi somente lida. Foram preservadas a capitalização alternada dos `@voice`, as diferenças entre `Morra` e `MORRA` e a pontuação aprovada.
- `DIA 1` a `DIA 4` mantêm os numerais originais. A legenda diagonal foi traduzida e mantém sua inclinação. Os tipos grandes foram renderizados no tamanho nativo, sem ampliação de uma máscara pequena.
- `Hum?` conserva o ponto de interrogação desenhado no original.
- Os diagramas mantêm grade, setas, cruzes, infinito e os nomes Shirou A a E. Foram traduzidos os dias, Sabe, Morte, Paralelização de Todas as Experiências e Guerra do Santo Graal Recriada. A curva junto de Sabe foi separada da máscara das letras para sua preservação.
- Nas palavras espalhadas de `怨嗟02`, `03`, `04`, `05` e `07`, foram recuperadas respectivamente **3, 5, 7, 9 e 66 posições**, incluindo palavras parciais nas bordas.
- Os campos de repetição 078 mantêm quatro estágios, com camadas de tamanhos e contrastes crescentes. Os períodos medidos foram 336 × 88, 420 × 104, 525 × 132 e 1.130 × 238 px. A repetição da maldição 17 usa período aproximado de 144 × 113,6 px. A tipografia foi reconstruída; não se trata de identidade pixel a pixel com as letras originais.
- Nos textos do RPG 118, foi recomposta a inclinação que varia ao longo da linha, com brilho claro amarelado.
- Mantidas as três variantes de cor dos botões manuscritos e as quatro variantes de Voltar, nas respectivas posições.
- O corpo dos textos longos foi reduzido quando necessário. O painel da faixa vertical mantém o tamanho, a cor e a transparência do original. As quebras das cartas, da abertura e do bilhete foram acomodadas nos respectivos blocos.
- Os prefixos Próximo/ foram traduzidos. Os oito títulos que a planilha mantém em inglês ficaram como no original. BAD permanece como aprovado, e o texto BAD END. da tela correspondente foi preservado.
- Nas capas, foram traduzidas somente as duas legendas da planilha. Os nomes e os elementos japoneses restantes foram conservados.

### Recuperação dos fundos

As versões japonesas locais do próprio jogo foram consultadas somente para leitura. Quando apresentavam a mesma arte sem a legenda inglesa, foram usadas para recuperar o trecho sob a substituição. Isso se aplica à faixa 016, às cinco placas de compra de ema, aos seis símbolos de sorte, aos sete cartões de resultado, às duas telas de quiz, às duas capas e às seis telas de Himuro. As substituições foram limitadas às áreas das legendas.

Na caixa Recepcionista, o fundo liso foi recomposto a partir das cores intactas do próprio painel. Os fundos simples dos diagramas, de telas de encerramento e de legendas foram recompostos somente sob as letras.

Em `bad_end_us`, houve inpainting sob as três frases substituídas. Em `dead_end`, a tinta das letras foi isolada pelos canais de cor, removendo componentes espúrios antes do inpainting. A edição ficou restrita à máscara dilatada das letras; as chamas e a linha decorativa fora dessa máscara foram preservadas na composição antes da gravação com perda. Não foi redesenhada a arte das personagens.

### Fontes e tamanhos

As candidatas foram renderizadas com o inglês e comparadas por sobreposição, usando as fontes do jogo e as fontes locais. **As escolhas são aproximações; a identidade exata das fontes não foi comprovada.** A tabela informa o tamanho nominal vertical após a calibração e a acomodação, arredondado em pixels. As escalas, o espaçamento, a espessura, os retângulos e os parâmetros de efeitos estão nos registros da fase.

| Família | Fontes utilizadas | Tamanho nominal vertical |
| --- | --- | ---: |
| Caixa de nome | arial.ttf | 47 px |
| Faixa de bolinhos | arial.ttf | 12 px |
| Cartas de Shinto | segoeui.ttf | 34–53 px |
| Campo vermelho 078 | GARA.TTF | 34–157 px |
| Cartões DIA | arialbd.ttf, ariblk.ttf | 34–809 px |
| RPG 118 | BemboBookMTPro-Bold.otf | 42–50 px |
| Hum? | FOT-UDKakugo_LargePr6-DB.otf | 404 px |
| Maldições 17 | arial.ttf, ariali.ttf | 53–91 px |
| Diagramas de Rin | GARABD.TTF, cambria.ttc, georgiab.ttf | 27–74 px |
| Vozes | georgiai.ttf | 51–54 px |
| Textos FK | GARA.TTF, georgiai.ttf, timesi.ttf | 31–58 px |
| Encerramentos | cambria.ttc, georgia.ttf, times.ttf, timesbd.ttf | 37–50 px |
| Santuário | BRLNSDB.TTF, comicbd.ttf, segoeprb.ttf | 7–64 px |
| Último Interlúdio | GARA.TTF | 49 px |
| Próximo | GARA.TTF | 48 px |
| Quiz | arial.ttf | 35–37 px |
| Capas Japunika | arial.ttf | 23–30 px |
| Abertura | timesbd.ttf | 60–64 px |
| Bilhete de Rin | arial.ttf | 32 px |
| Palavras vermelhas espalhadas | georgiai.ttf | 86 px |
| Himuro | arial.ttf | 31–36 px |

### Reduções para acomodação

O quadro registra o menor tamanho relativo à base calibrada de cada arquivo. Cada trecho e cada estado têm seus próprios parâmetros no registro.

| Imagem | Menor tamanho relativo |
| --- | ---: |
| `016_中華まん幟_us` | 64.3% |
| `040_letter1_us` | 83.8% |
| `040_letter2_us` | 83.1% |
| `040_letter3_us` | 90.7% |
| `078_殺01_us` | 72.0% |
| `078_殺02_us` | 72.0% |
| `078_殺03_us` | 72.0% |
| `078_殺04_us` | 72.0% |
| `099_ミミックday1` | 94.6% |
| `099_ミミックday2` | 94.6% |
| `099_ミミックday3` | 94.6% |
| `099_ミミックday4` | 94.3% |
| `118_ゴバッチネンa_us` | 80.0% |
| `118_ゴバッチネンb_us` | 92.1% |
| `118_ゴバッチネンd_us` | 99.6% |
| `118_ゴバッチネンe_us` | 82.4% |
| `118_ゴバッチネンf_us` | 82.4% |
| `118_ゴバッチネンg_us` | 82.4% |
| `118_ゴバッチネンh_us` | 90.9% |
| `118_ゴバッチネンi_us` | 93.6% |
| `121_んん_us` | 98.7% |
| `17死の呪詛(呪)_us` | 88.1% |
| `17死の呪詛・全画面c_us` | 95.7% |
| `17死の呪詛・全画面d(呪)_us` | 56.4% |
| `FK016台詞a _us` | 89.4% |
| `FK016台詞a_us` | 89.4% |
| `FK025台詞b_us` | 79.2% |
| `bad_end_us` | 97.4% |
| `dead_end` | 89.7% |
| `jj_ema_us` | 82.4% |
| `jj_emabg夕_us` | 99.6% |
| `jj_money_us` | 94.8% |
| `jj_yen_us` | 72.0% |
| `last` | 94.1% |
| `ジャプニカ暗殺帳(士郎版)_us` | 72.4% |
| `ジャプニカ暗殺帳(慎二版)_us` | 72.4% |
| `凛メモ字幕_us` | 92.1% |
| `怨嗟02_us` | 88.1% |
| `怨嗟03_us` | 88.1% |
| `怨嗟04_us` | 88.1% |
| `怨嗟05_us` | 88.1% |
| `怨嗟07_us` | 88.1% |
| `氷室恋愛探偵01_us` | 97.3% |
| `氷室恋愛探偵02_us` | 92.2% |

### Observações de revisão

- A planilha contém **AIinDa** em `@voice_04(object)_us` e **ODdeio** em `@voice_08(object)_us`. Essas grafias foram mantidas literalmente; não houve correção silenciosa.
- A barra entre frases das cartas e da abertura foi interpretada como separação de linhas, mantendo as palavras e a pontuação. Em Revisão / Revanche, a barra é texto visível e foi mantida.
- O bilhete de Rin conserva o trecho literal **(...)** aprovado na planilha e o efeito de risco sobre esse trecho. A frase inglesa riscada não foi reinserida.
- A validação técnica e a revisão das composições não substituem a conferência dentro do jogo. Não houve compilação, instalação ou teste no jogo.

### Conferência

- **97 arquivos novos**, nos nomes, caminhos, dimensões e modos RGB/RGBA de seus originais. Nenhum arquivo anterior foi substituído.
- Perfil ICC de `pack10d/wm_main01_us.webp` preservado, com os mesmos bytes do original.
- Formato WebP conferido por arquivo. Os arquivos sem perda foram reabertos e comparados pixel a pixel com os mestres. Os arquivos com perda usam qualidade 95; o alfa do arquivo RGBA foi preservado. Não foram acrescentados EXIF/XMP; o bloco PSAI não foi recriado.
- Conferência de texto, presença dos glifos, retângulos e preservação de pixels fora das áreas de edição nas 97 composições. Valores RGB invisíveis sob alfa zero foram desconsiderados nessa verificação de arte.
- 97 provas de original/PT-BR em fundos claro e escuro e 25 pranchas de comparação. Os recortes mantêm detalhes nativos quando cabem; vistas gerais grandes são reduzidas somente nas provas.
- **1.065 conferidos, 1.065 OK e zero com problema** no validador do projeto. Apenas os três LOG dispensados continuam na lista bruta.
- **2.037 hashes preservados**, incluindo os 968 arquivos anteriores e a planilha. Scripts do jogo, pastas extraídas e hanafuda não foram alterados. Não houve uso de Git.

### Imagem → arquivo gerado

Todos os caminhos abaixo são relativos a `Imagens/imagens_prontas`.

| Imagem-base | Arquivo desta fase |
| --- | --- |
| `wm_main01_us` | `pack10d/wm_main01_us.webp` |
| `016_中華まん幟_us` | `pack11d/016_中華まん幟_us.webp` |
| `040_letter1_us` | `pack11d/040_letter1_us.webp` |
| `040_letter2_us` | `pack11d/040_letter2_us.webp` |
| `040_letter3_us` | `pack11d/040_letter3_us.webp` |
| `078_殺01_us` | `pack11d/078_殺01_us.webp` |
| `078_殺02_us` | `pack11d/078_殺02_us.webp` |
| `078_殺03_us` | `pack11d/078_殺03_us.webp` |
| `078_殺04_us` | `pack11d/078_殺04_us.webp` |
| `099_ミミックday1` | `pack11d/099_ミミックday1.webp` |
| `099_ミミックday2` | `pack11d/099_ミミックday2.webp` |
| `099_ミミックday3` | `pack11d/099_ミミックday3.webp` |
| `099_ミミックday4` | `pack11d/099_ミミックday4.webp` |
| `118_ゴバッチネンa_us` | `pack11d/118_ゴバッチネンa_us.webp` |
| `118_ゴバッチネンb_us` | `pack11d/118_ゴバッチネンb_us.webp` |
| `118_ゴバッチネンc_us` | `pack11d/118_ゴバッチネンc_us.webp` |
| `118_ゴバッチネンd_us` | `pack11d/118_ゴバッチネンd_us.webp` |
| `118_ゴバッチネンe_us` | `pack11d/118_ゴバッチネンe_us.webp` |
| `118_ゴバッチネンf_us` | `pack11d/118_ゴバッチネンf_us.webp` |
| `118_ゴバッチネンg_us` | `pack11d/118_ゴバッチネンg_us.webp` |
| `118_ゴバッチネンh_us` | `pack11d/118_ゴバッチネンh_us.webp` |
| `118_ゴバッチネンi_us` | `pack11d/118_ゴバッチネンi_us.webp` |
| `121_んん_us` | `pack11d/121_んん_us.webp` |
| `17死の呪詛(呪)_us` | `pack11d/17死の呪詛(呪)_us.webp` |
| `17死の呪詛・全画面c_us` | `pack11d/17死の呪詛・全画面c_us.webp` |
| `17死の呪詛・全画面d(呪)_us` | `pack11d/17死の呪詛・全画面d(呪)_us.webp` |
| `36凛の魔術講座_us` | `pack11d/36凛の魔術講座_us.webp` |
| `36凛の魔術講座b_us` | `pack11d/36凛の魔術講座b_us.webp` |
| `36凛の魔術講座c_us` | `pack11d/36凛の魔術講座c_us.webp` |
| `36凛の魔術講座d_us` | `pack11d/36凛の魔術講座d_us.webp` |
| `36凛の魔術講座e_us` | `pack11d/36凛の魔術講座e_us.webp` |
| `@voice_01(object)_us` | `pack11d/@voice_01(object)_us.webp` |
| `@voice_02(object)_us` | `pack11d/@voice_02(object)_us.webp` |
| `@voice_03(object)_us` | `pack11d/@voice_03(object)_us.webp` |
| `@voice_04(object)_us` | `pack11d/@voice_04(object)_us.webp` |
| `@voice_05(object)_us` | `pack11d/@voice_05(object)_us.webp` |
| `@voice_06(object)_us` | `pack11d/@voice_06(object)_us.webp` |
| `@voice_07(object)_us` | `pack11d/@voice_07(object)_us.webp` |
| `@voice_08(object)_us` | `pack11d/@voice_08(object)_us.webp` |
| `FK016台詞a _us` | `pack11d/FK016台詞a _us.webp` |
| `FK016台詞a_us` | `pack11d/FK016台詞a_us.webp` |
| `FK025台詞b_us` | `pack11d/FK025台詞b_us.webp` |
| `FK029台詞d_us` | `pack11d/FK029台詞d_us.webp` |
| `bad_end_us` | `pack11d/bad_end_us.webp` |
| `dead_end` | `pack11d/dead_end.webp` |
| `exit_end_us` | `pack11d/exit_end_us.webp` |
| `jj_account_us` | `pack11d/jj_account_us.webp` |
| `jj_back_us` | `pack11d/jj_back_us.webp` |
| `jj_ema_us` | `pack11d/jj_ema_us.webp` |
| `jj_emabg夕_us` | `pack11d/jj_emabg夕_us.webp` |
| `jj_emabg夜_us` | `pack11d/jj_emabg夜_us.webp` |
| `jj_emabg早朝_us` | `pack11d/jj_emabg早朝_us.webp` |
| `jj_emabg昼_us` | `pack11d/jj_emabg昼_us.webp` |
| `jj_emabg朝_us` | `pack11d/jj_emabg朝_us.webp` |
| `jj_money_us` | `pack11d/jj_money_us.webp` |
| `jj_omikuji_us` | `pack11d/jj_omikuji_us.webp` |
| `jj_ret_us` | `pack11d/jj_ret_us.webp` |
| `jj_yen_us` | `pack11d/jj_yen_us.webp` |
| `jj_中_us` | `pack11d/jj_中_us.webp` |
| `jj_凶_us` | `pack11d/jj_凶_us.webp` |
| `jj_吉_us` | `pack11d/jj_吉_us.webp` |
| `jj_大_us` | `pack11d/jj_大_us.webp` |
| `jj_小_us` | `pack11d/jj_小_us.webp` |
| `jj_御神籤結果中吉_us` | `pack11d/jj_御神籤結果中吉_us.webp` |
| `jj_御神籤結果凶_us` | `pack11d/jj_御神籤結果凶_us.webp` |
| `jj_御神籤結果吉_us` | `pack11d/jj_御神籤結果吉_us.webp` |
| `jj_御神籤結果大凶_us` | `pack11d/jj_御神籤結果大凶_us.webp` |
| `jj_御神籤結果大吉_us` | `pack11d/jj_御神籤結果大吉_us.webp` |
| `jj_御神籤結果小吉_us` | `pack11d/jj_御神籤結果小吉_us.webp` |
| `jj_御神籤結果末吉_us` | `pack11d/jj_御神籤結果末吉_us.webp` |
| `jj_末_us` | `pack11d/jj_末_us.webp` |
| `last` | `pack11d/last.webp` |
| `next01_us` | `pack11d/next01_us.webp` |
| `next02_us` | `pack11d/next02_us.webp` |
| `next03_us` | `pack11d/next03_us.webp` |
| `next04_us` | `pack11d/next04_us.webp` |
| `next05_us` | `pack11d/next05_us.webp` |
| `next06_us` | `pack11d/next06_us.webp` |
| `next07_us` | `pack11d/next07_us.webp` |
| `next08_us` | `pack11d/next08_us.webp` |
| `クイズ鬼不正解_us` | `pack11d/クイズ鬼不正解_us.webp` |
| `クイズ鬼正解_us` | `pack11d/クイズ鬼正解_us.webp` |
| `ジャプニカ暗殺帳(士郎版)_us` | `pack11d/ジャプニカ暗殺帳(士郎版)_us.webp` |
| `ジャプニカ暗殺帳(慎二版)_us` | `pack11d/ジャプニカ暗殺帳(慎二版)_us.webp` |
| `冒頭導入部分_us` | `pack11d/冒頭導入部分_us.webp` |
| `凛メモ字幕_us` | `pack11d/凛メモ字幕_us.webp` |
| `怨嗟02_us` | `pack11d/怨嗟02_us.webp` |
| `怨嗟03_us` | `pack11d/怨嗟03_us.webp` |
| `怨嗟04_us` | `pack11d/怨嗟04_us.webp` |
| `怨嗟05_us` | `pack11d/怨嗟05_us.webp` |
| `怨嗟07_us` | `pack11d/怨嗟07_us.webp` |
| `氷室恋愛探偵01_us` | `pack11d/氷室恋愛探偵01_us.webp` |
| `氷室恋愛探偵01end_us` | `pack11d/氷室恋愛探偵01end_us.webp` |
| `氷室恋愛探偵02_us` | `pack11d/氷室恋愛探偵02_us.webp` |
| `氷室恋愛探偵02end_us` | `pack11d/氷室恋愛探偵02end_us.webp` |
| `氷室恋愛探偵03_us` | `pack11d/氷室恋愛探偵03_us.webp` |
| `氷室恋愛探偵03end_us` | `pack11d/氷室恋愛探偵03end_us.webp` |

### Evidências e encerramento da leva

Pasta de apoio: `C:/Users/Thiago/.codex/visualizations/2026/11/05/01a1ac56-1f6b-7422-a08c-bc9035480780/fha-calibracao/fase_7`. Índice: `comparacoes_fase_7.html`. Registros: `inventario.json`, `estado_inicial.json`, `referencias.json`, `parametros.json`, `parametros_*.json`, `fontes_*.json`, `layout_repeticoes.json`, `auditoria_pre_exportacao.json`, `auditoria_elementos_preservados.json`, `manifesto.json`, `validacao_final.txt` e `resultado_final.json`.

A edição dos arquivos desta leva está concluída. Compilação e teste no jogo permanecem etapas posteriores. O hanafuda continua fora desta leva.

<!-- FASE_7_FIM -->

<!-- FASE_6_INICIO -->
## Histórico — fase 6 concluída em 06/11/2026

**Escopo autorizado:** 46 textos de cena de `pack11d`, com a grafia **Artoria** confirmada pelo dono do projeto.

**968 arquivos prontos, 968 OK e zero com problema.** Foram acrescentados **46 arquivos**. Restam **97 arquivos com edição necessária**: 96 em `pack11d` e um em `pack10d`. A lista bruta do validador contém 100 faltantes, incluindo as três variantes de LOG já dispensadas.

Os **1.068 originais**, os **922 arquivos anteriormente prontos** e a **planilha** foram preservados: **1.991 hashes iguais** aos do início da fase. Nenhum arquivo anterior foi substituído.

### Artoria

Aplicado **Senhorita Artoria, vinda da Bretanha** em `pack11d/093_セイバテロップ_us.webp`, conforme a linha 861 da planilha. A coluna Sugestão PT-BR já continha essa grafia; não foi necessário alterar a planilha. O nome japonês do arquivo foi preservado.

### Composição e efeitos

- Canvas e modo RGBA iguais aos originais; fundos transparentes. Todos estes arquivos existem em uma única resolução e foram redesenhados diretamente nesse tamanho.
- Mantidos os blocos de duas linhas de `076_オルガンtext01`, `05`, `07` e `107_バゼtext03`/`04`. A barra entre as duas frases de 107 na planilha foi tratada como separador de linhas. As palavras e a pontuação foram preservadas.
- As variantes `107_バゼtext02` e `04` mantêm a rotação de 180°.
- Preservadas as maiúsculas e minúsculas alternadas dos seis textos vermelhos `143_天杯text`.
- Os sinais ※ de `023_notice`, `090_釣notice01` e `097_ルヴィアtext01` foram copiados nos mesmos pixels dos originais.
- Mantidas as duas apresentações de fonte na mesma linha das três legendas 093: nome em itálico e origem em corpo menor.
- Cores de preenchimento, contornos e brilhos foram medidas nos originais; as composições foram revistas em fundos claro e escuro. Os efeitos foram ajustados após a primeira comparação visual.
- Não houve reconstrução de CG, papel ou outro fundo artístico. Nenhuma imagem deste lote foi dispensada por texto idêntico ao inglês.

### Fontes e tamanhos

As candidatas foram renderizadas com o inglês e comparadas por sobreposição, incluindo Bembo e as demais fontes do jogo, além das fontes locais. **As fontes abaixo são aproximações; a identidade exata não foi comprovada.**

O desenho usa uma referência de **60 px**, ajustada à altura e à largura medidas em cada original antes de acomodar o PT-BR. A tabela informa a altura final das letras em pixels; `parametros.json` guarda fonte, espessura, espaçamento, escala, tamanho relativo e caixa de cada trecho.

| Família | Fontes utilizadas | Altura das letras no arquivo |
| --- | --- | ---: |
| 023 | georgia.ttf | 28 px |
| 070 | georgia.ttf | 49 px |
| 074 | georgia.ttf, georgiab.ttf | 36–94 px |
| 076 | georgiab.ttf | 26–38 px |
| 088 | FOT-TsukuMinPr6N-B.otf | 33–45 px |
| 090 | FOT-UDKakugo_LargePr6-DB.otf | 30 px |
| 093 | FOT-UDKakugo_LargePr6-DB.otf, arialbi.ttf, calibrib.ttf, calibriz.ttf | 33–60 px |
| 097 | ariali.ttf | 36 px |
| 100 | GARA.TTF | 52 px |
| 107 | cambria.ttc | 41–42 px |
| 136 | FOT-TsukuMinPr6N-B.otf | 57 px |
| 143 claro | cambria.ttc | 34–45 px |
| 143 vermelho | georgiai.ttf, timesi.ttf | 35–52 px |
| 147 | georgia.ttf | 31 px |

### Acomodação dos textos

O espaçamento foi reduzido antes do corpo quando necessário. Nos trechos em que acentos ou texto mais longo exigiram redução adicional, o corpo foi reduzido proporcionalmente. Não foi acrescentada linha a imagens de uma linha. As mudanças de quebra em 076 mantêm os dois blocos do original.

| Imagem | Menor tamanho relativo à base calibrada |
| --- | ---: |
| `023_notice_us` | 99.5% |
| `070_銀音色text2_us` | 85.3% |
| `070_銀音色text_us` | 86.8% |
| `074_アンリtext01_us` | 87.7% |
| `074_アンリtext02_us` | 70.0% |
| `074_アンリtext03_us` | 94.1% |
| `074_アンリtext04_us` | 86.4% |
| `074_アンリtext05_us` | 84.9% |
| `074_アンリtext07_us` | 72.8% |
| `074_アンリtext08_us` | 93.2% |
| `076_オルガンtext02_us` | 79.0% |
| `076_オルガンtext03_us` | 90.2% |
| `076_オルガンtext04_us` | 80.5% |
| `076_オルガンtext06_us` | 83.1% |
| `088_キャスターtext03_us` | 72.0% |
| `088_キャスターtext04_us` | 77.8% |
| `088_キャスターtext05_us` | 84.0% |
| `088_キャスターtext06_us` | 78.0% |
| `090_釣notice01_us` | 83.6% |
| `093_セイバテロップ_us` | 81.3% |
| `093_桜テロップ_us` | 87.9% |
| `097_ルヴィアtext01_us` | 84.3% |
| `107_バゼtext01_us` | 80.6% |
| `107_バゼtext02_us` | 80.6% |
| `136_冒頭05text01_us` | 96.7% |
| `143_カレン06text01_us` | 97.3% |
| `143_カレン06text02_us` | 87.5% |
| `143_カレン06text03_us` | 98.4% |
| `143_天杯text03_us` | 81.9% |
| `143_天杯text06_us` | 79.5% |
| `147_バゼtext01_us` | 77.1% |

### Conferência

- 46 WebP sem perda, com os mesmos nomes, caminhos, dimensões e modos de cor dos originais. Sem EXIF/XMP adicionais; o bloco PSAI não foi recriado, conforme o prompt.
- Reabertura dos 46 arquivos com igualdade dos pixels em relação ao mestre antes da gravação.
- Texto renderizado conferido contra o inventário da coluna aprovada; glifos e acentos presentes nas fontes; caixas das letras dentro do canvas.
- 12 pranchas individuais por grupo, com as 46 imagens em tamanho nativo, original e PT-BR, sobre fundos claro e escuro. As versões finais das imagens ajustadas foram revistas novamente.
- Validador: **968 conferidos, 968 OK, zero com problema**.
- Hashes: originais, arquivos anteriormente prontos e planilha preservados.
- Não houve compilação nem teste dentro do jogo. Scripts, pastas extraídas, hanafuda e Git não foram utilizados para alterações.

### Imagem → arquivo gerado

Todos em `Imagens/imagens_prontas`, no caminho relativo abaixo.

| Imagem-base | Arquivo desta fase |
| --- | --- |
| `023_notice_us` | `pack11d/023_notice_us.webp` |
| `070_銀音色text2_us` | `pack11d/070_銀音色text2_us.webp` |
| `070_銀音色text_us` | `pack11d/070_銀音色text_us.webp` |
| `074_アンリtext01_us` | `pack11d/074_アンリtext01_us.webp` |
| `074_アンリtext02_us` | `pack11d/074_アンリtext02_us.webp` |
| `074_アンリtext03_us` | `pack11d/074_アンリtext03_us.webp` |
| `074_アンリtext04_us` | `pack11d/074_アンリtext04_us.webp` |
| `074_アンリtext05_us` | `pack11d/074_アンリtext05_us.webp` |
| `074_アンリtext07_us` | `pack11d/074_アンリtext07_us.webp` |
| `074_アンリtext08_us` | `pack11d/074_アンリtext08_us.webp` |
| `076_オルガンtext01_us` | `pack11d/076_オルガンtext01_us.webp` |
| `076_オルガンtext02_us` | `pack11d/076_オルガンtext02_us.webp` |
| `076_オルガンtext03_us` | `pack11d/076_オルガンtext03_us.webp` |
| `076_オルガンtext04_us` | `pack11d/076_オルガンtext04_us.webp` |
| `076_オルガンtext05_us` | `pack11d/076_オルガンtext05_us.webp` |
| `076_オルガンtext06_us` | `pack11d/076_オルガンtext06_us.webp` |
| `076_オルガンtext07_us` | `pack11d/076_オルガンtext07_us.webp` |
| `088_キャスターtext03_us` | `pack11d/088_キャスターtext03_us.webp` |
| `088_キャスターtext04_us` | `pack11d/088_キャスターtext04_us.webp` |
| `088_キャスターtext05_us` | `pack11d/088_キャスターtext05_us.webp` |
| `088_キャスターtext06_us` | `pack11d/088_キャスターtext06_us.webp` |
| `090_釣notice01_us` | `pack11d/090_釣notice01_us.webp` |
| `093_イリヤテロップ_us` | `pack11d/093_イリヤテロップ_us.webp` |
| `093_セイバテロップ_us` | `pack11d/093_セイバテロップ_us.webp` |
| `093_桜テロップ_us` | `pack11d/093_桜テロップ_us.webp` |
| `097_ルヴィアtext01_us` | `pack11d/097_ルヴィアtext01_us.webp` |
| `100_ミミックtext01_us` | `pack11d/100_ミミックtext01_us.webp` |
| `100_ミミックtext02_us` | `pack11d/100_ミミックtext02_us.webp` |
| `107_バゼtext01_us` | `pack11d/107_バゼtext01_us.webp` |
| `107_バゼtext02_us` | `pack11d/107_バゼtext02_us.webp` |
| `107_バゼtext03_us` | `pack11d/107_バゼtext03_us.webp` |
| `107_バゼtext04_us` | `pack11d/107_バゼtext04_us.webp` |
| `136_冒頭05text01_us` | `pack11d/136_冒頭05text01_us.webp` |
| `143_カレン06text01_us` | `pack11d/143_カレン06text01_us.webp` |
| `143_カレン06text02_us` | `pack11d/143_カレン06text02_us.webp` |
| `143_カレン06text03_us` | `pack11d/143_カレン06text03_us.webp` |
| `143_カレン06text04_us` | `pack11d/143_カレン06text04_us.webp` |
| `143_カレン06text05_us` | `pack11d/143_カレン06text05_us.webp` |
| `143_カレン06text06_us` | `pack11d/143_カレン06text06_us.webp` |
| `143_天杯text01_us` | `pack11d/143_天杯text01_us.webp` |
| `143_天杯text02_us` | `pack11d/143_天杯text02_us.webp` |
| `143_天杯text03_us` | `pack11d/143_天杯text03_us.webp` |
| `143_天杯text04_us` | `pack11d/143_天杯text04_us.webp` |
| `143_天杯text05_us` | `pack11d/143_天杯text05_us.webp` |
| `143_天杯text06_us` | `pack11d/143_天杯text06_us.webp` |
| `147_バゼtext01_us` | `pack11d/147_バゼtext01_us.webp` |

### Evidências e próxima etapa

Pasta de apoio: `C:/Users/Thiago/.codex/visualizations/2026/11/05/01a1ac56-1f6b-7422-a08c-bc9035480780/fha-calibracao/fase_6`. Índice: `comparacoes_fase_6.html`. Registros: `inventario.json`, `estado_inicial.json`, `busca_fontes.json`, `ajustes_fontes.json`, `parametros.json`, `manifesto.json`, `validacao_final.txt` e `resultado_final.json`.

Próxima etapa, fase 7: os 97 arquivos restantes com edição necessária, incluindo cartas, bilhetes, efeitos, cartões e a caixa de nome de `pack10d`. A relação exata está em `resultado_final.json` e `validacao_final.txt`.

<!-- FASE_6_FIM -->

<!-- FASE_5_INICIO -->
## Histórico — fase 5 concluída em 06/11/2026

**Escopo autorizado:** `guide` e `60_endroll`, com a retradução da frase de despedida solicitada durante esta fase.

| Pasta | Imagens-base | Arquivos novos |
| --- | ---: | ---: |
| guide | 16 | 48 |
| 60_endroll | 6 | 16 |
| **Total da fase 5** | **22** | **64** |

**922 arquivos prontos, 922 OK e zero com problema.** Não restam pendências em guide ou 60_endroll. Restam **143 arquivos com edição necessária**: 142 em pack11d e um em pack10d. A lista bruta do validador contém 146 faltantes, pois inclui as três variantes de LOG dispensadas anteriormente.

Os **1.068 originais** e os **858 arquivos anteriormente prontos** foram preservados, com os **1.926 hashes iguais** aos do início da fase. A única alteração autorizada em arquivo anterior foi **Traduções!F59** na planilha. A conferência compara os 1.927 registros iniciais com essa exceção explícita.

### Retradução aplicada

**Obrigado. E aqui nos despedimos... desta ataraxia vazia.**

Aplicada em `149_edtext05.webp` e nas três resoluções de `sbed_font05`. O traço que precede a frase permanece na posição e nos pixels do original. O texto da planilha foi atualizado somente em **Traduções!F59**. A comparação de todas as células confirmou uma única mudança de valor; todas as partes do XLSX, exceto o XML da aba que contém essa célula, permaneceram iguais. O estilo original da célula também foi preservado. Registros: `alteracoes_autorizadas.json`, `linha_antes.png` e `linha_depois.png`.

### Guias de controles

- Foram traduzidos os guias de teclado/mouse, Switch em modo portátil, Joy-Con Grip, controle Pro, Joy-Con horizontal, Joy-Cons separados e comandos com uma mão. As variantes azuis e rosas mantêm suas próprias cores.
- As posições foram definidas no layout do FHA. O FSN possui comandos e linhas adicionais; seus quadros completos não foram transplantados para o FHA.
- As faixas lisas e seus degradês foram recompostos apenas nos retângulos dos textos, usando uma linha intacta da mesma faixa. Desenhos dos controles, botões, setas, sinais de igualdade, teclas, logotipos e demais pixels fora das áreas de edição foram mantidos.
- A preservação foi conferida também nas resoluções 2x/1x: depois da redução do mestre 4x com alfa pré-multiplicado e LANCZOS, as áreas externas à edição receberam os pixels do original da própria resolução.
- Segurar e alternar loop usam a cor do rótulo correspondente no original: azul ou rosa. MENU e Mouse permanecem como definidos na planilha.
- `guide_08_us.webp`, já pronto do FSN e existente somente em 1x, não foi alterado. Não foi criada resolução inexistente.

### Fontes e acomodação

As candidatas foram comparadas por sobreposição com o inglês. **As escolhas são aproximações; a identidade exata das fontes não foi comprovada.** Os tamanhos abaixo são nominais, com ocupação e linha de base calibradas sobre os originais.

| Família | Fonte | Tamanho nominal no mestre |
| --- | --- | --- |
| Diagramas dos guias | FOT-UDKakugo Large Pr6 DB | 60 px; afinamento de 0,5 px e espaçamento de −1 px |
| Tabelas de controles | FOT-UDKakugo Large Pr6 DB | 45 px; afinamento de 0,25 px |
| Cabeçalhos dos guias | FOT-UDKakugo Large Pr6 DB | 54 px nos títulos; 36 px nas colunas |
| sbed_font01 a 05 | Garamond Bold | 64 px; espaçamento de 1 px antes dos ajustes |
| 149_edtext05 | Times New Roman Regular | 42 px de base, no canvas nativo de 820 × 40 |

Nos trechos longos, foi reduzido o espaçamento antes do tamanho da fonte. As legendas de duas linhas continuam no bloco correspondente. A tabela abaixo registra o menor tamanho relativo entre as variantes da mesma imagem-base; o detalhamento por rótulo e estado está em `parametros.json`.

| Imagem-base | Texto | Tamanho relativo à base |
| --- | --- | ---: |
| `149_edtext05` | Obrigado. E aqui nos despedimos... desta ataraxia vazia. | 83,3% |
| `sbed_font05` | Obrigado. E aqui nos despedimos... desta ataraxia vazia. | 81,2% |
| `guide_02_us` | Retroceder Rápido | 96,7% |
| `guide_02_us` | Segurar | 96,7% |
| `guide_02_us` | Avançar Texto, Confirmar | 98,3% |
| `guide_02_us` | Tocar na Tela : Avançar Texto, Confirmar | 95,0% |
| `guide_03_us` | Retroceder Rápido | 96,7% |
| `guide_03_us` | Segurar | 96,7% |
| `guide_04_us` | Retroceder Rápido | 96,7% |
| `guide_04_us` | Segurar | 96,7% |
| `guide_05_us` | Retroceder Rápido | 96,7% |
| `guide_05_us` | Segurar | 96,7% |
| `guide_05_us` | Ocultar Janela de Texto, | 93,3% |
| `guide_05_us` | Cancelar, Parar Modo Auto | 93,3% |
| `guide_06_us` | Retroceder Rápido | 96,7% |
| `guide_06_us` | Segurar | 96,7% |
| `guide_06_us` | Ocultar Janela de Texto, | 93,3% |
| `guide_06_us` | Cancelar, Parar Modo Auto | 93,3% |
| `guide_07_us` | Retroceder Rápido | 95,0% |
| `guide_07_us` | Segurar | 95,0% |
| `guide_09_us` | Ocultar Janela de Texto, Cancelar, Parar Modo Auto | 95,6% |
| `guide_09_us` | Segurar | 73,3% |

A maior redução ocorre em Segurar entre botões e sinais de igualdade de guide_09: esses ícones foram preservados em suas posições. Nos demais casos, os ajustes são menores e mantêm a legenda dentro de sua faixa. As frases sbed_font01 a 04 conservam o alinhamento à direita do original; sbed_font05 e 149_edtext05 acomodam o novo texto depois do traço preservado.

### Referências e observações

- A planilha não lista Teclado e as cinco descrições de gestos da seção de mouse de guide_01. Foram reutilizados os textos existentes no guia FSN traduzido, disponível em `FSN/patch00mextraido/root/data/fuzz/release/root/resident/gui/textures/guide/guide_01_us.png`: Mover cursor para o rodapé; Arrastar da Esquerda para a Direita; Arrastar da Direita para a Esquerda; Arrastar do centro para a direita; Arrastar do centro para a esquerda. Controle coincide com o rótulo aprovado em guide_09.
- Segurar em guide_01 e na variante rosa de guide_05, ausente das linhas correspondentes da planilha, reutiliza o termo aprovado nas outras telas da mesma família.
- A planilha inclui Mudar Página, Abrir menu Salvar e Abrir menu Carregar para guide_01, herdados do FSN. Esses comandos não aparecem no quadro original do FHA e não foram acrescentados.
- Não houve reconstrução de CG ou de arte dos controles; apenas recomposição de fundos lisos sob as letras. Nenhuma imagem-base foi dispensada por todos os seus textos serem iguais ao inglês.
- As divergências herdadas das versões FSN registradas nas fases anteriores permanecem. Não houve recompilação, teste dentro do jogo ou uso de Git. Scripts do jogo, pastas extraídas e hanafuda não foram alterados.

### Conferência

- **64 arquivos novos**, nos nomes, caminhos, dimensões e modos de cor dos originais. WebP sem perda, sem EXIF/XMP adicionais; a reabertura de cada arquivo confirmou igualdade dos pixels com a composição antes da gravação.
- **922 conferidos, 922 OK, zero com problema** pelo validador. Nenhum arquivo ausente nas duas pastas desta fase.
- Conferência dos hashes de originais e arquivos anteriormente prontos sem alteração; mudança isolada de F59 conferida em todas as células e partes do XLSX.
- Conferência de glifos, caixas de texto, preservação fora das edições nas três resoluções e ausência de legendas coloridas inglesas fora das áreas tratadas.
- **22 folhas individuais** de original/PT-BR em tamanho nativo, sobre fundos claro e escuro, nas resoluções disponíveis; seis folhas gerais e seis folhas de detalhes de resoluções.

Pasta de apoio: `C:/Users/Thiago/.codex/visualizations/2026/11/05/01a1ac56-1f6b-7422-a08c-bc9035480780/fha-calibracao/fase_5`. Índice: `comparacoes_fase_5.html`. Registros: `inventario.json`, `estado_inicial.json`, `parametros.json`, `calibracao_fontes.json`, `auditoria.json`, `auditoria_legendas_coloridas.json`, `arquivos_gerados.json`, `hashes_gerados.json`, `validacao_final.txt` e `resultado_final.json`.

### Imagem → arquivos gerados

| Imagem-base | Arquivos desta fase |
| --- | --- |
| `60_endroll/149_edtext05` | `pack00m_gui/60_endroll/149_edtext05.webp` |
| `60_endroll/sbed_font05` | `pack00d_gui/60_endroll/sbed_font05@4x.webp`<br>`pack00m_gui/60_endroll/sbed_font05@2x.webp`<br>`pack00m_gui/60_endroll/sbed_font05.webp` |
| `60_endroll/sbed_font01` | `pack00d_gui/60_endroll/sbed_font01@4x.webp`<br>`pack00m_gui/60_endroll/sbed_font01@2x.webp`<br>`pack00m_gui/60_endroll/sbed_font01.webp` |
| `60_endroll/sbed_font02` | `pack00d_gui/60_endroll/sbed_font02@4x.webp`<br>`pack00m_gui/60_endroll/sbed_font02@2x.webp`<br>`pack00m_gui/60_endroll/sbed_font02.webp` |
| `60_endroll/sbed_font03` | `pack00d_gui/60_endroll/sbed_font03@4x.webp`<br>`pack00m_gui/60_endroll/sbed_font03@2x.webp`<br>`pack00m_gui/60_endroll/sbed_font03.webp` |
| `60_endroll/sbed_font04` | `pack00d_gui/60_endroll/sbed_font04@4x.webp`<br>`pack00m_gui/60_endroll/sbed_font04@2x.webp`<br>`pack00m_gui/60_endroll/sbed_font04.webp` |
| `guide/guide_01_us` | `pack00d_gui/guide/guide_01_us@4x.webp`<br>`pack00m_gui/guide/guide_01_us@2x.webp`<br>`pack00m_gui/guide/guide_01_us.webp` |
| `guide/guide_01_us@v1` | `pack00d_gui/guide/guide_01_us@v1@4x.webp`<br>`pack00m_gui/guide/guide_01_us@v1@2x.webp`<br>`pack00m_gui/guide/guide_01_us@v1.webp` |
| `guide/guide_02_us` | `pack00d_gui/guide/guide_02_us@4x.webp`<br>`pack00m_gui/guide/guide_02_us@2x.webp`<br>`pack00m_gui/guide/guide_02_us.webp` |
| `guide/guide_02_us@v1` | `pack00d_gui/guide/guide_02_us@v1@4x.webp`<br>`pack00m_gui/guide/guide_02_us@v1@2x.webp`<br>`pack00m_gui/guide/guide_02_us@v1.webp` |
| `guide/guide_03_us` | `pack00d_gui/guide/guide_03_us@4x.webp`<br>`pack00m_gui/guide/guide_03_us@2x.webp`<br>`pack00m_gui/guide/guide_03_us.webp` |
| `guide/guide_03_us@v1` | `pack00d_gui/guide/guide_03_us@v1@4x.webp`<br>`pack00m_gui/guide/guide_03_us@v1@2x.webp`<br>`pack00m_gui/guide/guide_03_us@v1.webp` |
| `guide/guide_04_us` | `pack00d_gui/guide/guide_04_us@4x.webp`<br>`pack00m_gui/guide/guide_04_us@2x.webp`<br>`pack00m_gui/guide/guide_04_us.webp` |
| `guide/guide_04_us@v1` | `pack00d_gui/guide/guide_04_us@v1@4x.webp`<br>`pack00m_gui/guide/guide_04_us@v1@2x.webp`<br>`pack00m_gui/guide/guide_04_us@v1.webp` |
| `guide/guide_05_us` | `pack00d_gui/guide/guide_05_us@4x.webp`<br>`pack00m_gui/guide/guide_05_us@2x.webp`<br>`pack00m_gui/guide/guide_05_us.webp` |
| `guide/guide_06_us` | `pack00d_gui/guide/guide_06_us@4x.webp`<br>`pack00m_gui/guide/guide_06_us@2x.webp`<br>`pack00m_gui/guide/guide_06_us.webp` |
| `guide/guide_06_us@v1` | `pack00d_gui/guide/guide_06_us@v1@4x.webp`<br>`pack00m_gui/guide/guide_06_us@v1@2x.webp`<br>`pack00m_gui/guide/guide_06_us@v1.webp` |
| `guide/guide_05_us@v1` | `pack00d_gui/guide/guide_05_us@v1@4x.webp`<br>`pack00m_gui/guide/guide_05_us@v1@2x.webp`<br>`pack00m_gui/guide/guide_05_us@v1.webp` |
| `guide/guide_07_us` | `pack00d_gui/guide/guide_07_us@4x.webp`<br>`pack00m_gui/guide/guide_07_us@2x.webp`<br>`pack00m_gui/guide/guide_07_us.webp` |
| `guide/guide_07_us@v1` | `pack00d_gui/guide/guide_07_us@v1@4x.webp`<br>`pack00m_gui/guide/guide_07_us@v1@2x.webp`<br>`pack00m_gui/guide/guide_07_us@v1.webp` |
| `guide/guide_09_us` | `pack00d_gui/guide/guide_09_us@4x.webp`<br>`pack00m_gui/guide/guide_09_us@2x.webp`<br>`pack00m_gui/guide/guide_09_us.webp` |
| `guide/guide_09_us@v1` | `pack00d_gui/guide/guide_09_us@v1@4x.webp`<br>`pack00m_gui/guide/guide_09_us@v1@2x.webp`<br>`pack00m_gui/guide/guide_09_us@v1.webp` |

### Próxima etapa

Fase 6: textos de cena do pack11d. As etapas restantes desta leva somam 143 arquivos com edição necessária.

<!-- FASE_5_FIM -->

<!-- FASE_4_INICIO -->
## Histórico — fase 4 concluída em 05/11/2026

**Escopo autorizado:** `imgtext` e `flaglist`. Foram preparados 49 mestres em 4x. A coluna Sugestão PT-BR foi usada sem retradução; a planilha foi apenas lida.

| Pasta | Imagens-base exportadas | Arquivos novos |
| --- | ---: | ---: |
| imgtext | 45 | 119 |
| flaglist | 4 | 12 |
| **Total da fase 4** | **49** | **131** |

O projeto contém **858 arquivos prontos**, todos conferidos pelo validador: **zero com problema**. Restam **207 arquivos com edição necessária**; a relação bruta inclui mais três variantes de LOG dispensadas anteriormente.

Os **1.068 originais**, os **727 arquivos anteriormente prontos** e a planilha foram preservados, com conferência dos **1.796 hashes** do início da fase. Nenhum arquivo anterior foi sobrescrito.

### Conteúdo e composição

- **Cenas:** 13 listas, cada uma nos estados normal e selecionado. A montagem segue as linhas físicas do atlas, incluindo títulos repetidos que aparecem uma única vez na planilha. As ocorrências repetidas de Time Passes, His Shore e Murderer at the Empty Mansion receberam o mesmo texto aprovado em suas próprias posições.
- **Galeria (`pictxt`):** hollow ataraxia permanece intacto; Outros e Especial substituem seus rótulos nas três linhas de 168 pixels, mantendo o espaço transparente inferior do atlas.
- **Categorias (`scenetab`):** datas no formato aprovado, lugares e categorias traduzidos. Guerra do Santo Graal Noturna usa duas linhas dentro da própria célula.
- **Flags (`flisttxt`):** 50 células, distribuídas em seis colunas, nos três estados de cor. Cada título permanece na célula correspondente; o texto pode ocupar uma ou duas linhas.
- **Músicas:** duas colunas, com 22 itens à esquerda e 16 à direita. Os nomes que a planilha mantém em inglês ou romanizados foram conservados pixel a pixel nos mestres.
- **Glossário (`libtxt`):** 53 células em cada uma das duas páginas, nos dois estados. Os textos e as quebras das referências FSN 2x foram transcritos e redesenhados em 4x; as entradas presentes na planilha foram cruzadas com essas referências. Os textos dessas entradas coincidem, desconsiderando apenas a disposição das quebras.
- **Armas:** rótulos redesenhados em 4x a partir da referência FSN. A última célula conserva as duas linhas Espada Dourada / da Vitória Garantida.
- **Configuração:** Texto, Som e Salvamento, incluindo estados neutro, azul e rosa.
- **Selos:** NOVO em quatro variantes, com degradês próprios e brilho mais intenso em icon_new2.

As setas foram copiadas dos originais 4x sem alteração; os trechos de texto dispensados permaneceram intactos. Os mestres foram desenhados pelas fontes. As novas versões 2x/1x foram reduzidas com LANCZOS e alfa pré-multiplicado para as dimensões exatas de cada original. Não houve ampliação de referência 2x nem reconstrução de CG ou fundo.

### Fontes e acomodação

As candidatas foram sobrepostas ao texto original ou à referência FSN. **As fontes utilizadas são aproximações: a identidade exata não foi comprovada.** Os tamanhos são nominais; a ocupação e a posição foram calibradas conforme a família.

| Família | Fonte | Tamanho nominal no mestre |
| --- | --- | --- |
| scene | Calibri Regular | 64 px; afinamento de 0,25 px e espaçamento de −1 px |
| mustxt | Jost, peso padrão | 64 px; afinamento de 0,25 px e espaçamento de −1 px |
| flisttxt | Bembo Book MT Pro Bold | 40 px; espaçamento de −1 px |
| libtxt / weptxt | Segoe UI Regular | 56 px; posições e ocupação da referência 2x ×2 |
| contxt | Humnst777 BT Roman | 56 px; gabarito FSN 2x ×2 |
| pictxt / scenetab | FOT-UDKakugo Large Pr6 Bold | 56 px; scenetab com afinamento de 0,25 px |
| icon_new* | Arial Bold | 42 px; ocupação ajustada ao selo |

Nos títulos que ultrapassariam a célula, o espaçamento foi reduzido antes da fonte. Casos com redução adicional de tamanho (mesma composição nos estados correspondentes):

| Imagem-base | Texto | Tamanho em relação à base |
| --- | --- | ---: |
| `flisttxt01_us` | Vingança da Limpeza da Mansão | 95.0% |
| `flisttxt01_us` | Carta da Associação dos Magos | 95.0% |
| `flisttxt01_us` | Histórias de Viagem de Londres | 97.5% |
| `scene07_us` | Grande Destruição! A Lenda do Autocrata Ressuscitado Gravada na Litografia Antiga! | 79.7% |
| `weptxt01_us` | Alabarda Incinerante do Céu | 96.4% |

As quebras acrescentadas aos títulos das flags mantêm o limite de duas linhas. As demais listas mantêm uma linha por título, exceto as categorias e os verbetes que já possuem composição de várias linhas. Os parâmetros completos estão em `parametros.json` e `estilos.json`.

### Divergências e textos complementares

- A versão 4x de weptxt aplica **Alabarda Incinerante do Céu**, conforme a planilha; as 1x/2x anteriores mantêm **Alabarda Queima-Céu**. Elas foram preservadas como exigido. Essa diferença textual entre resoluções permanece registrada.
- Em scene11, All Clear (1)/(3) reutiliza Tudo Concluído, mantendo os números originais; Dead Bridge (I) reutiliza Ponte Morta, mantendo o sufixo (I). São variações de rótulos aprovados na planilha, sem nova redação.
- Os cinco nomes Caren I–V (Anra Mainiiu), ausentes da planilha, foram mantidos como nomes próprios.
- Complementos definidos pelo usuário no chat: Silver Thread → Fio Prateado; Sister’s Summer (Apple) → O Verão das Irmãs (Maçã). A planilha não foi alterada.
- As divergências herdadas do FSN registradas nas fases anteriores permanecem sem alteração.
- Nenhuma imagem-base desta fase foi dispensada por ter todos os textos iguais. Células com nomes e textos idênticos foram conservadas dentro dos atlas.
- Não houve teste dentro do jogo, recompilação ou uso de Git. Scripts do jogo, fontes extraídas, originais e hanafuda não foram alterados.

### Conferência e registros

- Validação estrutural: **858 OK, zero com problema**; dimensões, modo de cor, WebP sem perda, EXIF/XMP e correspondência entre a imagem antes/depois da gravação conferidos.
- Conferência dos 1.796 hashes anteriores sem alteração.
- Verificação de setas e células preservadas, glifos disponíveis nas fontes, limites das caixas de texto e cobertura de todas as células com pixels visíveis.
- 49 folhas individuais de comparação original/PT-BR nas resoluções nativas disponíveis, sobre fundos claro e escuro; folhas adicionais por célula e nove folhas de resoluções.

Pasta de apoio: `C:/Users/Thiago/.codex/visualizations/2026/11/05/01a1ac56-1f6b-7422-a08c-bc9035480780/fha-calibracao/fase_4`. Índice: `comparacoes_fase_4.html`. Registros: `inventario.json`, `estado_inicial.json`, `parametros.json`, `estilos.json`, `arquivos_gerados.json`, `auditoria_celulas_glifos.json`, `validacao_final.txt` e `resultado_final.json`.

### Imagem → arquivos gerados

| Imagem-base | Arquivos desta fase |
| --- | --- |
| `flaglist/icon_new1` | `pack00d_gui/flaglist/icon_new1@4x.webp`<br>`pack00m_gui/flaglist/icon_new1@2x.webp`<br>`pack00m_gui/flaglist/icon_new1.webp` |
| `flaglist/icon_new1@v1` | `pack00d_gui/flaglist/icon_new1@v1@4x.webp`<br>`pack00m_gui/flaglist/icon_new1@v1@2x.webp`<br>`pack00m_gui/flaglist/icon_new1@v1.webp` |
| `flaglist/icon_new2` | `pack00d_gui/flaglist/icon_new2@4x.webp`<br>`pack00m_gui/flaglist/icon_new2@2x.webp`<br>`pack00m_gui/flaglist/icon_new2.webp` |
| `flaglist/icon_new2@v1` | `pack00d_gui/flaglist/icon_new2@v1@4x.webp`<br>`pack00m_gui/flaglist/icon_new2@v1@2x.webp`<br>`pack00m_gui/flaglist/icon_new2@v1.webp` |
| `imgtext/contxt01_us` | `pack00d_gui/imgtext/contxt01_us@4x.webp` |
| `imgtext/contxt01on_us` | `pack00d_gui/imgtext/contxt01on_us@4x.webp` |
| `imgtext/contxt01_us@v1` | `pack00d_gui/imgtext/contxt01_us@v1@4x.webp`<br>`pack00m_gui/imgtext/contxt01_us@v1@2x.webp`<br>`pack00m_gui/imgtext/contxt01_us@v1.webp` |
| `imgtext/contxt01on_us@v1` | `pack00d_gui/imgtext/contxt01on_us@v1@4x.webp`<br>`pack00m_gui/imgtext/contxt01on_us@v1@2x.webp`<br>`pack00m_gui/imgtext/contxt01on_us@v1.webp` |
| `imgtext/flisttxt01_us` | `pack00d_gui/imgtext/flisttxt01_us@4x.webp`<br>`pack00m_gui/imgtext/flisttxt01_us@2x.webp`<br>`pack00m_gui/imgtext/flisttxt01_us.webp` |
| `imgtext/flisttxt01sel_us` | `pack00d_gui/imgtext/flisttxt01sel_us@4x.webp`<br>`pack00m_gui/imgtext/flisttxt01sel_us@2x.webp`<br>`pack00m_gui/imgtext/flisttxt01sel_us.webp` |
| `imgtext/flisttxt01sel_us@v1` | `pack00d_gui/imgtext/flisttxt01sel_us@v1@4x.webp`<br>`pack00m_gui/imgtext/flisttxt01sel_us@v1@2x.webp`<br>`pack00m_gui/imgtext/flisttxt01sel_us@v1.webp` |
| `imgtext/libtxt01_us` | `pack00d_gui/imgtext/libtxt01_us@4x.webp` |
| `imgtext/libtxt01sel_us` | `pack00d_gui/imgtext/libtxt01sel_us@4x.webp` |
| `imgtext/libtxt02_us` | `pack00d_gui/imgtext/libtxt02_us@4x.webp` |
| `imgtext/libtxt02sel_us` | `pack00d_gui/imgtext/libtxt02sel_us@4x.webp` |
| `imgtext/mustxt_us` | `pack00d_gui/imgtext/mustxt_us@4x.webp`<br>`pack00m_gui/imgtext/mustxt_us@2x.webp`<br>`pack00m_gui/imgtext/mustxt_us.webp` |
| `imgtext/mustxtsel_us` | `pack00d_gui/imgtext/mustxtsel_us@4x.webp`<br>`pack00m_gui/imgtext/mustxtsel_us@2x.webp`<br>`pack00m_gui/imgtext/mustxtsel_us.webp` |
| `imgtext/pictxt01` | `pack00d_gui/imgtext/pictxt01@4x.webp`<br>`pack00m_gui/imgtext/pictxt01@2x.webp`<br>`pack00m_gui/imgtext/pictxt01.webp` |
| `imgtext/pictxt01on` | `pack00d_gui/imgtext/pictxt01on@4x.webp`<br>`pack00m_gui/imgtext/pictxt01on@2x.webp`<br>`pack00m_gui/imgtext/pictxt01on.webp` |
| `imgtext/scene01_us` | `pack00d_gui/imgtext/scene01_us@4x.webp`<br>`pack00m_gui/imgtext/scene01_us@2x.webp`<br>`pack00m_gui/imgtext/scene01_us.webp` |
| `imgtext/scene01sel_us` | `pack00d_gui/imgtext/scene01sel_us@4x.webp`<br>`pack00m_gui/imgtext/scene01sel_us@2x.webp`<br>`pack00m_gui/imgtext/scene01sel_us.webp` |
| `imgtext/scene02_us` | `pack00d_gui/imgtext/scene02_us@4x.webp`<br>`pack00m_gui/imgtext/scene02_us@2x.webp`<br>`pack00m_gui/imgtext/scene02_us.webp` |
| `imgtext/scene02sel_us` | `pack00d_gui/imgtext/scene02sel_us@4x.webp`<br>`pack00m_gui/imgtext/scene02sel_us@2x.webp`<br>`pack00m_gui/imgtext/scene02sel_us.webp` |
| `imgtext/scene03_us` | `pack00d_gui/imgtext/scene03_us@4x.webp`<br>`pack00m_gui/imgtext/scene03_us@2x.webp`<br>`pack00m_gui/imgtext/scene03_us.webp` |
| `imgtext/scene03sel_us` | `pack00d_gui/imgtext/scene03sel_us@4x.webp`<br>`pack00m_gui/imgtext/scene03sel_us@2x.webp`<br>`pack00m_gui/imgtext/scene03sel_us.webp` |
| `imgtext/scene04_us` | `pack00d_gui/imgtext/scene04_us@4x.webp`<br>`pack00m_gui/imgtext/scene04_us@2x.webp`<br>`pack00m_gui/imgtext/scene04_us.webp` |
| `imgtext/scene04sel_us` | `pack00d_gui/imgtext/scene04sel_us@4x.webp`<br>`pack00m_gui/imgtext/scene04sel_us@2x.webp`<br>`pack00m_gui/imgtext/scene04sel_us.webp` |
| `imgtext/scene05_us` | `pack00d_gui/imgtext/scene05_us@4x.webp`<br>`pack00m_gui/imgtext/scene05_us@2x.webp`<br>`pack00m_gui/imgtext/scene05_us.webp` |
| `imgtext/scene05sel_us` | `pack00d_gui/imgtext/scene05sel_us@4x.webp`<br>`pack00m_gui/imgtext/scene05sel_us@2x.webp`<br>`pack00m_gui/imgtext/scene05sel_us.webp` |
| `imgtext/scene06_us` | `pack00d_gui/imgtext/scene06_us@4x.webp`<br>`pack00m_gui/imgtext/scene06_us@2x.webp`<br>`pack00m_gui/imgtext/scene06_us.webp` |
| `imgtext/scene06sel_us` | `pack00d_gui/imgtext/scene06sel_us@4x.webp`<br>`pack00m_gui/imgtext/scene06sel_us@2x.webp`<br>`pack00m_gui/imgtext/scene06sel_us.webp` |
| `imgtext/scene07_us` | `pack00d_gui/imgtext/scene07_us@4x.webp`<br>`pack00m_gui/imgtext/scene07_us@2x.webp`<br>`pack00m_gui/imgtext/scene07_us.webp` |
| `imgtext/scene07sel_us` | `pack00d_gui/imgtext/scene07sel_us@4x.webp`<br>`pack00m_gui/imgtext/scene07sel_us@2x.webp`<br>`pack00m_gui/imgtext/scene07sel_us.webp` |
| `imgtext/scene08_us` | `pack00d_gui/imgtext/scene08_us@4x.webp`<br>`pack00m_gui/imgtext/scene08_us@2x.webp`<br>`pack00m_gui/imgtext/scene08_us.webp` |
| `imgtext/scene08sel_us` | `pack00d_gui/imgtext/scene08sel_us@4x.webp`<br>`pack00m_gui/imgtext/scene08sel_us@2x.webp`<br>`pack00m_gui/imgtext/scene08sel_us.webp` |
| `imgtext/scene09_us` | `pack00d_gui/imgtext/scene09_us@4x.webp`<br>`pack00m_gui/imgtext/scene09_us@2x.webp`<br>`pack00m_gui/imgtext/scene09_us.webp` |
| `imgtext/scene09sel_us` | `pack00d_gui/imgtext/scene09sel_us@4x.webp`<br>`pack00m_gui/imgtext/scene09sel_us@2x.webp`<br>`pack00m_gui/imgtext/scene09sel_us.webp` |
| `imgtext/scene10_us` | `pack00d_gui/imgtext/scene10_us@4x.webp`<br>`pack00m_gui/imgtext/scene10_us@2x.webp`<br>`pack00m_gui/imgtext/scene10_us.webp` |
| `imgtext/scene10sel_us` | `pack00d_gui/imgtext/scene10sel_us@4x.webp`<br>`pack00m_gui/imgtext/scene10sel_us@2x.webp`<br>`pack00m_gui/imgtext/scene10sel_us.webp` |
| `imgtext/scene11_us` | `pack00d_gui/imgtext/scene11_us@4x.webp`<br>`pack00m_gui/imgtext/scene11_us@2x.webp`<br>`pack00m_gui/imgtext/scene11_us.webp` |
| `imgtext/scene11sel_us` | `pack00d_gui/imgtext/scene11sel_us@4x.webp`<br>`pack00m_gui/imgtext/scene11sel_us@2x.webp`<br>`pack00m_gui/imgtext/scene11sel_us.webp` |
| `imgtext/scene12_us` | `pack00d_gui/imgtext/scene12_us@4x.webp`<br>`pack00m_gui/imgtext/scene12_us@2x.webp`<br>`pack00m_gui/imgtext/scene12_us.webp` |
| `imgtext/scene12sel_us` | `pack00d_gui/imgtext/scene12sel_us@4x.webp`<br>`pack00m_gui/imgtext/scene12sel_us@2x.webp`<br>`pack00m_gui/imgtext/scene12sel_us.webp` |
| `imgtext/scene13_us` | `pack00d_gui/imgtext/scene13_us@4x.webp`<br>`pack00m_gui/imgtext/scene13_us@2x.webp`<br>`pack00m_gui/imgtext/scene13_us.webp` |
| `imgtext/scene13sel_us` | `pack00d_gui/imgtext/scene13sel_us@4x.webp`<br>`pack00m_gui/imgtext/scene13sel_us@2x.webp`<br>`pack00m_gui/imgtext/scene13sel_us.webp` |
| `imgtext/scenetab01_us` | `pack00d_gui/imgtext/scenetab01_us@4x.webp`<br>`pack00m_gui/imgtext/scenetab01_us@2x.webp`<br>`pack00m_gui/imgtext/scenetab01_us.webp` |
| `imgtext/scenetab01sel_us` | `pack00d_gui/imgtext/scenetab01sel_us@4x.webp`<br>`pack00m_gui/imgtext/scenetab01sel_us@2x.webp`<br>`pack00m_gui/imgtext/scenetab01sel_us.webp` |
| `imgtext/weptxt01_us` | `pack00d_gui/imgtext/weptxt01_us@4x.webp` |
| `imgtext/weptxt01sel_us` | `pack00d_gui/imgtext/weptxt01sel_us@4x.webp` |

### Próxima etapa

Fase 5 executada em 06/11/2026; fechamento registrado no início deste relatório.

<!-- FASE_4_FIM -->

## Histórico — fase 3 concluída em 05/11/2026

**Escopo autorizado:** concluir `hollow` e `special`, seguindo os textos da coluna Sugestão PT-BR. A planilha foi apenas lida nesta fase.

| Pasta | Imagens-base | Arquivos novos |
| --- | ---: | ---: |
| hollow | 57 | 157 |
| special | 8 | 16 |
| **Total da fase 3** | **65** | **173** |

O projeto contém **727 arquivos prontos**. O validador conferiu **727 OK, zero com problema**. Restam **338 arquivos com edição necessária** nesta leva; a lista bruta contém 341 faltantes, incluindo as três variantes de LOG dispensadas anteriormente. Não restam arquivos ausentes nas duas pastas desta fase.

Os **1.068 originais**, os **554 arquivos previamente prontos** e a planilha foram preservados, com conferência dos **1.623 hashes** do início da fase. Nenhum arquivo das fases anteriores foi sobrescrito. Os ajustes de revisão ficaram restritos aos novos arquivos desta fase.

### Composição e aparência

- **Placas do mapa (`mp_place_*`):** 42 imagens-base, cada uma com dois estados. O interior sob o texto foi reconstruído usando trechos intactos de placas da mesma família e interpolação das regiões cobertas. A revisão eliminou resíduos do inglês e verificou as três paletas: verde, azul e rosa. As molduras, os ponteiros e os efeitos externos à área interna da cápsula permanecem pixel a pixel iguais ao original na versão-mestre.
- **Comandos (`mp_charbtn01` a `06`):** quatro estados por arquivo, com os textos aprovados de navegação e Retornar ao Título. As setas foram preservadas na posição de cada botão; essa posição varia entre arquivos. O trecho liso da barra sob o inglês foi recomposto a partir de um segmento intacto da mesma família. O quarto estado mantém o tratamento cinza com opacidade de aproximadamente **153/255**, medido nos originais.
- **Selos de novidade:** `alt_new` e `alt_new2` passam a NOVO, com seus degradês próprios e a diferença entre a versão com contorno branco e a versão sem contorno. `mp_new3_a` mantém as **60 cópias**, com suas posições e tamanhos progressivos no atlas de 1.920 × 120 pixels. As cópias que tocam a borda continuam na disposição do original.
- **Faixas `tl_*`:** as quatro cópias de cada rótulo permanecem nos quatro segmentos originais, incluindo as diferenças entre rosa escuro, realce claro e estado final escuro. Foram aplicados CONTINUAR, Galeria, ESPECIAL e INICIAR conforme a capitalização da planilha.
- **Contador:** `tk_title` recebeu Contador de Tickets. Em `tk_ticket`, somente PlayTime foi substituído por Tempo de Jogo; a fotografia, os painéis, a linha sublinhada e os demais rótulos foram preservados fora da área da edição.
- **special:** Dinheiro e ienes mantêm texto claro, contorno marrom e sombra. Detalhes, Fim, Amuleto Ema e Sorte mantêm as três cópias com contorno branco, amarelo e vermelho. A disposição em duas linhas foi mantida em Amuleto Ema, assim como no rótulo original.
- `mp_place_33_us` continua com duas linhas, agora **Sala do conselho / estudantil**. Não foram acrescentadas quebras às outras placas de uma linha. Nomes de personagens e lugares próprios seguiram exatamente a planilha.

As novas versões 4x foram redesenhadas a partir das fontes, e as novas 2x/1x foram reduzidas com LANCZOS e alfa pré-multiplicado, para os tamanhos exatos dos originais. Os arquivos que só existem em 1x foram compostos diretamente nesse canvas, com antisserrilhamento de fonte em resolução interna maior; nenhuma resolução inexistente foi criada.

### Fontes

Foram comparadas candidatas sobre o inglês; as sobreposições e os resultados da busca estão na pasta de apoio. A escolha final também considerou o formato dos terminais e a espessura. **As fontes abaixo são aproximações; a identidade exata não foi comprovada.** Tamanhos nominais antes dos ajustes de ocupação.

| Família | Fonte utilizada | Tamanho na versão-mestre |
| --- | --- | --- |
| mp_place_* | Arial Rounded MT Bold | 72 px; espaçamento de −1 px |
| mp_charbtn* | Humnst777 Cn BT Bold | 74 px; espaçamento reduzido nos rótulos longos |
| alt_new / alt_new2 | Arial Bold | 68 px; ajuste de largura para NOVO |
| mp_new3_a | Arial Bold | 28 px de base, ajustados às 60 caixas nativas |
| tl_* | Bembo Book MT Pro Bold | 28 px; Galeria: 30 px |
| tk_title | Garamond Regular | 68 px; largura ajustada ao canvas |
| tk_ticket | Futura Bk BT Book | 35 px |
| Money / yen | Berlin Sans FB Demi | Dinheiro: 62 px, ienes: 56 px |
| jj_account / back / ema / omikuji | Segoe Print Bold | 48 px; Amuleto Ema: 43 px |

Os valores completos de escala, contorno, posição e espaçamento constam de `parametros_pilulas.json`, `parametros_outros.json` e dos dois renderizadores de apoio.

### Ajustes para acomodar o português

O espaçamento foi reduzido antes do ajuste de ocupação. Dinheiro e ienes receberam redução de tamanho da fonte. Nos demais casos abaixo, a largura foi ajustada dentro da faixa do próprio original. Os percentuais se referem à composição já calibrada e mostram o menor valor entre os estados.

| Imagem-base | Texto aprovado | Ajuste mínimo registrado |
| --- | --- | --- |
| `hollow/mp_place_04_us` | Quarto da Saber | largura 89,1% |
| `hollow/mp_place_05_us` | Quarto da Sakura | largura 83,8% |
| `hollow/mp_place_06_us` | Quarto da Rider | largura 92,5% |
| `hollow/mp_place_09_us` | Porta da frente | largura 99,5% |
| `hollow/mp_place_11_us` | Distrito comercial | largura 91,4% |
| `hollow/mp_place_20_us` | Estação de trem | largura 91,3% |
| `hollow/mp_place_21_us` | Mansão Assombrada | largura 73,6% |
| `hollow/mp_place_22_us` | Mansão Assombrada | largura 73,6% |
| `hollow/mp_place_25_us` | Templo Ryuudou | largura 87,8% |
| `hollow/mp_place_27_us` | Ir para o trabalho | largura 86,0% |
| `hollow/mp_place_29_us` | Dojô de arco e flecha | largura 70,4% |
| `hollow/mp_place_30_us` | Pátio da escola | largura 98,0% |
| `hollow/mp_place_32_us` | Corredor do 3º ano | largura 84,8% |
| `hollow/mp_place_33_us` | Sala do conselho estudantil | largura 87,0% |
| `hollow/mp_place_34_us` | Terrenos do templo | largura 76,9% |
| `hollow/mp_place_35_us` | Portão da montanha | largura 73,4% |
| `hollow/mp_place_36_us` | Interior do templo | largura 83,5% |
| `hollow/mp_place_37_us` | Floresta dos fundos | largura 75,2% |
| `hollow/mp_place_41_us` | Ruínas na floresta | largura 82,7% |
| `hollow/alt_new` | NOVO | largura 76,8% |
| `hollow/alt_new2` | NOVO | largura 76,8% |
| `hollow/mp_charbtn01_us` | Ir para a Cidade | largura 81,5% |
| `hollow/mp_charbtn03_us` | Para Depois da Escola | largura 67,0% |
| `hollow/mp_charbtn04_us` | Para o Dia Seguinte | largura 61,2% |
| `hollow/mp_charbtn05_us` | Para a Noite | largura 66,9% |
| `hollow/mp_charbtn06_us` | Retornar ao Título | largura 90,7% |
| `hollow/tk_ticket` | Tempo de Jogo | largura 89,0% |
| `hollow/tk_title` | Contador de Tickets | largura 73,0% |
| `hollow/tl_continue` | CONTINUAR | largura 87,7% |
| `hollow/tl_special` | ESPECIAL | largura 88,1% |
| `hollow/tl_start` | INICIAR | largura 82,9% |
| `special/img_syojikin_us` | Dinheiro | fonte 91,0% |
| `special/jj_money_us` | Dinheiro | fonte 91,0% |
| `special/img_yen_us` | ienes | fonte 82,9% |
| `special/jj_yen_us` | ienes | fonte 82,9% |
| `special/jj_account_us` | Detalhes | largura 91,8% |

### Reconstrução, observações e limites

- Houve reconstrução apenas de fundos de interface: interiores lisos das placas, trecho central das barras de comando e fundo rosa sob PlayTime. Nenhuma CG ou fotografia foi reconstruída.
- A planilha descreve `jj_ema_us` como Ema charm, enquanto a imagem original mostra Prayer tablet. Foi aplicado **Amuleto Ema**, sem alterar o texto aprovado.
- `tk_ticket` também contém rótulos japoneses, incluindo os de horas/minutos e progresso, que não possuem linhas de tradução nesta imagem na planilha. Eles foram mantidos. A conclusão desta fase cobre os textos listados na planilha, sem acrescentar traduções para esses rótulos.
- Todas as imagens-base desta fase possuíam texto a substituir; nenhuma foi dispensada por inglês idêntico ao português.
- As divergências herdadas das versões FSN de `08_date`, registradas na fase 2, permanecem sem alteração.
- Não houve teste dentro do jogo ou recompilação. Git, scripts do jogo, pastas extraídas e hanafuda não foram alterados.

### Conferência

- Validação estrutural: **727 conferidos, 727 OK, zero com problema**; caminhos, nomes, dimensões, modo de cor e WebP sem perda conferidos.
- Conferência dos 1.623 hashes anteriores: nenhuma alteração.
- Conferência adicional de preservação dos ponteiros/molduras fora da área interna das placas, das setas antes da área de texto dos comandos e da arte externa à alteração em `tk_ticket`.
- Foram geradas **65 folhas individuais**, com original/PT-BR em tamanho nativo, nas resoluções disponíveis e sobre fundos claro/escuro. A revisão incluiu nove folhas de original/resultado, nove de resoluções, além das inspeções de detalhes em tamanho nativo.

Pasta de apoio:

`C:/Users/Thiago/.codex/visualizations/2026/11/05/01a1ac56-1f6b-7422-a08c-bc9035480780/fha-calibracao/fase_3`

Índice: `comparacoes_fase_3.html`. Prévia: `previa_fase_3.png`. Registros: `inventario.json`, `estado_inicial.json`, `arquivos_gerados.json`, `parametros_pilulas.json`, `parametros_outros.json`, `busca_fontes.json`, `busca_fontes_outros.json`, `validacao_final.txt` e `resultado_final.json`.

### Imagem → arquivos gerados na fase 3

Caminhos relativos a `Imagens/imagens_prontas`.

| Imagem-base | Arquivos novos |
| --- | --- |
| `hollow/alt_new` | `pack00d_gui/hollow/alt_new@4x.webp`<br>`pack00m_gui/hollow/alt_new@2x.webp`<br>`pack00m_gui/hollow/alt_new.webp` |
| `hollow/alt_new2` | `pack00d_gui/hollow/alt_new2@4x.webp`<br>`pack00m_gui/hollow/alt_new2@2x.webp`<br>`pack00m_gui/hollow/alt_new2.webp` |
| `hollow/mp_new3_a` | `pack00m_gui/hollow/mp_new3_a.webp` |
| `hollow/mp_charbtn01_us` | `pack00d_gui/hollow/mp_charbtn01_us@4x.webp`<br>`pack00m_gui/hollow/mp_charbtn01_us@2x.webp`<br>`pack00m_gui/hollow/mp_charbtn01_us.webp` |
| `hollow/mp_charbtn02_us` | `pack00d_gui/hollow/mp_charbtn02_us@4x.webp`<br>`pack00m_gui/hollow/mp_charbtn02_us@2x.webp`<br>`pack00m_gui/hollow/mp_charbtn02_us.webp` |
| `hollow/mp_charbtn03_us` | `pack00d_gui/hollow/mp_charbtn03_us@4x.webp`<br>`pack00m_gui/hollow/mp_charbtn03_us@2x.webp`<br>`pack00m_gui/hollow/mp_charbtn03_us.webp` |
| `hollow/mp_charbtn04_us` | `pack00d_gui/hollow/mp_charbtn04_us@4x.webp`<br>`pack00m_gui/hollow/mp_charbtn04_us@2x.webp`<br>`pack00m_gui/hollow/mp_charbtn04_us.webp` |
| `hollow/mp_charbtn05_us` | `pack00d_gui/hollow/mp_charbtn05_us@4x.webp`<br>`pack00m_gui/hollow/mp_charbtn05_us@2x.webp`<br>`pack00m_gui/hollow/mp_charbtn05_us.webp` |
| `hollow/mp_charbtn06_us` | `pack00d_gui/hollow/mp_charbtn06_us@4x.webp`<br>`pack00m_gui/hollow/mp_charbtn06_us@2x.webp`<br>`pack00m_gui/hollow/mp_charbtn06_us.webp` |
| `hollow/mp_place_01_us` | `pack00d_gui/hollow/mp_place_01_us@4x.webp`<br>`pack00m_gui/hollow/mp_place_01_us@2x.webp`<br>`pack00m_gui/hollow/mp_place_01_us.webp` |
| `hollow/mp_place_02_us` | `pack00d_gui/hollow/mp_place_02_us@4x.webp`<br>`pack00m_gui/hollow/mp_place_02_us@2x.webp`<br>`pack00m_gui/hollow/mp_place_02_us.webp` |
| `hollow/mp_place_03_us` | `pack00d_gui/hollow/mp_place_03_us@4x.webp`<br>`pack00m_gui/hollow/mp_place_03_us@2x.webp`<br>`pack00m_gui/hollow/mp_place_03_us.webp` |
| `hollow/mp_place_04_us` | `pack00d_gui/hollow/mp_place_04_us@4x.webp`<br>`pack00m_gui/hollow/mp_place_04_us@2x.webp`<br>`pack00m_gui/hollow/mp_place_04_us.webp` |
| `hollow/mp_place_05_us` | `pack00d_gui/hollow/mp_place_05_us@4x.webp`<br>`pack00m_gui/hollow/mp_place_05_us@2x.webp`<br>`pack00m_gui/hollow/mp_place_05_us.webp` |
| `hollow/mp_place_06_us` | `pack00d_gui/hollow/mp_place_06_us@4x.webp`<br>`pack00m_gui/hollow/mp_place_06_us@2x.webp`<br>`pack00m_gui/hollow/mp_place_06_us.webp` |
| `hollow/mp_place_07_us` | `pack00d_gui/hollow/mp_place_07_us@4x.webp`<br>`pack00m_gui/hollow/mp_place_07_us@2x.webp`<br>`pack00m_gui/hollow/mp_place_07_us.webp` |
| `hollow/mp_place_08_us` | `pack00d_gui/hollow/mp_place_08_us@4x.webp`<br>`pack00m_gui/hollow/mp_place_08_us@2x.webp`<br>`pack00m_gui/hollow/mp_place_08_us.webp` |
| `hollow/mp_place_09_us` | `pack00d_gui/hollow/mp_place_09_us@4x.webp`<br>`pack00m_gui/hollow/mp_place_09_us@2x.webp`<br>`pack00m_gui/hollow/mp_place_09_us.webp` |
| `hollow/mp_place_10_us` | `pack00d_gui/hollow/mp_place_10_us@4x.webp`<br>`pack00m_gui/hollow/mp_place_10_us@2x.webp`<br>`pack00m_gui/hollow/mp_place_10_us.webp` |
| `hollow/mp_place_11_us` | `pack00d_gui/hollow/mp_place_11_us@4x.webp`<br>`pack00m_gui/hollow/mp_place_11_us@2x.webp`<br>`pack00m_gui/hollow/mp_place_11_us.webp` |
| `hollow/mp_place_12_us` | `pack00d_gui/hollow/mp_place_12_us@4x.webp`<br>`pack00m_gui/hollow/mp_place_12_us@2x.webp`<br>`pack00m_gui/hollow/mp_place_12_us.webp` |
| `hollow/mp_place_13_us` | `pack00d_gui/hollow/mp_place_13_us@4x.webp`<br>`pack00m_gui/hollow/mp_place_13_us@2x.webp`<br>`pack00m_gui/hollow/mp_place_13_us.webp` |
| `hollow/mp_place_14_us` | `pack00d_gui/hollow/mp_place_14_us@4x.webp`<br>`pack00m_gui/hollow/mp_place_14_us@2x.webp`<br>`pack00m_gui/hollow/mp_place_14_us.webp` |
| `hollow/mp_place_15_us` | `pack00d_gui/hollow/mp_place_15_us@4x.webp`<br>`pack00m_gui/hollow/mp_place_15_us@2x.webp`<br>`pack00m_gui/hollow/mp_place_15_us.webp` |
| `hollow/mp_place_16_us` | `pack00d_gui/hollow/mp_place_16_us@4x.webp`<br>`pack00m_gui/hollow/mp_place_16_us@2x.webp`<br>`pack00m_gui/hollow/mp_place_16_us.webp` |
| `hollow/mp_place_17_us` | `pack00d_gui/hollow/mp_place_17_us@4x.webp`<br>`pack00m_gui/hollow/mp_place_17_us@2x.webp`<br>`pack00m_gui/hollow/mp_place_17_us.webp` |
| `hollow/mp_place_18_us` | `pack00d_gui/hollow/mp_place_18_us@4x.webp`<br>`pack00m_gui/hollow/mp_place_18_us@2x.webp`<br>`pack00m_gui/hollow/mp_place_18_us.webp` |
| `hollow/mp_place_19_us` | `pack00d_gui/hollow/mp_place_19_us@4x.webp`<br>`pack00m_gui/hollow/mp_place_19_us@2x.webp`<br>`pack00m_gui/hollow/mp_place_19_us.webp` |
| `hollow/mp_place_20_us` | `pack00d_gui/hollow/mp_place_20_us@4x.webp`<br>`pack00m_gui/hollow/mp_place_20_us@2x.webp`<br>`pack00m_gui/hollow/mp_place_20_us.webp` |
| `hollow/mp_place_21_us` | `pack00d_gui/hollow/mp_place_21_us@4x.webp`<br>`pack00m_gui/hollow/mp_place_21_us@2x.webp`<br>`pack00m_gui/hollow/mp_place_21_us.webp` |
| `hollow/mp_place_22_us` | `pack00d_gui/hollow/mp_place_22_us@4x.webp`<br>`pack00m_gui/hollow/mp_place_22_us@2x.webp`<br>`pack00m_gui/hollow/mp_place_22_us.webp` |
| `hollow/mp_place_23_us` | `pack00d_gui/hollow/mp_place_23_us@4x.webp`<br>`pack00m_gui/hollow/mp_place_23_us@2x.webp`<br>`pack00m_gui/hollow/mp_place_23_us.webp` |
| `hollow/mp_place_24_us` | `pack00d_gui/hollow/mp_place_24_us@4x.webp`<br>`pack00m_gui/hollow/mp_place_24_us@2x.webp`<br>`pack00m_gui/hollow/mp_place_24_us.webp` |
| `hollow/mp_place_25_us` | `pack00d_gui/hollow/mp_place_25_us@4x.webp`<br>`pack00m_gui/hollow/mp_place_25_us@2x.webp`<br>`pack00m_gui/hollow/mp_place_25_us.webp` |
| `hollow/mp_place_26_us` | `pack00d_gui/hollow/mp_place_26_us@4x.webp`<br>`pack00m_gui/hollow/mp_place_26_us@2x.webp`<br>`pack00m_gui/hollow/mp_place_26_us.webp` |
| `hollow/mp_place_27_us` | `pack00d_gui/hollow/mp_place_27_us@4x.webp`<br>`pack00m_gui/hollow/mp_place_27_us@2x.webp`<br>`pack00m_gui/hollow/mp_place_27_us.webp` |
| `hollow/mp_place_28_us` | `pack00d_gui/hollow/mp_place_28_us@4x.webp`<br>`pack00m_gui/hollow/mp_place_28_us@2x.webp`<br>`pack00m_gui/hollow/mp_place_28_us.webp` |
| `hollow/mp_place_29_us` | `pack00d_gui/hollow/mp_place_29_us@4x.webp`<br>`pack00m_gui/hollow/mp_place_29_us@2x.webp`<br>`pack00m_gui/hollow/mp_place_29_us.webp` |
| `hollow/mp_place_30_us` | `pack00d_gui/hollow/mp_place_30_us@4x.webp`<br>`pack00m_gui/hollow/mp_place_30_us@2x.webp`<br>`pack00m_gui/hollow/mp_place_30_us.webp` |
| `hollow/mp_place_31_us` | `pack00d_gui/hollow/mp_place_31_us@4x.webp`<br>`pack00m_gui/hollow/mp_place_31_us@2x.webp`<br>`pack00m_gui/hollow/mp_place_31_us.webp` |
| `hollow/mp_place_32_us` | `pack00d_gui/hollow/mp_place_32_us@4x.webp`<br>`pack00m_gui/hollow/mp_place_32_us@2x.webp`<br>`pack00m_gui/hollow/mp_place_32_us.webp` |
| `hollow/mp_place_33_us` | `pack00d_gui/hollow/mp_place_33_us@4x.webp`<br>`pack00m_gui/hollow/mp_place_33_us@2x.webp`<br>`pack00m_gui/hollow/mp_place_33_us.webp` |
| `hollow/mp_place_34_us` | `pack00d_gui/hollow/mp_place_34_us@4x.webp`<br>`pack00m_gui/hollow/mp_place_34_us@2x.webp`<br>`pack00m_gui/hollow/mp_place_34_us.webp` |
| `hollow/mp_place_35_us` | `pack00d_gui/hollow/mp_place_35_us@4x.webp`<br>`pack00m_gui/hollow/mp_place_35_us@2x.webp`<br>`pack00m_gui/hollow/mp_place_35_us.webp` |
| `hollow/mp_place_36_us` | `pack00d_gui/hollow/mp_place_36_us@4x.webp`<br>`pack00m_gui/hollow/mp_place_36_us@2x.webp`<br>`pack00m_gui/hollow/mp_place_36_us.webp` |
| `hollow/mp_place_37_us` | `pack00d_gui/hollow/mp_place_37_us@4x.webp`<br>`pack00m_gui/hollow/mp_place_37_us@2x.webp`<br>`pack00m_gui/hollow/mp_place_37_us.webp` |
| `hollow/mp_place_38_us` | `pack00d_gui/hollow/mp_place_38_us@4x.webp`<br>`pack00m_gui/hollow/mp_place_38_us@2x.webp`<br>`pack00m_gui/hollow/mp_place_38_us.webp` |
| `hollow/mp_place_40_us` | `pack00d_gui/hollow/mp_place_40_us@4x.webp`<br>`pack00m_gui/hollow/mp_place_40_us@2x.webp`<br>`pack00m_gui/hollow/mp_place_40_us.webp` |
| `hollow/mp_place_41_us` | `pack00d_gui/hollow/mp_place_41_us@4x.webp`<br>`pack00m_gui/hollow/mp_place_41_us@2x.webp`<br>`pack00m_gui/hollow/mp_place_41_us.webp` |
| `hollow/mp_place_44_us` | `pack00d_gui/hollow/mp_place_44_us@4x.webp`<br>`pack00m_gui/hollow/mp_place_44_us@2x.webp`<br>`pack00m_gui/hollow/mp_place_44_us.webp` |
| `hollow/mp_place_48_us` | `pack00d_gui/hollow/mp_place_48_us@4x.webp`<br>`pack00m_gui/hollow/mp_place_48_us@2x.webp`<br>`pack00m_gui/hollow/mp_place_48_us.webp` |
| `hollow/tk_ticket` | `pack00m_gui/hollow/tk_ticket.webp` |
| `hollow/tk_title` | `pack00m_gui/hollow/tk_title.webp` |
| `hollow/tl_continue` | `pack00m_gui/hollow/tl_continue.webp` |
| `hollow/tl_gallery` | `pack00m_gui/hollow/tl_gallery.webp` |
| `hollow/tl_special` | `pack00m_gui/hollow/tl_special.webp` |
| `hollow/tl_start` | `pack00m_gui/hollow/tl_start.webp` |
| `special/img_syojikin_us` | `pack00d_gui/special/img_syojikin_us@4x.webp`<br>`pack00m_gui/special/img_syojikin_us@2x.webp`<br>`pack00m_gui/special/img_syojikin_us.webp` |
| `special/jj_money_us` | `pack00d_gui/special/jj_money_us@4x.webp`<br>`pack00m_gui/special/jj_money_us@2x.webp`<br>`pack00m_gui/special/jj_money_us.webp` |
| `special/img_yen_us` | `pack00d_gui/special/img_yen_us@4x.webp`<br>`pack00m_gui/special/img_yen_us@2x.webp`<br>`pack00m_gui/special/img_yen_us.webp` |
| `special/jj_yen_us` | `pack00d_gui/special/jj_yen_us@4x.webp`<br>`pack00m_gui/special/jj_yen_us@2x.webp`<br>`pack00m_gui/special/jj_yen_us.webp` |
| `special/jj_account_us` | `pack00m_gui/special/jj_account_us.webp` |
| `special/jj_back_us` | `pack00m_gui/special/jj_back_us.webp` |
| `special/jj_ema_us` | `pack00m_gui/special/jj_ema_us.webp` |
| `special/jj_omikuji_us` | `pack00m_gui/special/jj_omikuji_us.webp` |

### Próxima fase planejada

Fase 4 executada neste atendimento; situação atual e eventuais complementos descritos no início deste relatório.

---

## Etapa anterior — correção de Título e fase 2 concluídas em 05/11/2026

### Correção solicitada

O botão de retorno da seleção de saves passa de **Entrada** para **Título**. Foram substituídas, por autorização expressa, as quatro variantes `02_title/t_entrance_1`, `_2`, `_2_1` e `_3`, nas resoluções 1x, 2x e 4x: **12 arquivos**. Mantiveram-se o alinhamento central, a fonte Futura Bk BT Book de 72 px na 4x, o afinamento de 0,75 px e os quatro tratamentos de cor/brilho. `common/menu_title_6`, que também contém Entrada, não faz parte desta correção.

A planilha foi sincronizada em **Traduções!F4 = Título**. A comparação das células confirmou uma única alteração de valor; apenas o XML da aba correspondente mudou dentro do XLSX. As demais entradas do arquivo, estilos e demais células foram preservados. A comparação dos hashes anteriores confirmou exatamente os 12 arquivos autorizados e a planilha como alterações da correção.

### Resultado da fase 2

| Pasta | Imagens-base | Arquivos novos |
| --- | ---: | ---: |
| 08_date | 3 | 3, somente 4x |
| map | 2 | 6 |
| mapdate | 29 | 87 |
| **Total** | **34** | **96** |

O projeto contém **554 arquivos prontos**, todos aprovados pelo validador estrutural: **554 OK, zero com problema**. Restam **511 arquivos com edição necessária** nesta leva. O validador lista 514 faltantes porque inclui as três variantes de LOG já dispensadas. Não restam arquivos ausentes nas pastas desta fase.

O estado inicial da fase 2 foi registrado após a correção de Título: os **1.068 originais**, os **458 arquivos anteriores** e a planilha mantiveram seus hashes durante a produção desta fase. Git, scripts do jogo, pastas extraídas e hanafuda não foram modificados. Não houve recompilação ou teste dentro do jogo.

### Fontes e reprodução

Os tamanhos abaixo são nominais na maior resolução, antes do ajuste às ocupações do original ou da referência FSN. A comparação com o inglês e as sobreposições ficaram registradas. As fontes são aproximações calibradas; a identidade exata não foi comprovada.

| Família | Fonte | Tamanho e ajustes |
| --- | --- | --- |
| 08_date/day_subtitle* | Jost Variable, peso padrão | 88 px; afinamento de 0,75 px; posições e escala das referências 2x |
| map/ent_day2, rótulos | Humnst777 Cn BT Bold | 66 px; afinamento de 0,25 px; Depois da Escola com espaçamento de −1 px e ajuste de largura |
| map/mapname | Humnst777 BT Roman | 120 px; afinamento de 0,25 px; texto branco e sombra escura |
| mapdate/ec_bar-day* | Calibri Light | 84 px; afinamento de 1,25 px; espaçamento de calibração de 2 px |
| mapdate/ec_day* | Garamond Bold | 140 px; afinamento de 0,25 px; espaçamento de 8 px; degradê cinza/preto |

- As novas 4x foram desenhadas a partir das fontes. As novas 2x e 1x foram reduzidas com LANCZOS e alfa pré-multiplicado para os tamanhos exatos dos próprios originais.
- Em `08_date`, somente as 4x ausentes foram geradas. As seis versões FSN 1x/2x foram preservadas. Os trechos cujo texto final é igual ao inglês foram copiados do próprio original 4x, sem ampliar a referência 2x: NEO, Utopia, VS Berserker, Avenger, De:light, Overdose e FINAL.
- Em `ent_day2`, 08-10, 09-10 e 11-10 foram montados reorganizando os algarismos nativos. A linha 10-10 permanece pixel a pixel igual. O fundo liso sob os quatro rótulos foi reconstruído localmente a partir das regiões sem texto. As molduras e sombras externas das pílulas foram preservadas pixel a pixel; os novos textos repetem o degradê colorido, a luz branca e a sombra suave.
- `mapname` contém sete faixas: Mansão Emiya e Cidade de Fuyuki se repetem nas duas últimas posições. As duas repetições foram traduzidas.
- Os cartões `mapdate` nítidos mantêm o fundo branco real. As variantes `b` repetem o desfoque medido no original e a borda. Há diferenças de modo entre resoluções: vários cartões são RGB em 4x/2x e RGBA em 1x. Em todos os arquivos RGBA desta família, o alfa do painel foi preservado exatamente do original da própria resolução, inclusive a borda 1x.
- Não houve reconstrução de CG ou ilustração nesta fase. Apenas o interior liso das quatro pílulas precisou ser reconstruído.

### Textos que precisaram de ajuste de largura

- `map/ent_day2_us`: Depois da Escola, largura final 74.5% após o ajuste de espaçamento.
- `mapdate/ec_day1-放課後_us`: Depois da Escola  Dia 1, largura final 96.7% após o ajuste de espaçamento.
- `mapdate/ec_day1-放課後b_us`: Depois da Escola  Dia 1, largura final 96.7% após o ajuste de espaçamento.
- `mapdate/ec_day2-放課後_us`: Depois da Escola  Dia 2, largura final 96.9% após o ajuste de espaçamento.
- `mapdate/ec_day2-放課後b_us`: Depois da Escola  Dia 2, largura final 96.9% após o ajuste de espaçamento.
- `mapdate/ec_day3-放課後_us`: Depois da Escola  Dia 3, largura final 96.8% após o ajuste de espaçamento.
- `mapdate/ec_day3-放課後b_us`: Depois da Escola  Dia 3, largura final 96.8% após o ajuste de espaçamento.
- `mapdate/ec_day4-放課後_us`: Depois da Escola  Dia 4, largura final 96.8% após o ajuste de espaçamento.
- `mapdate/ec_day4-放課後b_us`: Depois da Escola  Dia 4, largura final 96.8% após o ajuste de espaçamento.

Não foram introduzidas quebras de linha. Os números e rótulos permanecem nas faixas próprias de cada atlas.

### Divergências herdadas das versões FSN

A planilha atual é a autoridade para as novas 4x. As versões FSN existentes foram preservadas conforme a regra do projeto e, portanto, há diferenças de texto entre resoluções nestes pontos:

| Atlas | Texto antigo visto na referência 2x | Texto aprovado aplicado na 4x |
| --- | --- | --- |
| day_subtitle00_us | 6 BLADE | 6 LÂMINA |
| day_subtitle01_us | 6 Faker | 6 Farsante |
| day_subtitle02_us | 10 Bosque, Bela Adormecida | 10 Bosque Escuro, Bela Adormecida |
| day_subtitle02_us | 13 LAST TALK | 13 ÚLTIMA CONVERSA |

Essas diferenças não são detectadas pelo validador de formato e continuam como ressalva para uma futura uniformização das versões herdadas. Nenhum texto aprovado na planilha foi retraduzido nesta fase.

### Conferência e arquivos de apoio

Foram geradas **38 folhas individuais**: 34 imagens-base da fase 2 e as quatro variantes corrigidas de Título, com original/PT-BR, resoluções nativas e fundos claro/escuro. A revisão incluiu os três atlas completos, quatro folhas de original/resultado, cinco folhas de resoluções e inspeção em tamanho útil dos rótulos do mapa. A conferência adicional verificou a preservação de 10-10, das molduras/sombras das quatro pílulas e do alfa nativo dos painéis mapdate.

Pasta de apoio:

`C:/Users/Thiago/.codex/visualizations/2026/11/05/01a1ac56-1f6b-7422-a08c-bc9035480780/fha-calibracao/fase_2`

Índice: `comparacoes_fase_2.html`. Prévia: `previa_fase_2.png`. Registros: `correcao_titulo.json`, `estado_inicial.json`, `inventario.json`, `parametros.json`, `busca_fontes.json`, `arquivos_gerados.json`, `validacao_final.txt` e `resultado_final.json`.

### Imagem → arquivos gerados na fase 2

Caminhos relativos a `Imagens/imagens_prontas`.

| Imagem-base | Arquivos novos |
| --- | --- |
| `08_date/day_subtitle00_us` | `pack00d_gui/08_date/day_subtitle00_us@4x.webp` |
| `08_date/day_subtitle01_us` | `pack00d_gui/08_date/day_subtitle01_us@4x.webp` |
| `08_date/day_subtitle02_us` | `pack00d_gui/08_date/day_subtitle02_us@4x.webp` |
| `map/ent_day2_us` | `pack00d_gui/map/ent_day2_us@4x.webp`<br>`pack00m_gui/map/ent_day2_us@2x.webp`<br>`pack00m_gui/map/ent_day2_us.webp` |
| `map/mapname_us` | `pack00d_gui/map/mapname_us@4x.webp`<br>`pack00m_gui/map/mapname_us@2x.webp`<br>`pack00m_gui/map/mapname_us.webp` |
| `mapdate/ec_bar-day1_us` | `pack00d_gui/mapdate/ec_bar-day1_us@4x.webp`<br>`pack00m_gui/mapdate/ec_bar-day1_us@2x.webp`<br>`pack00m_gui/mapdate/ec_bar-day1_us.webp` |
| `mapdate/ec_bar-day1b_us` | `pack00d_gui/mapdate/ec_bar-day1b_us@4x.webp`<br>`pack00m_gui/mapdate/ec_bar-day1b_us@2x.webp`<br>`pack00m_gui/mapdate/ec_bar-day1b_us.webp` |
| `mapdate/ec_bar-day2` | `pack00d_gui/mapdate/ec_bar-day2@4x.webp`<br>`pack00m_gui/mapdate/ec_bar-day2@2x.webp`<br>`pack00m_gui/mapdate/ec_bar-day2.webp` |
| `mapdate/ec_bar-day3` | `pack00d_gui/mapdate/ec_bar-day3@4x.webp`<br>`pack00m_gui/mapdate/ec_bar-day3@2x.webp`<br>`pack00m_gui/mapdate/ec_bar-day3.webp` |
| `mapdate/ec_bar-day4` | `pack00d_gui/mapdate/ec_bar-day4@4x.webp`<br>`pack00m_gui/mapdate/ec_bar-day4@2x.webp`<br>`pack00m_gui/mapdate/ec_bar-day4.webp` |
| `mapdate/ec_day1-午前_us` | `pack00d_gui/mapdate/ec_day1-午前_us@4x.webp`<br>`pack00m_gui/mapdate/ec_day1-午前_us@2x.webp`<br>`pack00m_gui/mapdate/ec_day1-午前_us.webp` |
| `mapdate/ec_day1-午前b_us` | `pack00d_gui/mapdate/ec_day1-午前b_us@4x.webp`<br>`pack00m_gui/mapdate/ec_day1-午前b_us@2x.webp`<br>`pack00m_gui/mapdate/ec_day1-午前b_us.webp` |
| `mapdate/ec_day1-午後_us` | `pack00d_gui/mapdate/ec_day1-午後_us@4x.webp`<br>`pack00m_gui/mapdate/ec_day1-午後_us@2x.webp`<br>`pack00m_gui/mapdate/ec_day1-午後_us.webp` |
| `mapdate/ec_day1-午後b_us` | `pack00d_gui/mapdate/ec_day1-午後b_us@4x.webp`<br>`pack00m_gui/mapdate/ec_day1-午後b_us@2x.webp`<br>`pack00m_gui/mapdate/ec_day1-午後b_us.webp` |
| `mapdate/ec_day1-放課後_us` | `pack00d_gui/mapdate/ec_day1-放課後_us@4x.webp`<br>`pack00m_gui/mapdate/ec_day1-放課後_us@2x.webp`<br>`pack00m_gui/mapdate/ec_day1-放課後_us.webp` |
| `mapdate/ec_day1-放課後b_us` | `pack00d_gui/mapdate/ec_day1-放課後b_us@4x.webp`<br>`pack00m_gui/mapdate/ec_day1-放課後b_us@2x.webp`<br>`pack00m_gui/mapdate/ec_day1-放課後b_us.webp` |
| `mapdate/ec_day2-午前_us` | `pack00d_gui/mapdate/ec_day2-午前_us@4x.webp`<br>`pack00m_gui/mapdate/ec_day2-午前_us@2x.webp`<br>`pack00m_gui/mapdate/ec_day2-午前_us.webp` |
| `mapdate/ec_day2-午前b_us` | `pack00d_gui/mapdate/ec_day2-午前b_us@4x.webp`<br>`pack00m_gui/mapdate/ec_day2-午前b_us@2x.webp`<br>`pack00m_gui/mapdate/ec_day2-午前b_us.webp` |
| `mapdate/ec_day2-午後_us` | `pack00d_gui/mapdate/ec_day2-午後_us@4x.webp`<br>`pack00m_gui/mapdate/ec_day2-午後_us@2x.webp`<br>`pack00m_gui/mapdate/ec_day2-午後_us.webp` |
| `mapdate/ec_day2-午後b_us` | `pack00d_gui/mapdate/ec_day2-午後b_us@4x.webp`<br>`pack00m_gui/mapdate/ec_day2-午後b_us@2x.webp`<br>`pack00m_gui/mapdate/ec_day2-午後b_us.webp` |
| `mapdate/ec_day2-放課後_us` | `pack00d_gui/mapdate/ec_day2-放課後_us@4x.webp`<br>`pack00m_gui/mapdate/ec_day2-放課後_us@2x.webp`<br>`pack00m_gui/mapdate/ec_day2-放課後_us.webp` |
| `mapdate/ec_day2-放課後b_us` | `pack00d_gui/mapdate/ec_day2-放課後b_us@4x.webp`<br>`pack00m_gui/mapdate/ec_day2-放課後b_us@2x.webp`<br>`pack00m_gui/mapdate/ec_day2-放課後b_us.webp` |
| `mapdate/ec_day3-午前_us` | `pack00d_gui/mapdate/ec_day3-午前_us@4x.webp`<br>`pack00m_gui/mapdate/ec_day3-午前_us@2x.webp`<br>`pack00m_gui/mapdate/ec_day3-午前_us.webp` |
| `mapdate/ec_day3-午前b_us` | `pack00d_gui/mapdate/ec_day3-午前b_us@4x.webp`<br>`pack00m_gui/mapdate/ec_day3-午前b_us@2x.webp`<br>`pack00m_gui/mapdate/ec_day3-午前b_us.webp` |
| `mapdate/ec_day3-午後_us` | `pack00d_gui/mapdate/ec_day3-午後_us@4x.webp`<br>`pack00m_gui/mapdate/ec_day3-午後_us@2x.webp`<br>`pack00m_gui/mapdate/ec_day3-午後_us.webp` |
| `mapdate/ec_day3-午後b_us` | `pack00d_gui/mapdate/ec_day3-午後b_us@4x.webp`<br>`pack00m_gui/mapdate/ec_day3-午後b_us@2x.webp`<br>`pack00m_gui/mapdate/ec_day3-午後b_us.webp` |
| `mapdate/ec_day3-放課後_us` | `pack00d_gui/mapdate/ec_day3-放課後_us@4x.webp`<br>`pack00m_gui/mapdate/ec_day3-放課後_us@2x.webp`<br>`pack00m_gui/mapdate/ec_day3-放課後_us.webp` |
| `mapdate/ec_day3-放課後b_us` | `pack00d_gui/mapdate/ec_day3-放課後b_us@4x.webp`<br>`pack00m_gui/mapdate/ec_day3-放課後b_us@2x.webp`<br>`pack00m_gui/mapdate/ec_day3-放課後b_us.webp` |
| `mapdate/ec_day4-午前_us` | `pack00d_gui/mapdate/ec_day4-午前_us@4x.webp`<br>`pack00m_gui/mapdate/ec_day4-午前_us@2x.webp`<br>`pack00m_gui/mapdate/ec_day4-午前_us.webp` |
| `mapdate/ec_day4-午前b_us` | `pack00d_gui/mapdate/ec_day4-午前b_us@4x.webp`<br>`pack00m_gui/mapdate/ec_day4-午前b_us@2x.webp`<br>`pack00m_gui/mapdate/ec_day4-午前b_us.webp` |
| `mapdate/ec_day4-午後_us` | `pack00d_gui/mapdate/ec_day4-午後_us@4x.webp`<br>`pack00m_gui/mapdate/ec_day4-午後_us@2x.webp`<br>`pack00m_gui/mapdate/ec_day4-午後_us.webp` |
| `mapdate/ec_day4-午後b_us` | `pack00d_gui/mapdate/ec_day4-午後b_us@4x.webp`<br>`pack00m_gui/mapdate/ec_day4-午後b_us@2x.webp`<br>`pack00m_gui/mapdate/ec_day4-午後b_us.webp` |
| `mapdate/ec_day4-放課後_us` | `pack00d_gui/mapdate/ec_day4-放課後_us@4x.webp`<br>`pack00m_gui/mapdate/ec_day4-放課後_us@2x.webp`<br>`pack00m_gui/mapdate/ec_day4-放課後_us.webp` |
| `mapdate/ec_day4-放課後b_us` | `pack00d_gui/mapdate/ec_day4-放課後b_us@4x.webp`<br>`pack00m_gui/mapdate/ec_day4-放課後b_us@2x.webp`<br>`pack00m_gui/mapdate/ec_day4-放課後b_us.webp` |

### Próxima fase planejada

A fase 3 planejada na conclusão da fase 2 foi executada posteriormente e está registrada no início deste relatório.

---

## Etapa anterior — fase 1 concluída em 05/11/2026

**Escopo autorizado:** concluir `02_title` e as três versões 4x pendentes de `07_config`.

| Resultado | Quantidade |
| --- | ---: |
| Novos arquivos de 02_title | 90 |
| Novos arquivos de 07_config | 3 |
| **Arquivos novos nesta fase** | **93** |
| Imagens-base tratadas | 35 |
| Arquivos prontos em 02_title, somando os anteriores | 96 |
| Arquivos prontos em 07_config, somando os anteriores | 8 |
| Pendências nestas duas pastas | **0** |
| Arquivos prontos no projeto | **458** |
| Arquivos restantes que precisam de edição na leva | **607** |

O validador lista 610 originais sem cópia pronta; três são as variantes de LOG já dispensadas na etapa anterior. Os 365 arquivos previamente prontos, os 1.068 originais e a planilha foram preservados, com conferência dos 1.434 hashes registrados no início da fase.

### Texto, fontes e aparência

- O texto foi lido da coluna **Sugestão PT-BR**, sem alteração: Continuar, Entrada, Sair, Galeria, Iniciar, Novo Jogo, Aperte Um Botão, Especial e Outros.
- **Títulos:** Futura Bk BT Book, 72 px nominais na 4x, com afinamento de traço de 0,75 px. A calibração usa a 2x pronta de `t_continue_4`; `t_exit_4` e `t_newgame_4` também seguem a ocupação e a posição de suas próprias referências. Os outros títulos mantêm o alinhamento central e as diferenças de altura de cada palavra.
- **Configurações:** Segoe UI Regular, 56 px nominais na 4x. O texto branco e a sombra preta foram separados e ajustados às três referências 2x de Outros. O desfoque do texto e a sombra variam conforme a imagem; os valores estão em `parametros.json`.
- Os tamanhos são de renderização, antes do ajuste da ocupação às referências. As fontes usadas são aproximações calibradas; a identidade exata das fontes históricas não foi comprovada.
- Os estados normais dos títulos permanecem pretos. Os estados rosa sem brilho, rosa com brilho e vermelho com brilho mantêm seus tratamentos separados, medidos no original correspondente. A variante `_2_1` é um estado destacado próprio.
- As versões 4x foram redesenhadas a partir de fontes vetoriais. As novas 2x e 1x foram reduzidas com LANCZOS e alfa pré-multiplicado, para as dimensões exatas de cada original. Nenhuma referência 2x foi ampliada para gerar uma 4x.
- As versões 1x e 2x já prontas do FSN não foram sobrescritas. `07_cv_27c_us` só possui 2x e 4x; não foi criada uma 1x inexistente.
- Não foi necessária redução especial de fonte ou quebra de linha para acomodar os textos desta fase. Aperte Um Botão cabe no canvas, com acento e margens preservados.
- Todas as imagens desta fase contêm texto sobre transparência; não houve reconstrução de arte ou fundo. Nenhuma imagem desta fase foi dispensada por texto igual ao inglês.

### Conferência

- `validar_prontas.py --faltando`: **458 conferidos, 458 OK, zero com problema**.
- Os 93 arquivos novos têm o nome e caminho esperados, as dimensões e o modo RGBA do original e codificação WebP sem perda VP8L. Não foram adicionados EXIF ou XMP.
- Nenhuma imagem nova apresenta alfa nas bordas externas do canvas; não foram encontrados cortes de texto ou brilho na conferência.
- Foram geradas **35 folhas individuais**, com original e PT-BR em tamanho nativo nas resoluções disponíveis e sobre fundos claro e escuro.
- A revisão visual incluiu cinco folhas de original/resultado e cinco folhas das resoluções disponíveis, com conferência das variantes de estado e do acento de Botão.
- A sobreposição do inglês e a busca de fontes ficaram registradas como diagnóstico de calibração.
- Não houve teste dentro do jogo ou recompilação nesta fase. Git, scripts do jogo, pastas extraídas e hanafuda permaneceram fora das alterações.

Índice das comparações:

`C:/Users/Thiago/.codex/visualizations/2026/11/05/01a1ac56-1f6b-7422-a08c-bc9035480780/fha-calibracao/fase_1/comparacoes_fase_1.html`

Na mesma pasta: `previa_fase_1.png`, `resultado_final.json`, `validacao_final.txt`, `arquivos_gerados.json`, `parametros.json`, `busca_fontes.json`, `sobreposicao_ingles.png`, `revisao_01.png` a `revisao_05.png` e `resolucoes_01.png` a `resolucoes_05.png`.

### Imagem → arquivos gerados na fase 1

Caminhos relativos a `Imagens/imagens_prontas`.

| Imagem-base | Arquivos novos |
| --- | --- |
| `02_title/t_continue_1` | `pack00d_gui/02_title/t_continue_1@4x.webp`<br>`pack00m_gui/02_title/t_continue_1@2x.webp`<br>`pack00m_gui/02_title/t_continue_1.webp` |
| `02_title/t_continue_2` | `pack00d_gui/02_title/t_continue_2@4x.webp`<br>`pack00m_gui/02_title/t_continue_2@2x.webp`<br>`pack00m_gui/02_title/t_continue_2.webp` |
| `02_title/t_continue_2_1` | `pack00d_gui/02_title/t_continue_2_1@4x.webp`<br>`pack00m_gui/02_title/t_continue_2_1@2x.webp`<br>`pack00m_gui/02_title/t_continue_2_1.webp` |
| `02_title/t_continue_3` | `pack00d_gui/02_title/t_continue_3@4x.webp`<br>`pack00m_gui/02_title/t_continue_3@2x.webp`<br>`pack00m_gui/02_title/t_continue_3.webp` |
| `02_title/t_continue_4` | `pack00d_gui/02_title/t_continue_4@4x.webp` |
| `02_title/t_entrance_1` | `pack00d_gui/02_title/t_entrance_1@4x.webp`<br>`pack00m_gui/02_title/t_entrance_1@2x.webp`<br>`pack00m_gui/02_title/t_entrance_1.webp` |
| `02_title/t_entrance_2` | `pack00d_gui/02_title/t_entrance_2@4x.webp`<br>`pack00m_gui/02_title/t_entrance_2@2x.webp`<br>`pack00m_gui/02_title/t_entrance_2.webp` |
| `02_title/t_entrance_2_1` | `pack00d_gui/02_title/t_entrance_2_1@4x.webp`<br>`pack00m_gui/02_title/t_entrance_2_1@2x.webp`<br>`pack00m_gui/02_title/t_entrance_2_1.webp` |
| `02_title/t_entrance_3` | `pack00d_gui/02_title/t_entrance_3@4x.webp`<br>`pack00m_gui/02_title/t_entrance_3@2x.webp`<br>`pack00m_gui/02_title/t_entrance_3.webp` |
| `02_title/t_exit_1` | `pack00d_gui/02_title/t_exit_1@4x.webp`<br>`pack00m_gui/02_title/t_exit_1@2x.webp`<br>`pack00m_gui/02_title/t_exit_1.webp` |
| `02_title/t_exit_2` | `pack00d_gui/02_title/t_exit_2@4x.webp`<br>`pack00m_gui/02_title/t_exit_2@2x.webp`<br>`pack00m_gui/02_title/t_exit_2.webp` |
| `02_title/t_exit_2_1` | `pack00d_gui/02_title/t_exit_2_1@4x.webp`<br>`pack00m_gui/02_title/t_exit_2_1@2x.webp`<br>`pack00m_gui/02_title/t_exit_2_1.webp` |
| `02_title/t_exit_3` | `pack00d_gui/02_title/t_exit_3@4x.webp`<br>`pack00m_gui/02_title/t_exit_3@2x.webp`<br>`pack00m_gui/02_title/t_exit_3.webp` |
| `02_title/t_exit_4` | `pack00d_gui/02_title/t_exit_4@4x.webp` |
| `02_title/t_gallery_1` | `pack00d_gui/02_title/t_gallery_1@4x.webp`<br>`pack00m_gui/02_title/t_gallery_1@2x.webp`<br>`pack00m_gui/02_title/t_gallery_1.webp` |
| `02_title/t_gallery_2` | `pack00d_gui/02_title/t_gallery_2@4x.webp`<br>`pack00m_gui/02_title/t_gallery_2@2x.webp`<br>`pack00m_gui/02_title/t_gallery_2.webp` |
| `02_title/t_gallery_2_1` | `pack00d_gui/02_title/t_gallery_2_1@4x.webp`<br>`pack00m_gui/02_title/t_gallery_2_1@2x.webp`<br>`pack00m_gui/02_title/t_gallery_2_1.webp` |
| `02_title/t_gallery_3` | `pack00d_gui/02_title/t_gallery_3@4x.webp`<br>`pack00m_gui/02_title/t_gallery_3@2x.webp`<br>`pack00m_gui/02_title/t_gallery_3.webp` |
| `02_title/t_special_4` | `pack00d_gui/02_title/t_special_4@4x.webp`<br>`pack00m_gui/02_title/t_special_4@2x.webp`<br>`pack00m_gui/02_title/t_special_4.webp` |
| `02_title/t_newgame_1` | `pack00d_gui/02_title/t_newgame_1@4x.webp`<br>`pack00m_gui/02_title/t_newgame_1@2x.webp`<br>`pack00m_gui/02_title/t_newgame_1.webp` |
| `02_title/t_newgame_2` | `pack00d_gui/02_title/t_newgame_2@4x.webp`<br>`pack00m_gui/02_title/t_newgame_2@2x.webp`<br>`pack00m_gui/02_title/t_newgame_2.webp` |
| `02_title/t_newgame_2_1` | `pack00d_gui/02_title/t_newgame_2_1@4x.webp`<br>`pack00m_gui/02_title/t_newgame_2_1@2x.webp`<br>`pack00m_gui/02_title/t_newgame_2_1.webp` |
| `02_title/t_newgame_3` | `pack00d_gui/02_title/t_newgame_3@4x.webp`<br>`pack00m_gui/02_title/t_newgame_3@2x.webp`<br>`pack00m_gui/02_title/t_newgame_3.webp` |
| `02_title/t_newgame_4` | `pack00d_gui/02_title/t_newgame_4@4x.webp` |
| `02_title/t_press_1` | `pack00d_gui/02_title/t_press_1@4x.webp`<br>`pack00m_gui/02_title/t_press_1@2x.webp`<br>`pack00m_gui/02_title/t_press_1.webp` |
| `02_title/t_press_2` | `pack00d_gui/02_title/t_press_2@4x.webp`<br>`pack00m_gui/02_title/t_press_2@2x.webp`<br>`pack00m_gui/02_title/t_press_2.webp` |
| `02_title/t_press_2_1` | `pack00d_gui/02_title/t_press_2_1@4x.webp`<br>`pack00m_gui/02_title/t_press_2_1@2x.webp`<br>`pack00m_gui/02_title/t_press_2_1.webp` |
| `02_title/t_press_3` | `pack00d_gui/02_title/t_press_3@4x.webp`<br>`pack00m_gui/02_title/t_press_3@2x.webp`<br>`pack00m_gui/02_title/t_press_3.webp` |
| `02_title/t_special_1` | `pack00d_gui/02_title/t_special_1@4x.webp`<br>`pack00m_gui/02_title/t_special_1@2x.webp`<br>`pack00m_gui/02_title/t_special_1.webp` |
| `02_title/t_special_2` | `pack00d_gui/02_title/t_special_2@4x.webp`<br>`pack00m_gui/02_title/t_special_2@2x.webp`<br>`pack00m_gui/02_title/t_special_2.webp` |
| `02_title/t_special_2_1` | `pack00d_gui/02_title/t_special_2_1@4x.webp`<br>`pack00m_gui/02_title/t_special_2_1@2x.webp`<br>`pack00m_gui/02_title/t_special_2_1.webp` |
| `02_title/t_special_3` | `pack00d_gui/02_title/t_special_3@4x.webp`<br>`pack00m_gui/02_title/t_special_3@2x.webp`<br>`pack00m_gui/02_title/t_special_3.webp` |
| `07_config/07_cv_00c_us` | `pack00d_gui/07_config/07_cv_00c_us@4x.webp` |
| `07_config/07_cv_27b_us` | `pack00d_gui/07_config/07_cv_27b_us@4x.webp` |
| `07_config/07_cv_27c_us` | `pack00d_gui/07_config/07_cv_27c_us@4x.webp` |

### Próxima fase planejada

A fase 2, planejada na conclusão da fase 1, foi executada posteriormente e está registrada no início deste relatório.

---

## Etapa anterior — pasta common concluída em 05/11/2026

O responsável aprovou a calibração e autorizou a continuação até concluir a primeira pasta. O escopo desta etapa foi `common`, nos dois pacotes de menus.

- **210 arquivos novos:** 108 em `pack00m_gui/common` e 102 em `pack00d_gui/common`.
- **331 arquivos prontos em common**, cobrindo as 119 imagens-base que precisam de edição.
- As três variantes `btn_log`, `btn_log2` e `btn_log3` mantêm **LOG**, exatamente como aprovado na planilha. Não foram geradas cópias desnecessárias. Somadas às 119 imagens editadas, fecham as 122 imagens-base da pasta.
- Não há edição pendente em `common`. As resoluções ausentes no próprio original não foram inventadas.
- **365 arquivos prontos no projeto, 365 OK, zero com problema** no validador. O total de 703 originais sem cópia pronta inclui os três LOG dispensados; as demais pastas ainda não foram concluídas.
- Os **155 arquivos prontos anteriores a esta etapa**, os 1.068 originais e a planilha permaneceram inalterados, com hashes conferidos.

### Métodos e tipografia desta etapa

| Família | Fonte e tamanho de trabalho | Aplicação |
| --- | --- | --- |
| menu_* (itens) | Futura Bk BT Book, 84 px na 4x, traço afinado em 0,5 px | Gabarito das 2x do FSN onde existente. Menus novos seguem essa família; cores e brilhos são medidos nas variantes correspondentes. |
| menu_title_* | Jost variável, peso 200, 120 px nominais na 4x | Ocupação e posição ajustadas às referências FSN e às dimensões de cada título. |
| dialog_com* | Calibri Light, 92 px nominais na 4x | Texto, posição e ocupação seguem as 2x prontas. O canvas mais estreito de dialog_com6_2 foi tratado separadamente; sua 1x existente foi preservada. |
| btn_back* e config_mute* | Calibri Regular, 54 px nominais na 4x | Ícones nativos copiados. As setas de Voltar seguem a posição da referência FSN. |
| btn_logplay* e config_test* | Calibri Regular, 44 px na 4x | Triângulos, molduras e brilho do painel preservados. O texto foi substituído por Tocar ou Testar. |
| btn_autoread* e btn_title* | Arial, 12 px na única resolução existente | Duas linhas para manter legibilidade: MODO / AUTO e IR AO / TÍTULO. |
| btn_window* | Arial, 10 px | OCULTAR numa linha, preservando o ícone e o botão de 64 × 32. |
| ent_day1_us | Humnst777 Cn BT Bold, 40 px; 33 px para Depois da Escola | Oito faixas do atlas preservadas. Somente as seis previstas na planilha foram editadas; AM e PM ficaram idênticos ao original. |
| icon_savelavel_us | Calibri Regular, 43 px nominais | Só Prólogo e Dojô da Tigresa foram redesenhados. As quatro rotas com nome inalterado permanecem pixel a pixel iguais ao original na nova 4x. |
| icon_savemode_us | Arial, 28 px nominais | SAVE. RÁPIDO e SAVE. AUTO. redesenhados e rotacionados conforme a referência FSN. |
| q_title | Arial, 37 px | PERGUNTA com espaçamento por letra; símbolo de interrogação preservado. |
| sel_new1* | Arial Bold, 23 px na 2x | NOVO, com espaçamento reduzido em 1,75 px. Não existe 4x destas imagens. |

Os tamanhos acima são de renderização, antes do ajuste da ocupação às referências. As fontes são aproximações calibradas; não foi comprovada a identidade exata de todas as fontes históricas. Não se ampliou nenhum bitmap 2x para produzir uma textura 4x.

### Ajustes de encaixe e reconstrução

- MODO AUTO e IR AO TÍTULO mantêm as duas linhas do tipo original de botão; o texto aprovado não foi alterado.
- OCULTAR usa corpo menor para caber sem invadir o ícone.
- Tocar e Testar usam corpo ajustado e espaçamento de -1 px e -1,5 px, respectivamente.
- Depois da Escola usa 33 px e espaçamento de -2 px para caber na faixa sem corte.
- NOVO usa 23 px e espaçamento de -1,75 px para preservar margens no botão pequeno.
- O fundo atrás do inglês foi reconstruído somente nos painéis dos botões Play/Test, nos dois selos de rota editados e nos painéis verticais dos modos de salvamento. A reconstrução usa o degradê ou as linhas limpas do próprio painel; não houve intervenção sobre CGs nesta etapa.
- Os brilhos azuis, rosas e vermelhos foram ajustados por variante. As versões menores novas foram reduzidas com LANCZOS e alfa pré-multiplicado. Elementos gráficos preservados foram restaurados a partir do original da própria resolução para evitar alterações causadas pelo filtro.

### Conferência e comparações

- Validação de nome, caminho, dimensões, RGBA, WebP sem perda e ausência de EXIF/XMP nos 210 arquivos novos.
- Comparação das 119 imagens editadas em 10 folhas de conjunto de original/resultado e 10 folhas das resoluções disponíveis, em fundos claro e escuro.
- **119 folhas individuais** também estão disponíveis, com original e PT-BR lado a lado em tamanho nativo, nas resoluções existentes e sobre fundos claro e escuro.
- Conferência pixel a pixel dos triângulos dos 36 arquivos Play/Test, das faixas AM/PM e das rotas não alteradas na nova 4x.
- Conferência por hashes dos arquivos anteriores e da planilha.
- Não houve teste dentro do jogo, recompilação, Git ou alterações nas pastas extraídas e nos scripts do jogo.

Índice das comparações:

`C:/Users/Thiago/.codex/visualizations/2026/11/05/01a1ac56-1f6b-7422-a08c-bc9035480780/fha-calibracao/common/comparacoes_common.html`

Na mesma pasta: `previa_common.png`, `resultado_final.json`, `validacao_final.txt`, `arquivos_gerados_common.json`, `parametros_common.json`, `revisao_01.png` a `revisao_10.png` e `resolucoes_01.png` a `resolucoes_10.png`.

### Imagem → arquivos gerados nesta etapa

Os caminhos abaixo são relativos a `Imagens/imagens_prontas`.

| Imagem-base | Arquivos novos |
| --- | --- |
| `btn_autoread` | `pack00m_gui/common/btn_autoread.webp` |
| `btn_autoread2` | `pack00m_gui/common/btn_autoread2.webp` |
| `btn_autoread3` | `pack00m_gui/common/btn_autoread3.webp` |
| `btn_back` | `pack00d_gui/common/btn_back@4x.webp` |
| `btn_back2` | `pack00d_gui/common/btn_back2@4x.webp` |
| `btn_back3` | `pack00d_gui/common/btn_back3@4x.webp` |
| `btn_back2@v1` | `pack00d_gui/common/btn_back2@v1@4x.webp`<br>`pack00m_gui/common/btn_back2@v1@2x.webp`<br>`pack00m_gui/common/btn_back2@v1.webp` |
| `btn_back3@v1` | `pack00d_gui/common/btn_back3@v1@4x.webp`<br>`pack00m_gui/common/btn_back3@v1@2x.webp`<br>`pack00m_gui/common/btn_back3@v1.webp` |
| `btn_back@v1` | `pack00d_gui/common/btn_back@v1@4x.webp`<br>`pack00m_gui/common/btn_back@v1@2x.webp`<br>`pack00m_gui/common/btn_back@v1.webp` |
| `btn_logplay` | `pack00d_gui/common/btn_logplay@4x.webp`<br>`pack00m_gui/common/btn_logplay@2x.webp`<br>`pack00m_gui/common/btn_logplay.webp` |
| `btn_logplay@v1` | `pack00d_gui/common/btn_logplay@v1@4x.webp`<br>`pack00m_gui/common/btn_logplay@v1@2x.webp`<br>`pack00m_gui/common/btn_logplay@v1.webp` |
| `btn_logplay_on` | `pack00d_gui/common/btn_logplay_on@4x.webp`<br>`pack00m_gui/common/btn_logplay_on@2x.webp`<br>`pack00m_gui/common/btn_logplay_on.webp` |
| `btn_logplay_on@v1` | `pack00d_gui/common/btn_logplay_on@v1@4x.webp`<br>`pack00m_gui/common/btn_logplay_on@v1@2x.webp`<br>`pack00m_gui/common/btn_logplay_on@v1.webp` |
| `btn_logplay_sel` | `pack00d_gui/common/btn_logplay_sel@4x.webp`<br>`pack00m_gui/common/btn_logplay_sel@2x.webp`<br>`pack00m_gui/common/btn_logplay_sel.webp` |
| `btn_logplay_sel@v1` | `pack00d_gui/common/btn_logplay_sel@v1@4x.webp`<br>`pack00m_gui/common/btn_logplay_sel@v1@2x.webp`<br>`pack00m_gui/common/btn_logplay_sel@v1.webp` |
| `btn_title` | `pack00m_gui/common/btn_title.webp` |
| `btn_title2` | `pack00m_gui/common/btn_title2.webp` |
| `btn_title3` | `pack00m_gui/common/btn_title3.webp` |
| `btn_window` | `pack00m_gui/common/btn_window.webp` |
| `btn_window2` | `pack00m_gui/common/btn_window2.webp` |
| `btn_window3` | `pack00m_gui/common/btn_window3.webp` |
| `config_mute_us` | `pack00d_gui/common/config_mute_us@4x.webp` |
| `config_muteon_us` | `pack00d_gui/common/config_muteon_us@4x.webp` |
| `config_mutesel_us` | `pack00d_gui/common/config_mutesel_us@4x.webp` |
| `config_mute_us@v1` | `pack00d_gui/common/config_mute_us@v1@4x.webp`<br>`pack00m_gui/common/config_mute_us@v1@2x.webp`<br>`pack00m_gui/common/config_mute_us@v1.webp` |
| `config_muteon_us@v1` | `pack00d_gui/common/config_muteon_us@v1@4x.webp`<br>`pack00m_gui/common/config_muteon_us@v1@2x.webp`<br>`pack00m_gui/common/config_muteon_us@v1.webp` |
| `config_mutesel_us@v1` | `pack00d_gui/common/config_mutesel_us@v1@4x.webp`<br>`pack00m_gui/common/config_mutesel_us@v1@2x.webp`<br>`pack00m_gui/common/config_mutesel_us@v1.webp` |
| `config_test` | `pack00d_gui/common/config_test@4x.webp`<br>`pack00m_gui/common/config_test@2x.webp`<br>`pack00m_gui/common/config_test.webp` |
| `config_test@v1` | `pack00d_gui/common/config_test@v1@4x.webp`<br>`pack00m_gui/common/config_test@v1@2x.webp`<br>`pack00m_gui/common/config_test@v1.webp` |
| `config_teston` | `pack00d_gui/common/config_teston@4x.webp`<br>`pack00m_gui/common/config_teston@2x.webp`<br>`pack00m_gui/common/config_teston.webp` |
| `config_teston@v1` | `pack00d_gui/common/config_teston@v1@4x.webp`<br>`pack00m_gui/common/config_teston@v1@2x.webp`<br>`pack00m_gui/common/config_teston@v1.webp` |
| `config_testsel` | `pack00d_gui/common/config_testsel@4x.webp`<br>`pack00m_gui/common/config_testsel@2x.webp`<br>`pack00m_gui/common/config_testsel.webp` |
| `config_testsel@v1` | `pack00d_gui/common/config_testsel@v1@4x.webp`<br>`pack00m_gui/common/config_testsel@v1@2x.webp`<br>`pack00m_gui/common/config_testsel@v1.webp` |
| `dialog_com2_1` | `pack00d_gui/common/dialog_com2_1@4x.webp` |
| `dialog_com2_2` | `pack00d_gui/common/dialog_com2_2@4x.webp` |
| `dialog_com2_3` | `pack00d_gui/common/dialog_com2_3@4x.webp` |
| `dialog_com3_1@v1` | `pack00d_gui/common/dialog_com3_1@v1@4x.webp` |
| `dialog_com3_2` | `pack00d_gui/common/dialog_com3_2@4x.webp` |
| `dialog_com3_3` | `pack00d_gui/common/dialog_com3_3@4x.webp` |
| `dialog_com3_3@v1` | `pack00d_gui/common/dialog_com3_3@v1@4x.webp`<br>`pack00m_gui/common/dialog_com3_3@v1@2x.webp`<br>`pack00m_gui/common/dialog_com3_3@v1.webp` |
| `dialog_com4_1` | `pack00d_gui/common/dialog_com4_1@4x.webp` |
| `dialog_com4_2` | `pack00d_gui/common/dialog_com4_2@4x.webp` |
| `dialog_com4_3` | `pack00d_gui/common/dialog_com4_3@4x.webp` |
| `dialog_com4_1@v1` | `pack00d_gui/common/dialog_com4_1@v1@4x.webp`<br>`pack00m_gui/common/dialog_com4_1@v1.webp` |
| `dialog_com4_3@v1` | `pack00d_gui/common/dialog_com4_3@v1@4x.webp`<br>`pack00m_gui/common/dialog_com4_3@v1@2x.webp`<br>`pack00m_gui/common/dialog_com4_3@v1.webp` |
| `dialog_com5_1` | `pack00d_gui/common/dialog_com5_1@4x.webp` |
| `dialog_com5_2` | `pack00d_gui/common/dialog_com5_2@4x.webp` |
| `dialog_com5_3` | `pack00d_gui/common/dialog_com5_3@4x.webp` |
| `dialog_com6_1` | `pack00d_gui/common/dialog_com6_1@4x.webp` |
| `dialog_com6_2` | `pack00d_gui/common/dialog_com6_2@4x.webp` |
| `dialog_com6_3` | `pack00d_gui/common/dialog_com6_3@4x.webp` |
| `dialog_com7_1` | `pack00d_gui/common/dialog_com7_1@4x.webp` |
| `dialog_com7_2` | `pack00d_gui/common/dialog_com7_2@4x.webp` |
| `dialog_com7_3` | `pack00d_gui/common/dialog_com7_3@4x.webp` |
| `ent_day1_us` | `pack00d_gui/common/ent_day1_us@4x.webp`<br>`pack00m_gui/common/ent_day1_us@2x.webp`<br>`pack00m_gui/common/ent_day1_us.webp` |
| `icon_savelavel_us` | `pack00d_gui/common/icon_savelavel_us@4x.webp` |
| `icon_savemode_us` | `pack00d_gui/common/icon_savemode_us@4x.webp` |
| `menu_Library_1` | `pack00d_gui/common/menu_Library_1@4x.webp` |
| `menu_Library_2` | `pack00d_gui/common/menu_Library_2@4x.webp` |
| `menu_Library_3` | `pack00d_gui/common/menu_Library_3@4x.webp` |
| `menu_Picture_1` | `pack00d_gui/common/menu_Picture_1@4x.webp` |
| `menu_Picture_2` | `pack00d_gui/common/menu_Picture_2@4x.webp` |
| `menu_Picture_3` | `pack00d_gui/common/menu_Picture_3@4x.webp` |
| `menu_edlist_1` | `pack00d_gui/common/menu_edlist_1@4x.webp` |
| `menu_edlist_2` | `pack00d_gui/common/menu_edlist_2@4x.webp` |
| `menu_edlist_3` | `pack00d_gui/common/menu_edlist_3@4x.webp` |
| `menu_flow_1` | `pack00d_gui/common/menu_flow_1@4x.webp`<br>`pack00m_gui/common/menu_flow_1@2x.webp`<br>`pack00m_gui/common/menu_flow_1.webp` |
| `menu_flow_2` | `pack00d_gui/common/menu_flow_2@4x.webp`<br>`pack00m_gui/common/menu_flow_2@2x.webp`<br>`pack00m_gui/common/menu_flow_2.webp` |
| `menu_flow_2@v1` | `pack00d_gui/common/menu_flow_2@v1@4x.webp`<br>`pack00m_gui/common/menu_flow_2@v1@2x.webp`<br>`pack00m_gui/common/menu_flow_2@v1.webp` |
| `menu_flow_3` | `pack00d_gui/common/menu_flow_3@4x.webp`<br>`pack00m_gui/common/menu_flow_3@2x.webp`<br>`pack00m_gui/common/menu_flow_3.webp` |
| `menu_flow_3@v1` | `pack00d_gui/common/menu_flow_3@v1@4x.webp`<br>`pack00m_gui/common/menu_flow_3@v1@2x.webp`<br>`pack00m_gui/common/menu_flow_3@v1.webp` |
| `menu_guide_1` | `pack00d_gui/common/menu_guide_1@4x.webp` |
| `menu_guide_2` | `pack00d_gui/common/menu_guide_2@4x.webp` |
| `menu_guide_3` | `pack00d_gui/common/menu_guide_3@4x.webp` |
| `menu_guide_2@v1` | `pack00d_gui/common/menu_guide_2@v1@4x.webp`<br>`pack00m_gui/common/menu_guide_2@v1@2x.webp`<br>`pack00m_gui/common/menu_guide_2@v1.webp` |
| `menu_guide_3@v1` | `pack00d_gui/common/menu_guide_3@v1@4x.webp`<br>`pack00m_gui/common/menu_guide_3@v1@2x.webp`<br>`pack00m_gui/common/menu_guide_3@v1.webp` |
| `menu_load_1` | `pack00d_gui/common/menu_load_1@4x.webp` |
| `menu_load_2` | `pack00d_gui/common/menu_load_2@4x.webp` |
| `menu_load_3` | `pack00d_gui/common/menu_load_3@4x.webp` |
| `menu_movie_1` | `pack00d_gui/common/menu_movie_1@4x.webp` |
| `menu_movie_2` | `pack00d_gui/common/menu_movie_2@4x.webp` |
| `menu_movie_3` | `pack00d_gui/common/menu_movie_3@4x.webp` |
| `menu_music_1` | `pack00d_gui/common/menu_music_1@4x.webp` |
| `menu_music_2` | `pack00d_gui/common/menu_music_2@4x.webp` |
| `menu_music_3` | `pack00d_gui/common/menu_music_3@4x.webp` |
| `menu_return_1` | `pack00d_gui/common/menu_return_1@4x.webp`<br>`pack00m_gui/common/menu_return_1@2x.webp`<br>`pack00m_gui/common/menu_return_1.webp` |
| `menu_return_2` | `pack00m_gui/common/menu_return_2@2x.webp`<br>`pack00m_gui/common/menu_return_2.webp` |
| `menu_return_2@v1` | `pack00d_gui/common/menu_return_2@v1@4x.webp`<br>`pack00m_gui/common/menu_return_2@v1@2x.webp`<br>`pack00m_gui/common/menu_return_2@v1.webp` |
| `menu_return_3` | `pack00m_gui/common/menu_return_3@2x.webp`<br>`pack00m_gui/common/menu_return_3.webp` |
| `menu_return_3@v1` | `pack00d_gui/common/menu_return_3@v1@4x.webp`<br>`pack00m_gui/common/menu_return_3@v1@2x.webp`<br>`pack00m_gui/common/menu_return_3@v1.webp` |
| `menu_save_2` | `pack00d_gui/common/menu_save_2@4x.webp` |
| `menu_save_3` | `pack00d_gui/common/menu_save_3@4x.webp` |
| `menu_scene_1` | `pack00d_gui/common/menu_scene_1@4x.webp`<br>`pack00m_gui/common/menu_scene_1@2x.webp`<br>`pack00m_gui/common/menu_scene_1.webp` |
| `menu_scene_2` | `pack00d_gui/common/menu_scene_2@4x.webp`<br>`pack00m_gui/common/menu_scene_2@2x.webp`<br>`pack00m_gui/common/menu_scene_2.webp` |
| `menu_scene_3` | `pack00d_gui/common/menu_scene_3@4x.webp`<br>`pack00m_gui/common/menu_scene_3@2x.webp`<br>`pack00m_gui/common/menu_scene_3.webp` |
| `menu_serv_1` | `pack00d_gui/common/menu_serv_1@4x.webp` |
| `menu_serv_2` | `pack00d_gui/common/menu_serv_2@4x.webp` |
| `menu_serv_3` | `pack00d_gui/common/menu_serv_3@4x.webp` |
| `menu_title_3` | `pack00d_gui/common/menu_title_3@4x.webp` |
| `menu_title_4` | `pack00d_gui/common/menu_title_4@4x.webp` |
| `menu_title_5` | `pack00d_gui/common/menu_title_5@4x.webp` |
| `menu_title_6` | `pack00d_gui/common/menu_title_6@4x.webp`<br>`pack00m_gui/common/menu_title_6@2x.webp`<br>`pack00m_gui/common/menu_title_6.webp` |
| `menu_title_7` | `pack00d_gui/common/menu_title_7@4x.webp`<br>`pack00m_gui/common/menu_title_7@2x.webp`<br>`pack00m_gui/common/menu_title_7.webp` |
| `menu_to_title_1` | `pack00d_gui/common/menu_to_title_1@4x.webp`<br>`pack00m_gui/common/menu_to_title_1@2x.webp`<br>`pack00m_gui/common/menu_to_title_1.webp` |
| `menu_to_title_1@v1` | `pack00d_gui/common/menu_to_title_1@v1@4x.webp`<br>`pack00m_gui/common/menu_to_title_1@v1@2x.webp`<br>`pack00m_gui/common/menu_to_title_1@v1.webp` |
| `menu_to_title_2` | `pack00d_gui/common/menu_to_title_2@4x.webp`<br>`pack00m_gui/common/menu_to_title_2@2x.webp`<br>`pack00m_gui/common/menu_to_title_2.webp` |
| `menu_to_title_2@v1` | `pack00d_gui/common/menu_to_title_2@v1@4x.webp`<br>`pack00m_gui/common/menu_to_title_2@v1@2x.webp`<br>`pack00m_gui/common/menu_to_title_2@v1.webp` |
| `menu_to_title_3` | `pack00d_gui/common/menu_to_title_3@4x.webp`<br>`pack00m_gui/common/menu_to_title_3@2x.webp`<br>`pack00m_gui/common/menu_to_title_3.webp` |
| `menu_to_title_3@v1` | `pack00d_gui/common/menu_to_title_3@v1@4x.webp`<br>`pack00m_gui/common/menu_to_title_3@v1@2x.webp`<br>`pack00m_gui/common/menu_to_title_3@v1.webp` |
| `menu_wep_1` | `pack00d_gui/common/menu_wep_1@4x.webp` |
| `menu_wep_2` | `pack00d_gui/common/menu_wep_2@4x.webp` |
| `menu_wep_3` | `pack00d_gui/common/menu_wep_3@4x.webp` |
| `q_title` | `pack00d_gui/common/q_title@4x.webp`<br>`pack00m_gui/common/q_title@2x.webp`<br>`pack00m_gui/common/q_title.webp` |
| `sel_new1` | `pack00m_gui/common/sel_new1@2x.webp`<br>`pack00m_gui/common/sel_new1.webp` |
| `sel_new1@v1` | `pack00m_gui/common/sel_new1@v1@2x.webp`<br>`pack00m_gui/common/sel_new1@v1.webp` |
| `sel_new1sel` | `pack00m_gui/common/sel_new1sel@2x.webp`<br>`pack00m_gui/common/sel_new1sel.webp` |
| `sel_new1sel@v1` | `pack00m_gui/common/sel_new1sel@v1@2x.webp`<br>`pack00m_gui/common/sel_new1sel@v1.webp` |

### Continuação

A etapa termina em `common`, conforme solicitado. As outras pastas de menus e os pacotes de cenas permanecem para as próximas etapas. Hanafuda continua fora do escopo.

---

## 05/11/2026 — calibração inicial

**Registro histórico:** as duas amostras desta calibração foram avaliadas e aprovadas antes da conclusão de `common`, descrita acima.

O texto foi lido da coluna **Sugestão PT-BR** da planilha revisada, sem alterações. Os 1.068 arquivos originais estão mapeados pela planilha. Há 1.011 linhas de texto, sem células vazias na coluna de tradução.

### Arquivos gerados

| Imagem | Texto | Arquivo em imagens_prontas | Canvas | Formato |
| --- | --- | --- | --- | --- |
| common/menu_save_1 | Salvar | pack00d_gui/common/menu_save_1@4x.webp | 960 × 192 | WebP sem perda, VP8L, RGBA |
| common/dialog_com3_1 | Sim | pack00d_gui/common/dialog_com3_1@4x.webp | 360 × 168 | WebP sem perda, VP8L, RGBA |

As versões 1x e 2x já existentes permaneceram intactas. As letras foram renderizadas novamente a partir de fontes vetoriais; os bitmaps de referência não foram ampliados para gerar os arquivos de saída.

### Tipografia e medidas das amostras

| Família/amostra | Fonte usada | Tamanho nominal na 4x | Ajustes |
| --- | --- | --- | --- |
| Menu / Salvar | Futura Bk BT Book, de C:/Windows/Fonts/Futura Bk BT Book.ttf | 84 px | Traço afinado em 0,5 px; ocupação ajustada a 222 × 64 px, em x=60, y=60; degradê horizontal de opacidade branco reproduzido a partir do modelo medido no FSN. |
| Diálogo / Sim | Calibri Light, de C:/Windows/Fonts/calibril.ttf | 92 px | Ocupação ajustada a 110 × 60 px, em x=126, y=52; fator horizontal de aproximadamente 0,885 para corresponder à referência FSN; branco sem brilho acrescentado. |

As medidas da ocupação do texto seguem a 2x pronta multiplicada por dois. O canvas não foi redimensionado. O desenho foi feito com sobreamostragem de 4×, com redução LANCZOS. Nas comparações em escala reduzida, o alfa foi pré-multiplicado antes da redução.

Foram comparadas Jost, Futura e outras fontes disponíveis. Futura Book e Calibri Light foram as aproximações mais próximas selecionadas para estas referências específicas. **A identidade exata das fontes históricas usadas pelo FSN não foi comprovada.** A sobreposição do inglês também apresenta diferenças; estas amostras priorizam o gabarito em português do FSN, conforme a regra das imagens já prontas. A escolha ainda depende da avaliação visual do responsável antes de ser aplicada à família inteira.

Não houve redução de fonte para acomodar uma tradução longa nestas duas amostras. O ajuste de largura de “Sim” reproduz a ocupação da referência existente, sem alterar seu texto. Nenhuma arte precisou ser reconstruída. Nenhuma destas duas imagens tem todos os textos iguais ao inglês.

Os estados coloridos e seus brilhos, as demais famílias e os acentos ainda não foram calibrados nesta etapa. As duas palavras escolhidas não contêm acentos.

### Conferência

- Antes da edição: 153 arquivos conferidos, 153 OK, zero com problema.
- Após a edição: **155 arquivos conferidos, 155 OK, zero com problema** em `validar_prontas.py`.
- Saída sem EXIF e sem XMP, com dimensões e modo de cor iguais aos originais; os dois originais não possuem perfil ICC.
- Verificação de hashes: os 1.068 originais, os 153 arquivos anteriormente prontos e a planilha permaneceram inalterados.
- Originais e resultados comparados nas resoluções 1x, 2x e 4x, sobre fundos claro e escuro. A nova 4x também foi reduzida somente para inspeção ao lado da 2x de referência.
- A validação realizada cobre os arquivos e a comparação visual; não houve teste dentro do jogo.

As folhas de comparação, os parâmetros e a lista integral de pendências estão em:

`C:/Users/Thiago/.codex/visualizations/2026/11/05/01a1ac56-1f6b-7422-a08c-bc9035480780/fha-calibracao/`

Arquivos de conferência principais:

- `comparacao_menu_save_1.png`: original e PT-BR nas três resoluções, em fundos claro e escuro.
- `comparacao_dialog_com3_1.png`: original e PT-BR nas três resoluções, em fundos claro e escuro.
- `detalhe_menu_save_1.png` e `detalhe_dialog_com3_1.png`: comparação da 2x existente com a nova 4x exibida em 2x.
- `sobreposicao_ingles.png`: diagnóstico das diferenças entre o inglês original e as fontes candidatas.
- `estado_inicial.json`: hashes anteriores à edição.
- `parametros_finais.json`: medidas de reprodução das duas amostras.
- `validacao_e_pendencias.txt`: resultado do validador com `--faltando`.

### Pendências

O validador lista **913 arquivos originais ainda sem versão pronta**. Essa contagem inclui arquivos cuja necessidade de geração deverá ser reavaliada quando todos os textos da respectiva imagem forem idênticos ao inglês.

Próximo passo: avaliar as duas amostras e ajustar a calibração se necessário, antes de produzir os demais menus e suas variantes. Hanafuda permanece fora desta leva. Não houve uso de Git nem alterações nas pastas extraídas ou nos scripts do jogo.
