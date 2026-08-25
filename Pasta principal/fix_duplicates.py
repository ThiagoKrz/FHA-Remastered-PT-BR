import os
import codecs

dir_pt = r"c:\Users\Thiago\Desktop\FHA-Remastered-PT-BR\Pasta principal\scripts_pt-br"
dir_en = r"c:\Users\Thiago\Desktop\FHA-Remastered-PT-BR\Pasta principal\scripts_en"

problematic_files = [
    "0e48k71fsdomgcpo2k9299ump3.epk_dec",
    "270pptv5rtedgd0123n96c64aa.epk_dec",
    "4srpcang4drd31p2frat56b4kl.epk_dec",
    "uistring.epk_dec"
]

for filename in problematic_files:
    pt_path = os.path.join(dir_pt, filename)
    en_path = os.path.join(dir_en, filename)
    
    if not os.path.exists(pt_path) or not os.path.exists(en_path):
        print(f"Skipping {filename}")
        continue
        
    # Read PT file and get the LAST translation for each ID
    pt_dict = {}
    with codecs.open(pt_path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            parts = line.strip().split("::", 2)
            if len(parts) >= 3 and parts[0].isdigit():
                pt_dict[parts[0]] = parts[2]
                
    # Read EN file and construct new PT file
    new_lines = []
    with codecs.open(en_path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            parts = line.strip().split("::", 2)
            if len(parts) >= 3 and parts[0].isdigit():
                id_ = parts[0]
                label = parts[1]
                if id_ in pt_dict:
                    new_lines.append(f"{id_}::{label}::{pt_dict[id_]}\n")
                else:
                    new_lines.append(f"{id_}::{label}::{parts[2]}\n")
            else:
                new_lines.append(line.rstrip('\r\n') + '\n')
                
    # Save the new PT file
    with codecs.open(pt_path, "w", encoding="utf-8") as f:
        f.writelines(new_lines)
    print(f"Fixed duplicates in {filename}")

print("Done.")
