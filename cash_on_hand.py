<<<<<<< HEAD
from pathlib import Path
import csv
fp = Path.cwd()/"summary_report.txt"
fp.touch()

=======
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
>>>>>>> 2cec0c446b2ed95f4aeb1641c4bd6c29fe075f5e
