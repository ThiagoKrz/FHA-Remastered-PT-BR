import os
import glob
import subprocess

# Busca todos os arquivos .epk na pasta
arquivos_epk = glob.glob("*.epk")

if not arquivos_epk:
    print("Nenhum arquivo .epk encontrado nesta pasta!")
    exit()

print(f"Encontrados {len(arquivos_epk)} arquivos .epk. Iniciando processo...\n")

for epk in arquivos_epk:
    print(f"--- Processando: {epk} ---")
    
    # 1. Tira a criptografia (Transforma .epk em .epk_dec)
    print("Descriptografando com main.exe...")
    subprocess.run(["./main.exe", "dec", epk])
    
    # O main.exe gera um arquivo com o mesmo nome + "_dec" no final
    epk_dec = f"{epk}_dec"
    
    # 2. Verifica se deu certo e extrai o pacote
    if os.path.exists(epk_dec):
        print(f"Sucesso! {epk_dec} gerado.")
        print("Extraindo arquivos internos com fate_stay_extract.exe...")
        
        # Roda o extrator no arquivo .epk_dec
        subprocess.run(["./fate_stay_extract.exe", epk_dec])
        print("Extração concluída!\n")
    else:
        print(f"ERRO: O arquivo {epk_dec} não foi criado. Verifique se o SomeKey.bin está na pasta.\n")

print("Todos os processos foram finalizados!")