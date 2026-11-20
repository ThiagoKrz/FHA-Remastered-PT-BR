# Como contribuir na revisão de scripts (Fate/hollow ataraxia)

A `main` é a versão oficial. **Ninguém traduz direto na `main`:** cada pessoa trabalha numa branch própria e envia por pull request, tudo pelo [GitHub Desktop](https://desktop.github.com/). O fluxo é o mesmo dos outros projetos da equipe (Tsukihime, Fate/Extra CCC e Mahoyo).

## Uma vez só

1. Instale o [GitHub Desktop](https://desktop.github.com/) (entre com a sua conta do GitHub) e o [Python 3.10+](https://www.python.org/downloads/), marcando **Add python.exe to PATH**.
2. Peça acesso ao repositório no Discord.
3. No GitHub Desktop: **File › Clone repository › URL**, cole `https://github.com/ThiagoKrz/FHA-Remastered-PT-BR` e clique em **Clone**.

## Começar uma tarefa

Combine com a equipe qual rota ou cena você vai revisar, para duas pessoas não mexerem no mesmo `.json`.

1. **Current branch › `main`** e **Pull origin**. Se o botão estiver como **Fetch origin**, clique nele antes.
2. **Current branch › New branch**, nome `seunome/rota-cena` › **Create branch**.

## Todo dia, antes de traduzir

1. **Current branch › `main`** e **Pull origin**.
2. Volte para a sua branch e clique em **Branch › Update from main**. Apareceu conflito? Chame alguém no Discord.

## Revisar no painel

1. Dê duplo clique em `Abrir painel.cmd` na raiz do projeto (ou em `Pasta principal/trabalho/Abrir painel.cmd`).
2. Escolha a rota/cena e edite apenas o campo **Português brasileiro**: `jp` e `en` são referências imutáveis.
3. Preserve tags como `[wait...]`, `[hffacechg...]`, `[l]` e `[lr]`, e **nunca** use `::` dentro do texto.
4. **Busca global** (`Ctrl+Shift+F`) acha termos no projeto inteiro; **Conferir glossário** compara com `Guias/GLOSSARIO_TYPEMOON_OPERACIONAL.json`.
5. **F5** (Validar projeto): envie só com 0 erros.
6. **Gerar e instalar .epk** (`Ctrl+Enter`) compila e instala os `.epk` na pasta do mod (`%LOCALAPPDATA%\typemoon\hollow\data\root\data\locale\us\epk`) para testar no jogo.

## Enviar

1. Na aba **Changes**, confira o que mudou (deixe marcado só o que é de `Pasta principal/trabalho/`), escreva um resumo como `Revisa <rota/cena>` e clique em **Commit**.
2. **Publish branch**. Das próximas vezes, o botão vira **Push origin**. Faça isso no fim de cada dia, para o trabalho ficar guardado.
3. Tarefa pronta: **Preview Pull Request › Create pull request** e confirme no navegador. O GitHub roda a validação, e a revisão junta na `main`.

Precisa corrigir? Novo commit e **Push origin** na mesma branch. Aceito? A próxima tarefa começa do zero.

> Se, ao trocar de branch, o Desktop perguntar o que fazer com as suas alterações, cancele e faça o commit antes.

## Prefere o terminal?

```bash
git clone https://github.com/ThiagoKrz/FHA-Remastered-PT-BR.git         # uma vez
git switch main && git pull && git switch -c seunome/rota-cena         # nova tarefa
git pull --no-edit origin main                                         # todo dia, na sua branch
git add "Pasta principal/trabalho/" && git commit -m "Revisa <rota/cena>"
git push -u origin seunome/rota-cena                                   # depois, só: git push
```
