# Revisão da parte 1 das imagens — 08/11/2026

**Parecer:** revisão dos arquivos da parte 1 concluída. Os 1.065 arquivos são tecnicamente válidos para montar um pacote de teste. As cinco diferenças de texto entre resoluções foram corrigidas nos dez arquivos herdados, com autorização expressa e backup. A aprovação final do primeiro patch depende da montagem e do teste dentro do jogo.

## Conferência executada

| Verificação | Resultado |
| --- | --- |
| WebP decodificados e validados | 1.065 OK; zero problemas |
| Pacotes | 625 pack00m_gui; 297 pack00d_gui; 1 pack10d; 142 pack11d |
| Canvas, RGB/RGBA, codec, RIFF e ICC | Correspondem aos originais |
| EXIF/XMP acrescentados ou imagens vazias | Nenhum |
| Caminhos de destino e entradas dos bancos | 1.065 encontrados; nenhum ausente ou ambíguo |
| Originais comparados à primeira referência | 1.068 hashes iguais |
| Arquivos herdados do FSN | 143 intactos; dez substituições expressamente autorizadas, com backup |
| Alterações nesta fase | Quatro ajustes de margem e dez arquivos uniformizados, todos com backup |
| Hashes preservados desde o início da fase 8 | 2.120 de 2.134; somente as 14 alterações registradas |
| Planilha | Não alterada |
| Cobertura dos textos da planilha | 1.011 linhas associadas a originais; só LOG está dispensado |
| Inventários de produção contra a planilha atual | 1.694 registros, 998 linhas distintas |
| OCR independente | Triagem inicial de 473 versões; depois, 12 recortes dos arquivos finais alterados |
| Revisão visual direcionada | 70 arquivos em nove pranchas, mais comparações dos casos críticos e ajustes |

Os quatro registros históricos ainda escritos como Entrada pertencem ao inventário da fase 1. A correção autorizada posterior para Título foi confirmada nos arquivos atuais e na célula F4. Esses registros antigos foram preservados como histórico. As 13 linhas sem registro nos inventários por fase pertencem ao guia 08 herdado, verificado na amostra visual. O cruzamento de inventários verifica os dados de produção, não constitui leitura independente de todos os pixels. OCR tem falhas em brilhos, rotações, repetições e tipografia estilizada. Não foi tratado como aprovação automática de texto.

## Ajustes aplicados

| Arquivo | Ajuste |
| --- | --- |
| `pack00m_gui/60_endroll/149_edtext05.webp` | Texto deslocado 2 px para baixo; linha decorativa mantida pixel a pixel. |
| `pack11d/093_イリヤテロップ_us.webp` | Corpo reduzido uniformemente a 90% para acomodar contorno e sombra; margem vertical de 8 px na máscara. |
| `pack11d/143_天杯text04_us.webp` | Máscara deslocada 5 px para baixo para dar espaço ao brilho dos acentos. |
| `pack11d/121_んん_us.webp` | Hum redesenhado no mesmo tamanho, 6 px acima. Ponto de interrogação original preservado. |

As quatro versões anteriores estão em `fase_8/backup_margens`, na pasta de apoio. Os arquivos foram reabertos após a exportação sem perda e comparados com os mestres. O ponto de interrogação de Hum? e a linha decorativa da despedida foram preservados. A repetição MORRA de 怨嗟07 mantém os cortes nas extremidades, como no original.

## Textos críticos

- **Título:** confirmado nas quatro variantes 4x; as 12 versões 1x/2x/4x continuam com os hashes da correção autorizada.
- **Senhorita Artoria, vinda da Bretanha:** confirmado visualmente.
- **Obrigado. E aqui nos despedimos... desta ataraxia vazia.:** texto aprovado preservado; somente margem vertical ajustada.
- **Fio Prateado** e **O Verão das Irmãs (Maçã):** constam dos registros de produção autorizados.
- **AIinDa** e **ODdeio:** permanecem como na coluna aprovada. Não houve correção silenciosa.
- **LOG:** `btn_log`, `btn_log2` e `btn_log3` continuam dispensados; são os três faltantes brutos do validador.

## Uniformização aplicada em 08/11/2026

O usuário autorizou expressamente a exceção à regra de proteção dos arquivos herdados e pediu a máxima semelhança com o FSN pronto. Foram substituídos somente os dez WebP previstos, com backup byte a byte. As novas linhas vêm das versões 4x calibradas pelas referências do FSN, reduzidas com LANCZOS e alfa pré-multiplicado. Todo pixel fora das linhas alteradas ficou idêntico ao arquivo anterior. As setas originais dos atlas de armas foram mantidas pixel a pixel. As outras 143 imagens herdadas continuam com seus hashes originais.

| Família em 1x e 2x | Texto anterior | Texto aplicado, igual à planilha e à 4x |
| --- | --- | --- |
| day_subtitle00_us | 6 BLADE | 6 LÂMINA |
| day_subtitle01_us | 6 Faker | 6 Farsante |
| day_subtitle02_us | 10 Bosque, Bela Adormecida | 10 Bosque Escuro, Bela Adormecida |
| day_subtitle02_us | 13 LAST TALK | 13 ÚLTIMA CONVERSA |
| weptxt01_us e weptxt01sel_us | Alabarda Queima-Céu | Alabarda Incinerante do Céu |

Os dez arquivos finais foram reabertos e conferidos contra os mestres sem perda. As comparações visuais foram geradas a partir dos WebP finais, nas duas resoluções. O OCR reconheceu dez dos 12 recortes; não reconheceu as duas versões de 6 LÂMINA, que foram confirmadas visualmente. Os 2.124 outros hashes da conferência imediatamente anterior à uniformização permaneceram iguais. Os dez backups estão em `fase_8/backup_uniformizacao` na pasta de apoio.

## Teste obrigatório antes da publicação

A montagem, instalação e execução do patch não foram feitas nesta fase. O mapeamento de arquivos não comprova a aceitação do pacote pelo jogo.

1. Montar em staging separado, preservando as extrações originais. Menus seguem os caminhos completos de textures. pack10d e pack11d precisam do banco DAT e do índice fileinfo correspondente, levados juntos ao pacote.
2. Conferir os arquivos extraídos do pacote de teste contra o manifesto. Guardar o SHA-256 do pacote efetivamente instalado.
3. No jogo, testar título, seleção de saves e o retorno **Título**, com estados normal/selecionado/pressionado. Confirmar que a ação realmente retorna ao menu inicial.
4. Conferir as resoluções/escala de interface disponíveis: listas de capítulos, armas, glossário, música, galeria, mapa e guias. Incluir os dez arquivos uniformizados listados acima.
5. Conferir nas cenas: Artoria e Illyasviel, textos invertidos, os nove efeitos RPG, Hum?, DIA 1–4, diagrama de Rin, cartas, santuário, quiz e telas de Himuro.
6. Conferir os créditos, incluindo a despedida, e as telas de encerramento. Avaliar leitura, recorte e contraste sobre o fundo real.
7. Fechar e reabrir o jogo com o mesmo pacote, repetir carregar/salvar e registrar eventuais defeitos por cena e resolução.

Algumas fontes são aproximações documentadas nas fases anteriores. A revisão desta fase não comprova identidade exata com as fontes originais. Hanafuda, scripts e extrações continuam fora das alterações.

## Evidências

- [Manifesto dos arquivos atuais](manifesto_parte_1.json).
- [Catálogo completo com originais e fundo claro/escuro](C:/Users/Thiago/.codex/visualizations/2026/11/05/01a1ac56-1f6b-7422-a08c-bc9035480780/fha-calibracao/fase_8/revisao_parte_1.html).
- [Comparação da uniformização aplicada](C:/Users/Thiago/.codex/visualizations/2026/11/05/01a1ac56-1f6b-7422-a08c-bc9035480780/fha-calibracao/fase_8/uniformizacao_aplicada.png).
- [Resultado detalhado](C:/Users/Thiago/.codex/visualizations/2026/11/05/01a1ac56-1f6b-7422-a08c-bc9035480780/fha-calibracao/fase_8/resultado_final.json).
- [Mapa de empacotamento](C:/Users/Thiago/.codex/visualizations/2026/11/05/01a1ac56-1f6b-7422-a08c-bc9035480780/fha-calibracao/fase_8/mapa_empacotamento.json).

O catálogo abre os 1.065 WebP atuais. As pranchas são provas de revisão, não capturas do jogo. O manifesto e o mapa de empacotamento foram atualizados depois das dez substituições.
