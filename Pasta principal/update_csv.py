import csv

csv_path = r"c:\Users\Thiago\Desktop\FHA-Remastered-PT-BR\Pasta principal\etapas_traducao_qwen_codex_prompt_fha_qmax.csv"

with open(csv_path, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

for row in rows:
    if row.get("etapa") == "41":
        row["status_prompt_fha_qmax"] = "CONCLUÍDO"

with open(csv_path, "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print("Batch 40 updated.")
