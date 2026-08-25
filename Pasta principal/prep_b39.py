import os
import re

base_dir = r"c:\Users\Thiago\Desktop\FHA-Remastered-PT-BR\Pasta principal"
en_dir = os.path.join(base_dir, "scripts_en")

files = [
    "28efftgc8opkti8b8ndsrirhcl.epk_dec",
    "288ffrbpak7lqbjkgmroaf4gjc.epk_dec",
    "270pptv5rtedgd0123n96c64aa.epk_dec",
    "25i9em67k9sc67fl1ojv27rgv3.epk_dec",
    "24gktqa6bq0hkdom3s4pjejvvm.epk_dec"
]

def clean_file(filename, output_name):
    filepath = os.path.join(en_dir, filename)
    out_path = os.path.join(base_dir, output_name)
    
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.read().splitlines()
        
    with open(out_path, 'w', encoding='utf-8') as out:
        for i, line in enumerate(lines):
            # Ensure we keep the exact trailing spaces if they exist, except trailing newline
            out.write(line + "\n")

for i, file in enumerate(files):
    clean_file(file, f"temp_b39_{i+1}_clean.txt")
