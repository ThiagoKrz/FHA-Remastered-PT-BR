import os
import codecs
import csv

dir_pt = r"c:\Users\Thiago\Desktop\FHA-Remastered-PT-BR\Pasta principal\scripts_pt-br"
dir_en = r"c:\Users\Thiago\Desktop\FHA-Remastered-PT-BR\Pasta principal\scripts_en"
csv_path = r"c:\Users\Thiago\Desktop\FHA-Remastered-PT-BR\Pasta principal\etapas_traducao_qwen_codex_prompt_fha_qmax.csv"

# Load all files in pt directory
completed_files = [f for f in os.listdir(dir_pt) if f.endswith(".epk_dec")]

for filename in completed_files:
    pt_path = os.path.join(dir_pt, filename)
    en_path = os.path.join(dir_en, filename)
    
    if not os.path.exists(pt_path) or not os.path.exists(en_path):
        continue
        
    # Read EN file to map label to ID
    label_to_id = {}
    with codecs.open(en_path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            parts = line.strip().split("::")
            if len(parts) >= 3 and parts[0].isdigit():
                label = parts[1]
                id_ = parts[0]
                label_to_id[label] = id_
                
    # Read PT file and fix IDs
    changed = False
    with codecs.open(pt_path, "r", encoding="utf-8", errors="ignore") as f:
        pt_lines = f.readlines()
        
    new_lines = []
    for line in pt_lines:
        parts = line.split("::")
        if len(parts) >= 3 and parts[0].isdigit():
            label = parts[1]
            correct_id = label_to_id.get(label)
            if correct_id and parts[0] != correct_id:
                parts[0] = correct_id
                line = "::".join(parts)
                changed = True
        new_lines.append(line)
        
    if changed:
        with codecs.open(pt_path, "w", encoding="utf-8") as f:
            f.writelines(new_lines)
        print(f"Fixed IDs in {filename}")

print("Done checking all completed files.")
