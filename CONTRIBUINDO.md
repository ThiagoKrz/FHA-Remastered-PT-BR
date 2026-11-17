# Como contribuir na revisão de scripts (Fate/hollow ataraxia)

## Fluxo rápido (5 passos)

1. **Atualize seu repositório antes de começar:**
   ```bash
   git pull
   ```
2. **Abra o painel:** dê duplo clique em `Abrir painel.cmd` na raiz do projeto (ou em `Pasta principal/trabalho/Abrir painel.cmd`).
3. **Escolha sua rota/cena e edite:**
   - Combine com a equipe qual rota ou cena você vai revisar para evitar conflitos no mesmo arquivo `.json`.
   - Edite apenas o campo **Português brasileiro** (os campos `jp` e `en` são referências imutáveis).
   - Preserve tags como `[wait...]`, `[hffacechg...]`, `[l]`, `[lr]` e **nunca** use `::` dentro do texto.
   - Use **Busca global (`Ctrl+Shift+F`)** para achar termos no projeto inteiro e **Conferir glossário** para verificar `Guias/GLOSSARIO_TYPEMOON_OPERACIONAL.json`.
4. **Valide e teste no jogo (`F5` / `Ctrl+Enter`):**
   - Pressione `F5` (ou **Validar projeto**) para garantir 0 erros.
   - Clique em **Gerar e instalar .epk** (`Ctrl+Enter`) para compilar e instalar os `.epk` direto na pasta do mod em `%LOCALAPPDATA%\typemoon\hollow\data\root\data\locale\us\epk`.
5. **Envie suas alterações:**
   ```bash
   git add "Pasta principal/trabalho/"
   git commit -m "Revisa <rota/cena>"
   git push
   ```
