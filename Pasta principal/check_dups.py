import os
import codecs
from collections import Counter

dir_path = r"c:\Users\Thiago\Desktop\FHA-Remastered-PT-BR\Pasta principal\scripts_pt-br"
all_files = [f for f in os.listdir(dir_path) if f.endswith(".epk_dec")]

problematic_files = {}

for file in all_files:
    path = os.path.join(dir_path, file)
    with codecs.open(path, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()
    
    ids = []
    for line in lines:
        parts = line.split("::")
        if len(parts) >= 3 and parts[0].isdigit():
            ids.append(parts[0])
            
    id_counts = Counter(ids)
    duplicates = {k: v for k, v in id_counts.items() if v > 1}
    
    if duplicates:
        problematic_files[file] = duplicates

if problematic_files:
    print("Files with duplicate IDs:")
    for f, dups in problematic_files.items():
        print(f"  {f}: {len(dups)} duplicate IDs")
        # print some of them
        print(f"    Sample: {list(dups.keys())[:5]}")
else:
    print("No duplicate IDs found in any translated file.")
