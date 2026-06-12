# Padrão de Revisão FSN Remastered para Scripts PT-BR

Este padrão vale para a revisão dos arquivos de `scripts_PT-BR/` de Fate/stay night Remastered.

## Prioridade

1. `standards/type-moon/GLOSSARIO_TYPEMOON_OPERACIONAL.json`
2. Este padrão de revisão de scripts `.epk_dec`
3. `standards/type-moon/README.md`
4. `standards/type-moon/PROMPT_TRADUCAO_TYPEMOON_EPUB.md`
5. `scripts_EN/` e `scripts_JP/` como referência de estrutura, contexto e sentido

Se houver conflito de termo, o glossário vence. Se houver conflito entre fluidez e estrutura da engine, preserve a estrutura e reescreva apenas o texto visível.

## Estrutura das pastas

- `scripts_JP/`: fonte japonesa original e referência principal de sentido quando a tradução em inglês estiver duvidosa.
- `scripts_EN/`: fonte inglesa e referência prática para tags, quebras e estrutura de linhas.
- `scripts_PT-BR/`: alvo de revisão. Contém os scripts traduzidos e um CSV legado de glossário.
- `standards/type-moon/GLOSSARIO_TYPEMOON_OPERACIONAL.json`: fonte de verdade para termos.

O arquivo `scripts_PT-BR/Glossário TYPE-MOON - Página1.csv` não é fonte de verdade. Use-o apenas como pista histórica quando um termo estiver ausente do JSON.

## Formato dos arquivos `.epk_dec`

Os scripts de cena seguem este formato:

```text
DAT
id=qid::label=str::text=lstr::
6538::$$$message_0056_0000_0000$$$::Texto visível aqui.::
```

Regras obrigatórias:

- A primeira linha deve ser exatamente `DAT`.
- A segunda linha deve ser exatamente `id=qid::label=str::text=lstr::`.
- Cada linha de mensagem deve manter `id`, `label`, delimitadores `::` e `::` final.
- Edite apenas o campo de texto depois do segundo `::` da linha de mensagem.
- Não altere nomes de arquivo, IDs numéricos nem labels `$$$message_...$$$`.
- Preserve a quantidade e a ordem das linhas, salvo quando o usuário pedir uma correção estrutural específica.

## Protocolo de sincronização por cena

Antes de revisar um arquivo específico pedido pelo usuário, rode:

```powershell
node tools\fsn\fsn-review-tools.mjs scene <arquivo.epk_dec>
```

O diagnóstico deve classificar a cena antes da edição:

- `OK ESTRUTURAL`: IDs, labels e ordem batem com `scripts_EN/`; seguir para revisão literária.
- `REVISÃO PONTUAL`: estrutura bate, mas há tags, termos, encoding ou linhas suspeitas; corrigir apenas os pontos apontados.
- `BUG ESTRUTURAL`: cabeçalho, linha malformada, lixo de bytes ou delimitador quebrado; corrigir estrutura antes da revisão literária.
- `DESSYNC`: contagem, labels ou ordem divergem; não revisar por cima. Usar `scripts_EN/` como esqueleto canônico e reconstruir/remapear a cena.

Regra para cenas dessincronizadas:

- Não confie apenas em `id` ou `label`.
- Compare o conteúdo visível de `scripts_EN/`, `scripts_PT-BR/` e, se necessário, `scripts_JP/`.
- Se o PT-BR veio de uma engine antiga com menos falas ou ordem diferente, preserve a estrutura do EN atual e retraduza o texto visível na ordem correta.
- Quando poucos trechos estiverem deslocados, remapeie por conteúdo e contexto antes de editar.
- Quando a cena estiver muito deslocada, refaça a cena inteira usando o EN como esqueleto e o JP como referência de sentido.

## Tags e comandos da engine

Tudo entre colchetes deve ser tratado como comando técnico, não como texto comum:

```text
[lr] [line3] [w l=3] [font italic=true] [font italic=false] [normal]
[r] [l] [wait ...] [ld ...] [chgfg ...] [move ...] [dash ...]
```

Regras:

- Não traduza parâmetros técnicos dentro de tags.
- Não traduza `storage=...`, `file=...`, `rule=...`, `bg=...` ou nomes japoneses de assets.
- Japonês dentro de tag costuma ser nome de asset/regra da engine e deve ser preservado.
- Preserve a sequência de tags da fonte EN/JP sempre que possível.
- `[lr]` é uma tag única. A forma `[l][r]` deve ser tratada como provável bug de conversão e comparada com `scripts_EN/` e `scripts_JP/` antes da correção.
- `[r]` e `[l]` isolados podem ser válidos. Não normalize de forma cega.
- Tags de ênfase como `[font italic=true]... [font italic=false]` e `[normal]` devem ser mantidas.

## Texto visível

Ao revisar, traduza e reescreva apenas o texto que o leitor vê.

Regras de estilo:

- PT-BR natural, literário e fluido, sem tradutês.
- Corrija concordância, regência, gênero, número e registro de fala.
- Preserve ritmo de fala, pausas, reticências, gritos e interrupções.
- Substitua aspas japonesas `「」『』` por aspas duplas `"`.
- Mantenha nomes próprios, honoríficos e formas de tratamento japonesas quando já forem padrão do texto: `Senpai`, `Onii-chan`, `Fuji-nee`, `-san`, `-chan`, `-sensei`.
- Não transforme uma fala formal em casual, nem uma fala casual em formal, sem motivo de personagem.

## Glossário obrigatório

Use exatamente o glossário JSON. Termos recorrentes de FSN com alta prioridade:

- `Servant` -> `Servo`
- `Master` -> `Mestre`
- `Holy Grail` -> `Santo Graal`
- `Holy Grail War` -> `Guerra do Santo Graal`
- `Noble Phantasm` -> `Fantasma Nobre`
- `True Name` -> `Nome Verdadeiro`
- `Command Spell` / `Command Seal` -> `Selo de Comando`
- `Heroic Spirit` -> `Espírito Heroico`
- `Magecraft` -> `Magia`
- `Bounded Field` -> `Campo Limitado`
- `Shadow` -> `Sombra`
- `Black Shadow` -> `Sombra Negra`
- `Projection` -> `Projeção`
- `Begin Projection` -> `Iniciar Projeção`
- `Projection magecraft` -> `Magia de Projeção`
- `Strengthening` -> `Reforço`
- `Alteration` -> `Alteração`
- `Trace` -> `Trace`
- `Grail` -> `Graal`
- `Crest Worms` -> `Vermes do Brasão`
- `Jeweled Sword` -> `Espada de Joias`
- `Azoth Blade` -> `Lâmina de Azoth`
- `Gáe Bolg` -> `Gáe Bolg`
- `Kanshou and Bakuya` -> `Kanshou e Bakuya`
- `Holy Shroud` -> `Sudário Sagrado`
- `Unlimited Blade Works` -> `Unlimited Blade Works`
- `True Magic` -> `Magia Verdadeira`
- `Blood Fort Andromeda` -> `Forte de Sangue Andrômeda`
- `Other-Seal, Blood Temple` -> `Selo de Outrem, Templo de Sangue`
- `Cup of Heaven` -> `Cálice do Céu`
- `Rho Aias` -> `Rho Aias`
- `Einzbern Grail` -> `Graal Einzbern`
- `Einzbern Castle` -> `Castelo Einzbern`
- `Einzbern Forest` -> `Floresta Einzbern`
- `Fuyuki City` -> `Cidade de Fuyuki`
- `Matou Family` -> `Família Matou`
- `Tohsaka Family` -> `Família Tohsaka`
- `Association` -> `Associação dos Magos`
- `Church` -> `Igreja`

Classes de Servo nunca são traduzidas: `Saber`, `Archer`, `Lancer`, `Rider`, `Caster`, `Assassin`, `Berserker`, `Ruler`, `Avenger`, `Moon Cancer`, `Alter-Ego`, `Foreigner`, `Pretender`, `Shielder` e `Beast`.

Capitalização:

- Use inicial maiúscula quando o termo for conceito de lore: `Servo`, `Mestre`, `Santo Graal`, `Fantasma Nobre`, `Selo de Comando`.
- Use minúscula apenas quando a palavra estiver claramente em sentido comum, não como termo técnico.
- Não faça troca cega. Se a troca quebrar a frase, reescreva a frase inteira.

## Varredura de candidatos ao glossário

Para procurar termos recorrentes de FSN que ainda podem estar ausentes do glossário operacional, rode:

```powershell
node tools\fsn\fsn-review-tools.mjs terms --top 80 --min 3
```

Regras para usar o resultado:

- O relatório é uma lista de candidatos, não autorização para adicionar tudo ao glossário.
- Priorize termos de lore, sistema, locais, armas, famílias, instituições, feitiços, artefatos e nomes próprios com risco de inconsistência.
- Ignore frases comuns, nomes sem risco real de variação e termos já cobertos pelo glossário.
- Antes de inserir qualquer termo no JSON, confirme a forma PT-BR olhando contexto em EN/JP e ocorrências já traduzidas no PT-BR.
- Se houver dúvida de padronização, registre como candidato de revisão, não como termo definitivo.

## Sinais de bug encontrados nesta pasta

Na varredura inicial desta pasta, estes problemas apareceram e devem ser priorizados em revisões futuras:

- Cabeçalho `iid=qid::label=str::text=lstr::` em vez de `id=qid::label=str::text=lstr::`.
- `[l][r]` no lugar de `[lr]`.
- Linhas com `�`, bytes de controle ou lixo depois do `::` final.
- Mojibake como `NÃÃÃÃO` ou `Ânimo`.
- Linhas ainda em inglês dentro de `scripts_PT-BR/`.
- Termos do glossário em inglês que sobraram no PT-BR.
- Termos do glossário usados com capitalização errada por tradução automática, como `servo`, `mestre`, `santo graal` em contexto de lore.
- Texto visível omitindo tags de fonte/ênfase que existem na referência.

## Checklist antes de salvar uma revisão

1. Comparar o trecho com `scripts_EN/` e, se necessário, `scripts_JP/`.
2. Confirmar que só o texto visível foi alterado.
3. Confirmar que IDs, labels, delimitadores e `::` final continuam intactos.
4. Confirmar que tags foram preservadas ou movidas apenas por necessidade real de leitura.
5. Aplicar o glossário JSON com contexto.
6. Procurar sobras de japonês fora de tags.
7. Procurar sobras de inglês indevidas.
8. Procurar `�`, `Ã`, `Â`, `[l][r]` e cabeçalho `iid=`.
9. Relatar quais linhas foram revisadas e quais problemas estruturais foram corrigidos.

## Comandos úteis de auditoria

```powershell
rg -a -n --glob "*.epk_dec" "�|Ã|Â" scripts_PT-BR
rg -a -n --glob "*.epk_dec" "\[l\]\[r\]" scripts_PT-BR
rg -a -n --glob "*.epk_dec" "^iid=qid::label=str::text=lstr::$" scripts_PT-BR
rg -a -n --glob "*.epk_dec" "[「」『』]" scripts_PT-BR
rg -a -n --glob "*.epk_dec" "\b(Servant|Master|Holy Grail|Noble Phantasm|True Name|Command Spell|Heroic Spirit|Magecraft)\b" scripts_PT-BR
```

Use `-a` no `rg` porque alguns arquivos possuem bytes corrompidos e podem ser detectados como binários.
