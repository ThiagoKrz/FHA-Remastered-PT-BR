# Padrão de Tradução Type-Moon para Profiles de Servos Atlas

Este é o prompt canônico do projeto para traduzir profiles de Servos extraídos da Atlas Academy em arquivos `.ts`, com foco em páginas de leitura no Fate Café.

## Leitura obrigatória antes de agir

Leia nesta ordem:

1. `standards/type-moon/GLOSSARIO_TYPEMOON_OPERACIONAL.json`
2. `standards/type-moon/README.md`
3. `standards/type-moon/PROMPT_TRADUCAO_TYPEMOON_EPUB.md`
4. `standards/type-moon/PROMPT_TRADUCAO_TYPEMOON_PROFILE_SERVOS_ATLAS.md`

Se houver conflito entre este prompt e o glossário, o glossário vence.

## Objetivo

Traduzir profiles de Servos vindos da Atlas Academy para PT-BR natural, preservando:

- a estrutura TypeScript dos arquivos;
- os IDs e campos técnicos usados pelo frontend;
- as imagens e assets já extraídos;
- a padronização Type-Moon do projeto.

Este fluxo existe para arquivos como:

- `src/util/data/servant-translations/*.ts`

## Escopo da tradução

Traduzir apenas os campos voltados para leitura humana no frontend:

- `profile.title`
- `profile.entries[].label`
- `profile.entries[].text`
- `assets.title`
- `assets.groups[].label`, quando necessário
- `falas.title`
- `falas.sections[].category`
- `falas.sections[].content[].label`
- `falas.sections[].content[].text`

Não traduzir ou não alterar:

- `id`
- `className`
- URLs de imagem
- estrutura de arrays e objetos
- nomes de arquivos
- chaves TypeScript
- `cv`
- `illustrator`
- parâmetros técnicos sem superfície de leitura

## Prioridades absolutas

1. O glossário é PRIORIDADE MÁXIMA.
2. Acentuação correta, integridade de caracteres e encoding limpo são prioridade crítica máxima logo abaixo do glossário.
3. Classes de Servo nunca são traduzidas.
4. PT-BR natural é obrigatório.
5. A estrutura do `.ts` é sagrada.
6. A tradução deve ser feita por etapas.
7. Ao fim de cada etapa, informar quantas faltam e pedir confirmação para seguir.

Regra inegociável de encoding:

- É proibido deixar `?` no lugar de acentos, aspas ou caracteres válidos do texto.
- Se houver qualquer indício de corrupção de encoding, mojibake ou perda de acentuação, a etapa deve ser considerada inválida até ser corrigida.
- Antes de encerrar uma etapa, revisar explicitamente se palavras em PT-BR mantiveram acentos como `não`, `história`, `região`, `gênero`, `próprio`, `coração` e equivalentes.
- Não existe “quase certo” para acentuação: se um único trecho sair com `?` indevido, a etapa falhou e precisa ser refeita/corrigida antes de seguir.

## Regras de estilo para profiles

- O texto deve soar como material de profile Type-Moon em PT-BR, não como tradução literal dura.
- Preserve o tom enciclopédico, mítico, dramático ou frio do original, conforme o Servo.
- Não simplifique lore importante.
- Não reescreva termos do glossário para “soar melhor”.
- Quando o original usar títulos de Fantasmas Nobres ou skills no corpo do texto, aplique o glossário e mantenha a legibilidade.

## Padrões locais obrigatórios

### Labels de profile

Usar estes formatos:

- `Resumo`
- `Vínculo Lv. 1`
- `Vínculo Lv. 2`
- `Vínculo Lv. 3`
- `Vínculo Lv. 4`
- `Vínculo Lv. 5`
- `Após Quest {id}`

Se houver outros gates futuros:

- manter o identificador técnico;
- traduzir o prefixo textual;
- preservar o número da quest intacto.

### Quest labels

Quando houver `Após Quest {id}`, o número deve permanecer exatamente igual ao original para permitir o link automático do frontend.

Exemplo:

- `Após Quest 4000529`

## Padrões para parâmetros e stats

Traduzir apenas o texto de leitura. Não recriar nem inventar estrutura nova.

Exemplos de tradução aceitável:

- `Height/Weight` -> `Altura/Peso`
- `Origin` -> `Origem`
- `Region` -> `Região`
- `Alignment` -> `Alinhamento`
- `Sub-Attribute` -> `Subatributo`
- `Gender` -> `Gênero`

Os valores podem ser localizados quando fizer sentido:

- `policy: lawful` -> `Leal`
- `policy: neutral` -> `Neutro`
- `policy: chaotic` -> `Caótico`
- `personality: good` -> `Bom`
- `personality: evil` -> `Mau`
- `personality: balanced` -> `Equilibrado`
- `personality: madness` -> `Louco`
- `Lawful-Good` -> `Leal e Bom`
- `Neutral-Balanced` -> `Neutro e Equilibrado`
- `Chaotic-Good` -> `Caótico e Bom`
- `Neutral-Evil` -> `Neutro e Mau`
- `Chaotic-Madness` -> `Caótico e Louco`
- `Sub-Attribute: Earth` -> `Subatributo: Terra`
- `Sub-Attribute: Sky` -> `Subatributo: Céu`
- `Sub-Attribute: Human` -> `Subatributo: Humano`
- `Sub-Attribute: Star` -> `Subatributo: Estrela`
- `Sub-Attribute: Beast` -> `Subatributo: Besta`

Padronização obrigatória:

- Nos campos crus `policy` e `personality`, salvar os valores já localizados em PT-BR.
- Em linhas corridas de profile, usar `Alinhamento: Leal e Bom`, `Alinhamento: Caótico e Mau` e equivalentes.
- Em nenhum caso deixar alinhamento ou subatributo em inglês.

## Regras para assets

- Não alterar URLs.
- Não renomear chaves `key`.
- Só traduzir `title` e `label` se isso ajudar a leitura.
- Se o projeto já usa `Assets`, manter `Assets`.

## Fluxo obrigatório

1. Ler o glossário e os prompts centrais.
2. Identificar quais Servos ou classes entram no lote.
3. Traduzir por etapas.
4. Validar tom, glossário, estrutura TS e acentuação.
5. Entregar a etapa e pedir confirmação para a próxima.

## Validação mínima por etapa

Antes de fechar uma etapa:

1. Confirmar que nenhuma classe de Servo foi traduzida.
2. Confirmar que nenhum termo do glossário foi violado.
3. Confirmar que nenhuma URL foi alterada.
4. Confirmar que a estrutura TypeScript continua válida.
5. Confirmar que o PT-BR está natural.
6. Confirmar que não existe `?` substituindo acentos, aspas ou caracteres esperados.

## Resultado esperado

O arquivo final deve:

- parecer material editorial Type-Moon em PT-BR;
- respeitar rigorosamente o glossário do Fate Café;
- continuar plugável no frontend sem retrabalho;
- servir como base confiável para extração e tradução em massa.
