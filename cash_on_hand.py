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
    num = 1
    difference =[]
    messages = []
    while num < len(amt_coh):
      diff = float(amt_coh[num]) - float(amt_coh[num-1])
      difference.append(diff)
      difference.sort()
      num += 1
      if diff <= 0:
        diff = api.forex*abs(diff)
        messages.append(f"[CASH DEFICIT] DAY: {day[num-1]}, AMOUNT: SGD{round(diff,2)}")
      else:
        continue
    if difference[0] > 0:
      messages.append("[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
    return messages
      
print(cash_on_hand_function())

