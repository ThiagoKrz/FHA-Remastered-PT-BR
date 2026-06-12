# Padrão de Tradução Type-Moon para Falas de Servos Atlas

Este é o prompt canônico do projeto para traduzir a seção `voices` de Servos extraídos da Atlas Academy em arquivos `.ts`, com foco em integridade técnica do JSON e fidelidade terminológica ao universo Type-Moon.

## Leitura obrigatória antes de agir

Leia nesta ordem:

1. `standards/type-moon/GLOSSARIO_TYPEMOON_OPERACIONAL.json`
2. `standards/type-moon/README.md`
3. `standards/type-moon/PROMPT_TRADUCAO_TYPEMOON_EPUB.md`
4. `standards/type-moon/PROMPT_TRADUCAO_TYPEMOON_FALAS_ATLAS.md`

Se houver conflito entre este prompt e o glossário, o glossário vence.

## Objetivo

Traduzir a seção `voices` de Servos para PT-BR natural, preservando:

- a estrutura TypeScript dos arquivos;
- a integridade técnica de cada bloco `segments`;
- a fidelidade terminológica ao universo Type-Moon;
- a personalidade e o estilo de fala de cada personagem.

## Escopo da tradução

Traduzir apenas:

- `voices.title`
- `voices.sections[].category`
- `voices.sections[].content[].label`
- `voices.sections[].content[].segments[].text`

Não traduzir ou não alterar:

- `voices.sections[].content[].segments[].key`
- `voices.sections[].content[].audioFolder`
- `condType`, `condValues`, `additionalConds`
- estrutura de arrays e objetos
- chaves TypeScript

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

## ⚠ REGRA ABSOLUTA — NENHUMA CHAVE PODE FICAR VAZIA

**Esta é a regra de maior prioridade desta seção. Nenhuma outra regra a sobrepõe.**

- **Toda chave (`key`) existente no array `segments` DEVE ter um `text` preenchido.**
- Se o texto-fonte (EN ou JP) deixou uma chave com `""`, isso é falha da fonte, não um modelo a seguir.
- Neste caso, a tradução deve redistribuir o conteúdo da fala entre todas as chaves disponíveis, dividindo por pausas naturais de fala, pontuação ou mudança de tom.
- É proibido entregar qualquer `"text": ""` onde o original tinha conteúdo de áudio associado à chave.
- A conferência final obrigatória deve verificar explicitamente que nenhuma chave ficou vazia.

Exemplo correto (3 chaves, todas preenchidas):
```
{ "key": "0_H110", "text": "Ora, ora, Mestre, salvando a humanidade?" },
{ "key": "0_H111", "text": "Espere, você não acha que alguém da minha família está por trás disso, acha?" },
{ "key": "0_H112", "text": "N-Não, impossível, certo?" }
```

Exemplo proibido:
```
{ "key": "0_H110", "text": "Ora, ora, Mestre, salvando a humanidade?" },
{ "key": "0_H111", "text": "Espere, você não acha que alguém da minha família está por trás disso? N-Não, impossível, certo?" },
{ "key": "0_H112", "text": "" }  ← PROIBIDO
```

## Lógica de divisão de segmentos

- O número de fatias de texto traduzido deve ser **exatamente igual** ao número de chaves (`key`) fornecidas no array `segments`.
- A tradução completa de um pensamento deve ser fatiada respeitando pausas naturais de fala, pontuações ou mudanças de tela do jogo.
- Nenhuma chave pode ser removida ou adicionada ao bloco original.
- Em diálogos longos divididos em 5 ou 6 chaves (como nas falas de Vínculo ou Ascensão), a narrativa deve permanecer coesa e tecnicamente funcional.

## Padrões de labels

Usar estes formatos nas `content[].label`:

- `Vínculo Nível 1` … `Vínculo Nível 5`
- `Ascensão 1` … `Ascensão 4`
- `Aniversário`
- `Durante um Evento`
- `Diálogo 1` … `Diálogo N`
- `Batalha 1` … `Batalha N`
- outros labels: traduzir livremente mantendo clareza e consistência com o restante do arquivo

Usar estes formatos nas `sections[].category`:

- `Meu Quarto`
- `Meu Quarto (Ascensão 1)` … `Meu Quarto (Ascensão N)`
- outros: traduzir livremente mantendo fidelidade ao original

## Regras de estilo para falas

- O texto deve soar como material de fala Type-Moon em PT-BR, no estilo característico de Kinoko Nasu.
- Adaptar à personalidade do personagem que fala: tom formal, agressivo, gentil, mítico ou frio, conforme o Servo.
- Não traduzir de forma crua ou mecânica.
- Não simplificar lore importante.
- Não reescrever termos do glossário para "soar melhor".

## Regras de encoding e formatação

- Aspas japonesas (`「`, `」`, `『`, `』`) devem ser convertidas para aspas duplas padrão (`"`) com escape adequado (`\"`) para não corromper o JSON/TypeScript.
- Tags de cor (ex: `[FFff20]...[-]`), formatação de Ruby e quebras de linha (`\n`) devem ser mantidas intactas dentro do texto traduzido.
- Tolerância zero para mojibake.

## Fluxo obrigatório

1. Ler o glossário e os prompts centrais.
2. Identificar o Servo e suas seções de falas.
3. Traduzir por etapas (uma `section` por vez ou conforme combinado).
4. Validar tom, glossário, estrutura TS, segmentação e acentuação.
5. Entregar a etapa e pedir confirmação para a próxima.

## Validação mínima por etapa

Antes de fechar uma etapa:

1. **Confirmar que nenhuma chave tem `"text": ""` — varredura obrigatória em todos os segmentos entregues.**
2. Confirmar que o número de segmentos traduzidos é igual ao número de chaves originais.
3. Confirmar que nenhuma classe de Servo foi traduzida.
3. Confirmar que nenhum termo do glossário foi violado.
4. Confirmar que nenhuma chave (`key`) foi alterada, removida ou adicionada.
5. Confirmar que a estrutura TypeScript continua válida.
6. Confirmar que o PT-BR está natural e no estilo do personagem.
7. Confirmar que não existe `?` substituindo acentos, aspas ou caracteres esperados.
8. Confirmar que aspas japonesas foram convertidas corretamente.

## Resultado esperado

O arquivo final deve:

- parecer material editorial Type-Moon em PT-BR;
- respeitar rigorosamente o glossário do Fate Café;
- manter cada segmento de texto plugável no frontend sem retrabalho;
- preservar a personalidade e o estilo de fala de cada Servo.
