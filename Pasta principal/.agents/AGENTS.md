# Regras do Projeto FHA-Remastered-PT-BR

> **Prompt canônico de trabalho:** `standards/type-moon/PROMPT_AGENTE_FHA_UNIFICADO.md`
> (contrato, protocolo antideriva, glossário rápido, vozes e portões de qualidade).
> Releia o §0 dele antes de cada lote.

## 1. Integridade de Tags e Codificação (Encoding)
- **ATENÇÃO MÁXIMA**: Todos os arquivos de script (`.epk_dec`) devem ser lidos e escritos **obrigatoriamente em UTF-8**.
- **Jamais utilize comandos de terminal PowerShell (como `Get-Content`, `Add-Content`, `Set-Content`) para ler ou escrever arquivos**, pois o PowerShell no Windows usa ANSI (cp1252) por padrão, o que corrompe caracteres japoneses (mojibake) presentes dentro das tags do Kirikiri (ex: `[chgfg storage=凛...]`).
- Utilize **SEMPRE** as ferramentas nativas (`view_file`, `write_to_file`, `replace_file_content`) para manipular os scripts. Estas ferramentas garantem que a codificação UTF-8 e os caracteres japoneses originais sejam mantidos intactos ("Zero Tag Loss").

## 2. Agressividade e Qualidade na Retradução
- Ao retraduzir, o sistema está autorizado e instruído a ser **mais agressivo na reescrita** do texto.
- O foco é a **melhora total** na fluidez, naturalidade e adequação do texto para PT-BR, evitando traduções literais.
- As falas devem refletir perfeitamente o "Teste Cego de Voz" (Character Voice) já mapeado (ex: tom imponente e determinado da Saber, sarcasmo do Archer, etc).
- Adapte sentenças, reestruture frases e use expressões naturais do português para que os diálogos fiquem impecáveis, sem parecer uma tradução engessada.

## 3. Formatação de Quebra de Linha (Line Endings)
- **Obrigatório:** Todos os arquivos de script devem ser salvos exclusivamente com quebra de linha **LF (\n)** e nunca CRLF (\r\n). O uso de CRLF quebra o leitor da engine Kirikiri.

## 4. Atualização de Controle (CSV)
- **Obrigatório:** Após a conclusão e verificação de um lote inteiro (traduzido, revisado, salvo em UTF-8 e LF), você DEVE obrigatoriamente marcar a respectiva linha do lote no arquivo etapas_traducao_qwen_codex_prompt_fha_qmax.csv alterando o status de pendente para concluida e atualizando o campo de observações.
