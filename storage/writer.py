# 2025-12-15

import json
import csv
from pathlib import Path

def save_raw_json(path: str, data: list): 
	Path(path).parent.mkdir(parents=True, exist_ok=True)
	with open(path, "w", encoding="utf-8") as f:
		json.dump(data, f, ensure_ascii=False, indent = 2)

def save_csv(path: str, rows: list):
	if not rows :
		return


	Path(path).parent.mkdir(parents=True, exist_ok=True)
	with open(path, "w", encoding="utf-8") as f:
		writer = csv.DictWriter(f,fieldnames=rows[0].keys())
		writer.writeheader()
		writer.writerows(rows)

