# Guia de Build do NSP de Switch - Fate/hollow ataraxia REMASTERED PT-BR

Este guia detalha toda a arquitetura, regras de compatibilidade e o processo de geração do pacote cumulativo `.nsp` de **Fate/hollow ataraxia REMASTERED** para Nintendo Switch.

---

## 1. Identificadores e Versões do Jogo

- **Base Game Title ID:** `010070E022546000` (Versão `v0`)
- **Patch/Update Title ID:** `010070E022546800` (`BASE_ID + 0x800`)
- **Versão Oficial Atual de Switch:** `v131072` (Update 1.0.2 oficial)
- **Versão do NSP PT-BR Gerado:** `v196608` (Sempre maior que a oficial; `+65536` a cada novo release)
- **Tipo de NSP:** Update Cumulativo (contém as correções oficiais da v131072 + a tradução PT-BR, dispensando o update oficial da Nintendo e instalando diretamente sobre o jogo base).

---

## 2. Por que NÃO usar os arquivos `.bin` do PC direto no Switch?

Os pacotes `.bin` da versão Steam (PC) são estruturalmente diferentes dos pacotes de Switch. Testes comparativos arquivo por arquivo comprovaram:

### 2.1. `pack00m.bin` (Scripts e Resident)
- **17 arquivos existem EXCLUSIVAMENTE no Switch:**
  - 10 scripts na pasta `root/data/kag2/` (`夜編2-26.ks`, `真・冒頭-03.ks`, etc.) com ajustes de coordenadas gráficas e enquadramento feitos pela Type-Moon específicos para a tela do Switch.
  - 6 arquivos `.epk` em chinês (`locale/ck/`).
  - 1 fonte exclusiva do Switch.
- Se o `.bin` do PC for copiado direto, esses 17 arquivos somem, causando travamentos (o mesmo bug que corrompeu o FSN anteriormente).

### 2.2. `pack00d.bin` (Interface e Texturas)
- **19 imagens são exclusivas do Switch:**
  - Localizadas em `root/data/fuzz/release/root/resident/gui/textures/07_config/07_cv_XXb@4x.webp`.
  - São os nomes dos personagens na tela de vozes. A numeração dos dubladores no PC difere do Switch (ex.: no PC um ID é Berserker, no Switch é Kiritsugu).
  - Copiar o `.bin` do PC faz a tela de vozes do Switch exibir nomes trocados. O script de merge mantém a versão original do Switch para essas 19 imagens (`manter_versao_switch.txt`).

### 2.3. `pack11d.bin` (Banco de Imagens e CGs - `ex_pack2.dat`)
- Contém 6.392 imagens em um único banco contíguo, com índice em `fileinfo_ex_pack2.txt`.
- A tradução traduziu 142 imagens de texto/diálogos em cena.
- **Alinhamento de 16 Bytes:** O Switch exige que cada arquivo comece em offset múltiplo de 16 (`offset % 16 == 0`), com preenchimento em bytes nulos (`0x00`).
- **Defeito do MD5 do PC (Word Alignment):** A ferramenta antiga de PC alinhava arquivos a múltiplos de 4 bytes e calculava o hash MD5 *sobre os bytes preenchidos com padding*. A engine do Switch valida o MD5 estritamente sobre os *bytes reais (unpadded)*. O script de merge recalcula o MD5 correto sobre os bytes reais, evitando crash por corrupção.

### 2.4. Gestão de Memória (O "Bug do ZL")
- Pacotes com sufixo `m` (como `pack00m.bin`) ficam **completamente carregados na memória RAM**.
- No FSN, um erro de empacotamento fez o pacote inchar de 40 MB para 1,7 GB, fazendo o Switch travar ao segurar ZL para acelerar diálogos.
- No FHA, o `pack00m.bin` oficial tem ~307 MB e o traduzido tem ~317 MB (dentro da margem de segurança de 110%).

---

## 3. Arquitetura de Baixo Nível do NSP (BKTR)

A montagem do `.nsp` utiliza o padrão nativo do Nintendo Switch OS:
1. **RomFS BKTR:** O NCA de programa referencia os arquivos não modificados diretamente do jogo base (sem duplicar espaço no armazenamento do console). Apenas os arquivos novos/modificados são gravados na partição BKTR.
2. **Alinhamento de 16 Bytes:** Todas as entradas das tabelas de relocação BKTR e de subseções são alinhadas a 16 bytes (compatível com blocos AES-CTR).
3. **Decifração AES-CTR-Ex:** A tabela indireta BKTR possui geração explícita de subseção (subseção 0 e 1), garantindo que o console leia sem acusar "dados corrompidos".
4. **ExeFS:** Preserva o executável oficial da v131072 do Switch (código binário NSO não é alterado).
5. **CNMT (Patch 0x81):** O arquivo de metadados inclui o Program NCA, Control NCA (ícone e título) e o bloco de 28 bytes `PatchMetaExtendedData` exigido pelo Ryujinx, Atmosphère e LibHac.

---

## 4. Estrutura das Ferramentas

Local das ferramentas:
`C:\Users\Thiago\Pictures\fpm\FHA\ferramentas\switch\`

- `config.py`: Caminhos das NSPs oficiais, chaves `prod.keys`, diretórios temporários e versão.
- `nsp_lib.py`: Biblioteca de baixo nível para leitura estilo console, criptografia NCA, IVFC e BKTR.
- `manter_versao_switch.txt`: Lista das 19 imagens de vozes que mantêm a versão de Switch.
- `1_extrair_oficial.py`: Extrai o RomFS oficial e os pacotes necessários.
- `2_montar_romfs.py`: Realiza o merge inteligente dos pacotes oficiais + tradução de PC.
- `3_montar_nsp.py`: Compila os NCAs e empacota o `.nsp` final.
- `4_validar_nsp.py`: Valida a estrutura IVFC, CNMT, ExeFS e RomFS simulando a leitura do console.

---

## 5. Como Executar o Build Passo a Passo

### Pré-requisitos
- Python 3.11 instalado com os módulos `cryptography` e `pycryptodome`.
- Chaves do console em `C:\Users\Thiago\AppData\Roaming\Ryujinx\system\prod.keys`.
- Ficheiros originais em `D:\Games\`:
  - `v-fate_hollow_ataraxia_remastered.nsp` (jogo base)
  - `v-fate_hollow_ataraxia_remastered_v131072.nsp` (update oficial)

### Passo 1: Extrair dados oficiais
```powershell
cd C:\Users\Thiago\Pictures\fpm\FHA\ferramentas\switch
python 1_extrair_oficial.py
```
*Gera `D:\Games\FHAR_SWITCH\_trabalho\oficial\` com os pacotes descompactados e inventário.*

### Passo 2: Montar RomFS traduzido
```powershell
python 2_montar_romfs.py
```
*Aplica as alterações da tradução sobre os pacotes oficiais, mantendo exclusivos e corrigindo o alinhamento de 16 bytes e MD5 do pack11d.*

### Passo 3: Montar o NSP
```powershell
python 3_montar_nsp.py
```
*Gera o arquivo `D:\Games\FHAR_SWITCH\Fate_hollow_ataraxia_REMASTERED_PT-BR[010070E022546800][v196608].nsp` e seu arquivo `.sha256`.*

### Passo 4: Validar
```powershell
python 4_validar_nsp.py
```
*(Opcional para teste exaustivo de todos os blocos do jogo base: `python 4_validar_nsp.py --completo`)*

---

## 6. Como Atualizar Quando Sair um Novo Update Oficial

Se a Aniplex/Type-Moon lançar uma nova versão oficial de Switch (ex.: `v196608`):
1. Copie o novo `.nsp` oficial para `D:\Games\`.
2. Abra `config.py` e atualize:
   - `UPDATE_NSP`: nome do novo arquivo `.nsp`.
   - `OFFICIAL_VERSION`: novo número da versão (ex.: `196608`).
   - `VERSION`: versão do patch PT-BR superior à oficial (ex.: `262144`).
3. Apague a pasta `_trabalho` e execute os Passos 1 a 4.
