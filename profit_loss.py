from pathlib import Path
import csv,api

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
        while num < len(net_profit):
            diff = float (net_profit[num]) - float(net_profit[num-1])
            difference.append(diff)
            difference.sort()
            num += 1
            if diff <= 0:
                diff = api.forex*abs(diff)
                messages.append(f"[PROFIT DEFICIT] DAY: {day[num-1]}, AMOUNT: SGD{round(diff, 2)}")
            else:
                continue
        if difference[0] > 0:
            messages.append("[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
        return messages

print(profit_loss_function())