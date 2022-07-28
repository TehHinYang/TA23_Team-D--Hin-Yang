from pathlib import Path
import csv
fp = Path.cwd()/"summary_report.txt"
fp.touch()

file_path = Path.cwd()/"cash-on-hand-usd.csv"
with file_path.open(mode="r", encoding="UTF-8") as file:
    reader = csv.reader(file)
    next(reader)
    for line in reader:
        data = line[1]