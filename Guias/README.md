# Guias de Build e Publicação - Fate/hollow ataraxia REMASTERED PT-BR

Esta pasta contém a documentação técnica completa e passo a passo para compilar e gerar as distribuições da tradução para PC (Steam) e Nintendo Switch.

> **Aviso de Repositório:** Não adicione ficheiros binários pesados (`.nsp`, `.bin`, `.dat`, `.exe`) a esta pasta ou ao repositório git. Mantenha apenas documentação, código-fonte e scripts de automação.

---

## Estrutura dos Guias

1. **[Guia de Build do NSP de Switch](GUIA_BUILD_NSP_SWITCH.md)**
   - Explicação completa da arquitetura do patch cumulativo para Switch.
   - Detalhes de por que não se pode jogar os arquivos `.bin` do PC direto no Switch (arquivos exclusivos, tela de vozes, padding MD5 do banco de CGs).
   - Execução dos passos 1 ao 4 com validação em baixo nível (estilo console).
   - Instruções de atualização quando sair novo update oficial do jogo.

2. **[Guia de Build do Instalador de PC (.exe)](GUIA_BUILD_INSTALADOR_PC.md)**
   - Como funciona o gerador do executável `Instalar Patch PT-BR.exe`.
   - Processo de checagem SHA-256 e tamanho dos arquivos traduzidos.
   - Compilação via .NET SDK (`dotnet build`).
   - Geração automática de `LEIA-ME.txt` e empacotamento da versão de PC.

---

## Localização das Ferramentas no Sistema

- **Ferramentas de Switch:** `C:\Users\Thiago\Pictures\fpm\FHA\ferramentas\switch`
- **Ferramentas do Instalador PC:** `C:\Users\Thiago\Pictures\fpm\FHA\ferramentas\instalador`
- **Executável fpm (reempacotador):** `C:\Users\Thiago\Pictures\fpm\FHA\fpm.exe`
- **Patch de PC publicado / base:** `D:\Downloads\Fate-hollow-ataraxia-PT-BR-beta 0.1-PC\Fate hollow ataraxia PT-BR beta 0.1 (Fate Cafe)`
- **Área de trabalho Switch:** `D:\Games\FHAR_SWITCH\_trabalho`
- **Saída do NSP:** `D:\Games\FHAR_SWITCH`
