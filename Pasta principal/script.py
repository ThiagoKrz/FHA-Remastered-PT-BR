import sys
import subprocess
import os

if len(sys.argv) != 2:
    print("Usage: " + sys.argv[0] + " ./editar/<nome do arquivo.epk_enc>")
    exit(1)

input_file = sys.argv[1]
output_file = os.path.basename(sys.argv[1][:-8])
input_move = str(sys.argv[1][:-8])

subprocess.run(["./main.exe", "enc", input_file])
subprocess.run(["powershell", "-Command", "mv", "\"" + input_move + ".epk_enc" + "\"",  "\"" + output_file + ".epk" + "\"", "-Force"])
