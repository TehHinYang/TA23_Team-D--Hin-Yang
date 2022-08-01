from pathlib import Path
import csv,api

def cash_on_hand_function():
  amt_coh = []
  day = []
  file_path = Path.cwd()/"csv_reports"/"cash-on-hand-usd.csv"
  with file_path.open(mode="r", encoding="UTF-8") as file:
    reader = csv.reader(file)
    next(reader)
    for line in reader:
      days = line[0]
      data = line[1]
      amt_coh.append(data)
      day.append(days)
      
print(cash_on_hand_function())
