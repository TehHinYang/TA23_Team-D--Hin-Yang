from pathlib import Path
import csv,web_api

def profit_loss_function():
    net_profit = []
    day = []
    file_path = Path.cwd()/"profit-and-loss-usd (1).csv"
    with file_path.open(mode="r", encoding="UTF-8") as file:
        reader = csv.reader(file)
        next(reader)
        for line in reader:
            days = line[0]
            data = line[4]
            net_profit.append(data)
            day.append(days)
        num = 1
        difference =[]
        messages = []
