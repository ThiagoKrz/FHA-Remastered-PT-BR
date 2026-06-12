# Guia Operacional Type-Moon para EPUBs e Publicação no Site

Esta pasta concentra o padrão oficial do projeto para tradução, validação, recompilação e publicação de EPUBs Type-Moon no site.

## Leitura obrigatória para LLMs

Ordem de leitura e prioridade:

1. `standards/type-moon/GLOSSARIO_TYPEMOON_OPERACIONAL.json`
2. `standards/type-moon/README.md`
3. `standards/type-moon/PROMPT_TRADUCAO_TYPEMOON_EPUB.md`

Para revisão dos scripts `.epk_dec` de Fate/stay night Remastered, leia também:

4. `standards/type-moon/PROMPT_REVISAO_FSN_REMASTERED_SCRIPTS.md`

Regra de conflito:

- Se houver conflito entre o prompt e o glossário, o glossário vence.
- Se houver conflito entre um workbench local e este guia central, este guia central vence.
- Se houver conflito entre o padrão específico de FSN Remastered e o glossário, o glossário vence.
- Instruções específicas da tarefa atual só podem complementar o padrão, nunca derrubar o glossário.
- Integridade de caracteres, acentuação correta e ausência de mojibake são obrigatórias em qualquer etapa de tradução.

## Objetivo deste padrão

Este padrão existe para garantir que qualquer LLM consiga repetir o mesmo processo, com consistência, em volumes e novels diferentes:

- preparar um workbench de tradução sem quebrar o EPUB;
- mapear termos novos da obra ou da Type-Moon antes da tradução e registrar a padronização no glossário do projeto;
- traduzir por etapas controladas;
- validar a tradução em cada etapa;
- sincronizar a tradução de volta ao pacote do EPUB;
- normalizar metadados e navegação para leitura em PT-BR;
- recompilar o EPUB;
- publicar o EPUB final no site;
- manter o runtime do site independente do workbench;
- permitir a exclusão futura dos workbenches sem quebrar o projeto publicado.

## Arquivos centrais

Documentos:

- `standards/type-moon/GLOSSARIO_TYPEMOON_OPERACIONAL.json`
- `standards/type-moon/README.md`
- `standards/type-moon/PROMPT_TRADUCAO_TYPEMOON_EPUB.md`
- `standards/type-moon/PROMPT_REVISAO_FSN_REMASTERED_SCRIPTS.md`

Scripts do pipeline:

- `tools/novels/prepare-epub-workbench.ps1`
- `tools/novels/preserve-pdf-illustrations.py`
- `tools/novels/sync-epub-translation.ps1`
- `tools/novels/rebuild-epub.ps1`

Ferramentas de apoio para FSN Remastered:

- `tools/fsn/fsn-review-tools.mjs`

Ponto atual de leitura do site:

- `src/util/data/novels.ts`

## Contrato canônico do repositório

### 1. O workbench é temporário

Tudo em `novel-workbench/...` é área de trabalho temporária:

- `package/` existe para extração, revisão, sync e rebuild;
- `translation/original-html/` existe para referência;
- `translation/translated-html/` existe para edição da tradução;
- `translation/plaintext/` existe para apoio de leitura e prompting;
- `build/` existe para gerar o `.epub` recompilado.

O workbench não pode virar dependência do runtime do site.

### 2. O runtime do site deve depender apenas dos assets publicados

Hoje, a publicação final que o site lê deve estar resolvida a partir de `src/assets/...` e do módulo de dados do frontend.

Contrato atual de publicação:

- `src/assets/<Autor>/<Pasta do volume>/cover.jpg`
- `src/assets/<Autor>/<Pasta do volume>/metadata.opf`
- `src/assets/<Autor>/<Pasta do volume>/*.ptbr-sample.epub`

O leitor do site não deve buscar conteúdo dentro de `novel-workbench/...`.

### 3. O nome do EPUB traduzido é padronizado

O EPUB final traduzido deve reaproveitar o nome-base do EPUB de origem e receber o sufixo:

- `.ptbr-sample.epub`

Exemplo:

- origem: `Fate_Apocrypha Vol. 1 - Yuuichiro Higashide.epub`
- publicado: `Fate_Apocrypha Vol. 1 - Yuuichiro Higashide.ptbr-sample.epub`

### 4. `metadata.opf` do asset e `content.opf` do pacote não têm o mesmo papel

Diferença importante:

- `src/assets/.../metadata.opf` alimenta o catálogo do site;
- `novel-workbench/.../package/content.opf` alimenta o EPUB recompilado.

Ou seja:

- o `content.opf` do pacote publicado em PT-BR deve ser normalizado para leitura ocidental;
- o `metadata.opf` do asset pode continuar representando o idioma/base bibliográfica original se essa for a intenção do catálogo.

### 5. A exclusão futura do workbench é parte do plano

Ao final da tradução de todos os volumes de uma novel:

- os workbenches poderão ser apagados;
- o site deverá continuar funcionando só com os assets publicados e o módulo de dados correspondente;
- nenhuma tela do frontend deve depender de `manifest.json`, `translated-html/`, `package/` ou qualquer arquivo de workbench.

Se no futuro o projeto migrar para um modelo estritamente EPUB-only, a mudança deve ser concentrada no módulo de descoberta de dados do frontend, não espalhada pela UI.

## Fluxo operacional detalhado

### Etapa 0. Preparar o workbench

Objetivo:

- extrair o EPUB;
- gerar cópias ordenadas dos HTML/XHTML do spine;
- gerar plaintext auxiliar;
- registrar tudo em um `manifest.json`.

Comando canônico:

```powershell
powershell -File tools/novels/prepare-epub-workbench.ps1 `
  -SourceEpub "src\assets\<Autor>\<Pasta do volume>\<Arquivo>.epub" `
  -WorkRoot "novel-workbench\<serie>\<volume>"
```

Ao final desta etapa devem existir:

- `package/`
- `translation/original-html/`
- `translation/translated-html/`
- `translation/plaintext/`
- `build/`
- `manifest.json`

### Etapa 0.5. Preservar ilustrações quando a origem for PDF

Se a obra tiver sido importada de PDF em vez de EPUB nativo, a LLM deve preservar antes da tradução:

- páginas de ilustração;
- cartões de classe, character sheets e equivalentes;
- inserts visuais relevantes para leitura do volume;
- a ordem original dessas páginas dentro do fluxo do livro.

Comando canônico:

```powershell
python tools/novels/preserve-pdf-illustrations.py `
  --manifest-path "novel-workbench\<serie>\<volume>\manifest.json"
```

Regras:

- essa etapa acontece antes da triagem de termos e antes da primeira etapa de tradução;
- as ilustrações não podem ser anexadas fora de ordem ou jogadas no fim do EPUB;
- o objetivo não é só "copiar imagens", mas reconstruir o volume com os inserts visuais no ponto correto do fluxo;
- páginas visuais de abertura que compartilhem o mesmo bloco da capa no PDF devem virar arquivos XHTML próprios no spine do EPUB, para evitar vazamento entre páginas no leitor;
- quando uma página visual precisar ocupar uma página inteira no leitor, o padrão preferido é criar um documento XHTML dedicado para ela no spine, em vez de confiar apenas em quebra por CSS;
- a ordem final do EPUB deve espelhar a ordem do PDF, inclusive na abertura, no miolo e no fim;
- quando o mapeamento automático não for suficiente, registrar os pages escolhidos no `manifest.json` do volume.

### Etapa 1. Ler o material antes de traduzir

A LLM deve inspecionar:

- `manifest.json`
- `translation/translated-html/`
- `translation/plaintext/`
- `package/content.opf`
- `package/toc.ncx`, quando existir

O objetivo é descobrir:

- quantos arquivos HTML/XHTML existem;
- como o sumário está quebrado;
- onde começam frontmatter, prólogo, capítulos, epílogo, posfácio e créditos;
- se o volume precisa ser dividido em 2, 3 ou 4 etapas de tradução;
- se há páginas especiais que precisarão de normalização posterior no pacote;
- se a preservação de ilustrações do PDF ficou fiel à ordem do material original.

### Etapa 2. Mapear termos novos antes de traduzir

Antes da primeira etapa traduzida de cada volume, a LLM deve fazer uma triagem de termos novos.

Fontes mínimas para a triagem:

- `manifest.json`
- `translation/plaintext/`
- `translation/translated-html/`
- títulos visíveis, sumário, créditos e páginas especiais

O objetivo é encontrar termos que:

- sejam específicos da obra atual;
- sejam específicos da Type-Moon;
- ainda não existam em `standards/type-moon/GLOSSARIO_TYPEMOON_OPERACIONAL.json`;
- precisem de padronização para evitar inconsistência na tradução do volume e dos volumes futuros.

Regras da triagem:

- adicionar ao glossário apenas termos relevantes de lore, facção, instituição, sistema, habilidade, item, título, apelido, epíteto, local, evento, cargo ou convenção narrativa recorrente;
- não inflar o glossário com palavras genéricas, nomes comuns sem ambiguidade ou termos sem valor de padronização;
- se o termo já existir no glossário, reaproveitar a forma existente sem criar duplicata;
- se o termo for específico da obra, registrar na seção específica da obra dentro do glossário operacional;
- se houver dúvida real sobre a forma final, preservar temporariamente o original no texto, registrar o candidato para revisão e não inventar padronização definitiva.

Entrega mínima desta etapa:

- lista dos termos novos encontrados;
- forma padronizada escolhida;
- seção do glossário atualizada no projeto antes de iniciar a tradução;
- resumo curto do que passou a valer para o volume.

Quando esta etapa encontrar termos novos e a atualização do glossário for concluída, a LLM deve informar o que foi padronizado antes de iniciar a primeira etapa de tradução do volume.

### Etapa 3. Definir as etapas de tradução

A tradução deve ser sempre feita por etapas.

Regras:

- usar divisões naturais do material;
- preservar continuidade entre arquivos consecutivos;
- não criar etapas minúsculas;
- não criar etapas grandes demais a ponto de perder consistência;
- se o usuário limitar o volume a no máximo 4 etapas, isso deve ser respeitado.

Cada etapa deve informar:

- `Etapa X/Y`;
- escopo exato, com arquivos ou capítulo;
- resultado;
- quantas etapas faltam;
- pedido de confirmação para seguir.

Formato mínimo:

```text
Etapa X/Y
Escopo: [arquivos / capítulo / trecho]

Resultado:
[o que foi traduzido e validado]

Faltam N etapa(s).
Posso seguir para a próxima etapa?
```

### Etapa 4. Traduzir com o glossário no topo da prioridade

Durante a tradução:

- o glossário é prioridade máxima;
- o glossário já deve incluir os termos novos padronizados na triagem prévia do volume;
- acentuação correta, integridade de caracteres e encoding limpo são prioridade crítica;
- classes de Servant nunca são traduzidas;
- o PT-BR deve soar natural;
- a estrutura HTML/XHTML deve permanecer intacta;
- ids, hrefs, classes, âncoras, imagens e CSS não podem ser quebrados;
- títulos visíveis ao leitor, sumário visível, posfácio e créditos também devem ser traduzidos quando entrarem no lote;
- ruby deve ser preservado estruturalmente.

Regra crítica:

- nunca aplicar termo do glossário por substituição cega se isso quebrar concordância, regência, gênero, número, tom ou naturalidade da frase.
- qualquer `?` indevido no lugar de acento, aspas ou caractere válido invalida a etapa até correção.

### Etapa 5. Validar cada etapa antes de avançar

Validações mínimas por etapa:

1. procurar sobras de japonês no lote traduzido;
2. procurar termos sensíveis ainda crus, como `Master`, `Servant`, `Holy Grail`, `Noble Phantasm`, `True Name`, `Command Spell`;
3. validar parse XML/HTML dos arquivos alterados;
4. rodar `git diff --check` para evitar whitespace e problemas simples de formatação;
5. revisar se o glossário foi aplicado com contexto, e não como troca automática;
6. revisar explicitamente se não existe mojibake, perda de acentuação ou `?` substituindo caracteres válidos.

Essas validações devem ser feitas antes de declarar a etapa concluída.

### Etapa 6. Sincronizar a tradução de volta ao pacote do EPUB

Depois que a tradução inteira do volume estiver concluída e validada, é obrigatório sincronizar `translation/translated-html/` de volta para `package/`.

Comando canônico:

```powershell
powershell -File tools/novels/sync-epub-translation.ps1 `
  -ManifestPath "novel-workbench\<serie>\<volume>\manifest.json"
```

Esse sync é a ponte oficial entre o HTML de tradução e o pacote que será recompilado.

### Etapa 7. Normalizar o pacote para publicação em PT-BR

Antes do rebuild, revisar o pacote final em `package/`.

Para EPUB traduzido publicado em PT-BR com leitura ocidental, a normalização mínima é:

- `xml:lang="pt-BR"` nos arquivos visíveis ao leitor;
- `package/content.opf` com `<dc:language>pt-BR</dc:language>`;
- `package/content.opf` com `page-progression-direction="ltr"`;
- `package/content.opf` com `primary-writing-mode="horizontal-lr"`;
- `package/toc.ncx` com labels traduzidos quando o sumário for visível no leitor;
- `titlepage.xhtml`, páginas especiais e navegação coerentes com o estado final publicado.

Compatibilidade obrigatória das páginas de imagem com o leitor do site (ver a seção "Compatibilidade de páginas de imagem com o leitor do site" em `PROMPT_TRADUCAO_TYPEMOON_EPUB.md`):

- toda ilustração de tela cheia (capa, frontmatter visual, ilustração de capítulo) precisa do wrapper com classe `illustration` e do heading estrutural escondido via CSS;
- no CSS do pacote, imagens/ilustrações usam `max-height: 100vh` (nunca `max-height: 100%`) e `width: 100%` (nunca `width: 100vw`);
- capas em `<svg>` mantêm `viewBox` + `preserveAspectRatio` e não dependem só de `height: 100%`.

Sem isso, o leitor renderiza a imagem em branco até o segundo toque, espalha a imagem por páginas fantasmas ou trava a rolagem contínua.

Observação importante:

- essa normalização é do pacote recompilado, não do `metadata.opf` de catálogo do asset, salvo quando houver decisão explícita de mudar também o catálogo.

### Etapa 8. Recompilar o EPUB

Comando canônico:

```powershell
powershell -File tools/novels/rebuild-epub.ps1 `
  -ManifestPath "novel-workbench\<serie>\<volume>\manifest.json"
```

Saída esperada:

- `novel-workbench\<serie>\<volume>\build\<nome-base>.ptbr-sample.epub`

### Etapa 9. Publicar o EPUB no site

Depois do rebuild, copiar o EPUB final para a pasta de assets publicada da obra:

- `src/assets/<Autor>/<Pasta do volume>/<nome-base>.ptbr-sample.epub`

Regra:

- o arquivo publicado que o site deve ler precisa ficar em `src/assets/...`;
- o site não deve depender do `build/` dentro do workbench.

### Etapa 10. Validar a integração no site

Após publicar o asset:

1. confirmar que o módulo de dados do frontend enxerga o EPUB publicado;
2. confirmar que o volume aparece como leitura disponível;
3. confirmar que o leitor abre;
4. confirmar que o sumário e a navegação estão coerentes;
5. testar capa, ilustrações de abertura e ilustrações do miolo nos DOIS modos do leitor (paginado e rolagem contínua): devem aparecer de primeira, ocupar uma página só e não travar a rolagem (ver o contrato de páginas de imagem no prompt canônico);
6. rodar `npm run build`;
7. quando necessário, subir `npm run dev` e testar a URL do volume.

No estado atual do projeto:

- a descoberta dos EPUBs publicados está centralizada em `src/util/data/novels.ts`.

Esse arquivo deve continuar sendo o ponto único de ajuste de descoberta de assets, para manter o frontend desacoplado do workbench.

## Checklist rápido para LLMs

Antes de começar:

- ler glossário;
- ler este guia;
- ler o prompt canônico;
- inspecionar o `manifest.json`;
- mapear termos novos específicos da obra ou da Type-Moon e atualizar o glossário operacional no projeto;
- confirmar como o volume será dividido em etapas.

Durante a tradução:

- seguir o glossário já expandido pela triagem do volume;
- preservar HTML/XHTML;
- validar cada etapa;
- pedir confirmação antes da etapa seguinte.

Depois da última etapa:

- sincronizar `translated-html/` para `package/`;
- normalizar `content.opf`, `toc.ncx` e páginas especiais;
- garantir o contrato de páginas de imagem (classe `illustration` + heading escondido; `max-height: 100vh`; sem `width: 100vw`) antes do rebuild;
- recompilar o EPUB;
- copiar o `.ptbr-sample.epub` para `src/assets/...`;
- validar integração com o site, incluindo capa e ilustrações nos modos paginado e rolagem;
- garantir que o runtime não depende do workbench.

## Política final de limpeza

Quando todos os volumes de uma novel estiverem concluídos e publicados:

- `novel-workbench/...` poderá ser removido;
- os assets finais publicados devem continuar íntegros;
- o módulo de dados do frontend deve continuar resolvendo tudo sem workbench.

Regra de segurança:

- nunca apagar o workbench antes de confirmar que o `.ptbr-sample.epub` final está em `src/assets/...`, que o site o enxerga e que o build do frontend passa.
