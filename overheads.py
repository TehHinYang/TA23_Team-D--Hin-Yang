from pathlib import Path
import csv
def overheads_function():
  percentage = []
  overheads = {}
  file_path = Path.cwd()/"csv_reports"/"overheads-day-50.csv"
  with file_path.open(mode="r", encoding = "UTF-8") as file:
    reader = csv.reader(file)
    next(reader)
    for line in reader:
      data = float(line[1])
      percentage.append(data)
      cat = line[0]
      overheads[data] = cat
    highest = max(percentage)
    highest_cat = overheads[highest]
    message = f"[HIGHEST OVERHEADS] {highest_cat.upper()}: {highest}%"
    return message
    
print(overheads_function())
