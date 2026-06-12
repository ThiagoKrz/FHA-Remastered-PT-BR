# Prompt Operacional - Expressões de Servos via Atlas

## Objetivo

Implementar, manter e corrigir a aba de **Expressões** da página de perfil dos Servos usando **apenas assets hospedados no Atlas Academy**, sem copiar PNGs para o projeto e sem quebrar o lazy load.

O sistema deve:

1. descobrir assets de expressão a partir da API da Atlas;
2. montar o sprite final em `<canvas>`;
3. mostrar apenas o sprite final, sem a galeria de cabeças no rodapé do sheet;
4. permitir troca de expressão e download em PNG;
5. usar overrides manuais só quando a automação não for suficiente.

---

## Regras inegociáveis

1. **Nunca hospedar localmente os PNGs de expressão.**
2. **O lazy load deve continuar ativo.**
   - a aba de Expressões só carrega o componente quando aberta;
   - os PNGs do Atlas só carregam quando a aba é aberta;
   - o projeto não pode importar todos os sheets de expressão no build.
3. **A automação é a regra; override manual é exceção.**
4. **Quando houver caso especial, corrigir via JSON de override antes de mexer na lógica global.**
5. **Não quebrar a seção de Servos nem a estrutura atual do projeto.**

---

## Arquivos centrais

- `src/components/servant/ServantProfile.tsx`
- `src/components/servant/ServantExpressions.tsx`
- `src/util/servantExpressions.ts`
- `src/types/atlas-servant-full.ts`
- `src/hooks/useAtlasServant.ts`
- `src/util/data/servant-expression-overrides.json`

---

## Fonte de dados correta

### 1. Metadados da API

Os dados principais vêm de:

- `extraAssets.charaFigure`
- `extraAssets.charaFigureForm`
- `charaScripts`

Campos importantes em `charaScripts`:

- `id`
- `form`
- `faceX`
- `faceY`
- `scale`
- `offsetX`
- `offsetY`
- `extendData.faceSize`
- `extendData.faceSizeRect`

### 2. Imagem real usada

As expressões reais vêm do próprio:

- `.../CharaFigure/..._merged.png`

Não usar `extraAssets.faces` como fonte principal de montagem, porque esses arquivos não resolvem corretamente o problema do recorte e posicionamento do rosto.

---

## Arquitetura atual

### Etapa A - Descoberta automática

O sistema tenta montar `expressionSources` automaticamente com base em:

- `charaScripts`
- `extraAssets.charaFigure`
- `extraAssets.charaFigureForm`

Ele normaliza cada source com:

- `id`
- `charaId`
- `form`
- `assetType`
- `assetKey`
- `url`
- `anchorX`
- `anchorY`
- `faceWidth`
- `faceHeight`
- `scale`

### Etapa B - Override manual por Servo

Se o Servo estiver em:

- `src/util/data/servant-expression-overrides.json`

o sistema usa essa curadoria manual em vez da seleção automática de sources.

Isso existe para casos em que a Atlas:

- lista assets demais;
- lista assets errados;
- não reflete a ordem desejada;
- mistura variantes que não devem virar botões na UI.

### Etapa C - Extração de frames

Ao abrir a aba:

1. o app baixa o `merged.png` direto do Atlas;
2. analisa a imagem no browser;
3. detecta os frames de expressão;
4. recorta o corpo;
5. sobrepõe a expressão escolhida no canvas;
6. permite download do resultado.

---

## Estratégia de automação

### Nível 1 - Automático por padrão

Para Servos novos, o sistema deve primeiro tentar funcionar sozinho.

Isso significa:

- o Servo novo aparece normalmente;
- a aba de Expressões tenta montar os sources automaticamente;
- se o layout do sheet for padrão, nenhuma intervenção manual é necessária.

### Nível 2 - Override de seleção de sheets

Se a Atlas listar sheets ruins ou incompletos, usar override manual para definir:

- quais URLs entram;
- em que ordem entram;
- quais labels serão mostradas.

### Nível 3 - Override fino de corte

Se o source estiver correto, mas o preview ainda mostrar a galeria de cabeças no rodapé, usar override por source com:

- `gridStartY`
- `bodyBottom`

Esses campos existem para forçar:

- onde começa a grade de expressões;
- até onde o corpo deve ser recortado.

Essa abordagem é preferível a alterar a heurística global quando o problema for localizado.

### Nível 4 - Heurística automática para sheets largos

Para sheets largos, especialmente os de `2048px` com células de `256px`, o sistema deve tentar detectar automaticamente a primeira faixa uniforme de expressões.

Padrão observado:

- as linhas do corpo costumam ter cobertura irregular;
- as linhas de expressão costumam formar uma sequência uniforme;
- essa sequência geralmente começa em `768`, mas a lógica deve detectar o padrão e não depender de hardcode por Servo.

Se essa heurística funcionar, preferir isso antes de criar override manual.

---

## Formato do override

Arquivo:

- `src/util/data/servant-expression-overrides.json`

Estrutura:

```json
{
  "2501400": {
    "name": "Aozaki Aoko",
    "images": [
      {
        "label": "Ascensão 1",
        "url": "https://static.atlasacademy.io/JP/CharaFigure/25014000/25014000_merged.png",
        "charaId": 25014000,
        "assetType": "ascension"
      },
      {
        "label": "Story 1",
        "url": "https://static.atlasacademy.io/JP/CharaFigure/1098292950/1098292950_merged.png",
        "charaId": 1098292950,
        "assetType": "story"
      }
    ]
  }
}
```

Campos aceitos por item:

- `label`
- `url`
- `charaId`
- `form`
- `assetType`
- `gridStartY`
- `bodyBottom`

Exemplo de ajuste fino:

```json
{
  "label": "Asc 3",
  "url": "https://static.atlasacademy.io/JP/CharaFigure/23009002/23009002_merged.png",
  "charaId": 23009002,
  "assetType": "ascension",
  "gridStartY": 768,
  "bodyBottom": 768
}
```

---

## Casos já mapeados

### Funcionaram bem com curadoria

- Aozaki Aoko
- Sima Yi (Reines)

### Casos em que foi necessário override fino de corte

- `2300900` - Mysterious Executor C.I.E.L
  - `Asc 3`
- `2300600` - BB Dubai
  - `Asc 2`
  - `Asc 3`

Motivo:

- o source estava certo;
- as expressões estavam certas;
- mas o preview ainda incluía a faixa inferior com as cabeças.

Nesses casos, a solução preferida é ajustar `gridStartY` e `bodyBottom` no JSON, não reescrever a heurística inteira.

---

## Como decidir entre heurística e override

### Mexer na heurística global quando:

- o mesmo bug aparece em vários Servos diferentes;
- o padrão visual é claramente repetível;
- a correção beneficia muitos casos sem risco alto de regressão.

### Usar override manual quando:

- o problema acontece em poucos Servos;
- o layout do sheet é atípico;
- a Atlas mistura assets errados para aquele Servo;
- o corte do corpo precisa de um valor fixo específico.

---

## Fluxo recomendado para corrigir um Servo

1. Abrir o perfil do Servo e ir na aba de Expressões.
2. Verificar se:
   - os botões de source estão certos;
   - a ordem está certa;
   - as expressões detectadas estão certas;
   - o preview mostra só o sprite final;
   - não há cabeças sobrando no rodapé.
3. Se a seleção de sheets estiver errada:
   - adicionar ou ajustar entrada no `servant-expression-overrides.json`.
4. Se a seleção estiver certa, mas o crop estiver errado:
   - ajustar `gridStartY` e/ou `bodyBottom` naquele source.
5. Rodar `npm run build`.
6. Validar visualmente no navegador.

---

## O que já atualiza sozinho quando a Atlas adiciona Servo novo

### Sim, automaticamente:

- dados do Servo vindos da Atlas;
- tentativa automática de descobrir expression sources;
- carregamento dos PNGs direto da Atlas;
- lazy load da aba.

### Não, automaticamente:

- curadoria perfeita da ordem dos sheets;
- exclusão manual de sheets ruins;
- ajustes finos de `gridStartY` e `bodyBottom`.

### Também deve acontecer automaticamente quando possível:

- rotular ascensões pela chave real do asset (`1`, `2`, `3`);
- exibir variantes como `Ascensão 2 · Forma 1`, em vez de transformar isso em `Ascensão 3` ou `Ascensão 4` por contagem cega.

Ou seja:

- Servo novo entra e o sistema tenta funcionar sozinho;
- se for caso padrão, ótimo;
- se for caso especial, adicionar uma entrada no JSON resolve sem mexer na lógica central.

---

## Restrições de performance

1. Não converter esse sistema em import estático de todos os sheets.
2. Não criar bundle gigante em `ServantProfile`.
3. Não fazer preload desnecessário fora da aba de Expressões.
4. Continuar usando URLs remotas da Atlas com `crossOrigin="anonymous"`.

---

## Checklist antes de fechar qualquer alteração

1. `npm run build` passou.
2. A aba de Expressões continua lazy-loaded.
3. O preview mostra só o sprite final, sem a galeria inferior.
4. O download em PNG continua funcionando.
5. Servos já corrigidos anteriormente não regrediram.

---

## Resumo operacional

A estratégia correta para este sistema é:

1. **Atlas como fonte única de imagem**
2. **detecção automática por padrão**
3. **override por Servo quando a seleção de sheets falhar**
4. **override por source (`gridStartY` / `bodyBottom`) quando o crop falhar**
5. **lazy load preservado o tempo todo**

Se este chat se perder, continuar exatamente daqui, seguindo este prompt e preservando a arquitetura atual.
