# Guia de Build do Instalador de PC (`Instalar Patch PT-BR.exe`)

Este guia documenta o funcionamento, estrutura e processo de compilação do instalador oficial para a versão de PC (Steam) de **Fate/hollow ataraxia REMASTERED**.

---

## 1. Visão Geral

O instalador é uma aplicação Windows (.NET Framework 4.7.2 / WPF) leve, sem dependências externas, projetada para:
1. Localizar automaticamente a pasta de instalação do jogo através da Steam (chaves de registro e `libraryfolders.vdf`).
2. Permitir seleção manual caso o jogo esteja em diretório customizado.
3. **Verificar a integridade de cada arquivo** da tradução antes de copiar, conferindo tamanho em bytes e hash SHA-256. Se qualquer arquivo estiver corrompido ou incompleto, a instalação é bloqueada com aviso claro.
4. Fazer backup automático dos arquivos originais em `<PastaDoJogo>/fatecafe_backup/`.
5. Permitir desinstalação com um clique, restaurando os arquivos originais.

---

## 2. Estrutura de Arquivos

As ferramentas do instalador ficam em:
`C:\Users\Thiago\Pictures\fpm\FHA\ferramentas\instalador\`

```text
ferramentas/instalador/
├── gerar_instalador.py       # Script principal de automação
├── preparar_assets.py        # Extração e preparação de ícones pixel art
├── icone_pixelart.png        # Ícone visual do instalador
├── ultimo_instalador.json    # Relatório do último build (hashes e tamanhos)
├── src/                      # Código-fonte C# (.NET 4.7.2)
│   ├── Instalador.csproj
│   ├── Program.cs
│   ├── MainWindow.xaml / .cs
│   ├── SteamDetector.cs
│   ├── PatchEngine.cs
│   └── PatchInfo.g.cs        # Gerado automaticamente com os hashes
└── build/                    # Binários compilados temporários
```

---

## 3. Os 5 Arquivos do Patch de PC

O patch de tradução de PC é composto estritamente pelos seguintes arquivos:
- `boot.dat` (Imagens de boot, aviso e logo da Fate Café)
- `obb/pack00d.bin` (Texturas e assets gráficos 2D da interface)
- `obb/pack00m.bin` (Scripts de diálogos .epk, textos, fontes, scripts de controle)
- `obb/pack01d.bin` (Vídeos e aberturas traduzidas)
- `obb/pack11d.bin` (Banco de CGs - `ex_pack2.dat` e `fileinfo_ex_pack2.txt`)

---

## 4. Como Gerar o Instalador

Toda vez que qualquer arquivo traduzido for modificado e salvo na pasta do patch de PC, o instalador **DEVE ser recompilado** para atualizar a tabela de hashes SHA-256. Se isso não for feito, o instalador recusará os arquivos por falha de integridade.

### Comando de Execução:

Abra o terminal e execute:

```powershell
cd C:\Users\Thiago\Pictures\fpm\FHA\ferramentas\instalador
python gerar_instalador.py "D:\Downloads\Fate-hollow-ataraxia-PT-BR-beta 0.1-PC\Fate hollow ataraxia PT-BR beta 0.1 (Fate Cafe)" --versao "beta 0.1"
```

### O que o script faz automaticamente:
1. Lê os 5 arquivos na pasta informada e calcula o SHA-256 e o tamanho exato de cada um.
2. Escreve `src/PatchInfo.g.cs` contendo a lista com os hashes fixados.
3. Chama o compilador .NET (`dotnet build src/Instalador.csproj -c Release`).
4. Copia o binário gerado para a pasta do patch como `Instalar Patch PT-BR.exe`.
5. Gera o `LEIA-ME.txt` com instruções completas, aviso sobre IA e links do Discord/Site, codificado em UTF-8 com BOM e quebras de linha Windows (`\r\n`).
6. Salva um resumo auditável em `ultimo_instalador.json`.

---

## 5. Empacotamento para Distribuição

Para gerar o `.zip` que é distribuído aos jogadores:
1. Abra a pasta do patch:
   `D:\Downloads\Fate-hollow-ataraxia-PT-BR-beta 0.1-PC\Fate hollow ataraxia PT-BR beta 0.1 (Fate Cafe)`
2. Verifique se estão presentes:
   - `Instalar Patch PT-BR.exe`
   - `LEIA-ME.txt`
   - `boot.dat`
   - pasta `obb/` (com `pack00d.bin`, `pack00m.bin`, `pack01d.bin`, `pack11d.bin`)
3. Compacte em um arquivo `.zip` ou `.7z` sem compressão excessiva para permitir extração rápida pelo usuário.
