from pathlib import Path
import csv,api
def cash_on_hand_function():
    amt_coh = []
    day = []
    file_path = Path.cwd()/"csv_reports"/"cash-on-hand-usd.csv"
    print(file_path.exists())
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
        while num < len(amt_coh):
            diff = float(amt_coh[num]) - float(amt_coh[num-1])
            #print(diff)
            difference.append(diff)
            difference.sort()
            num += 1
            if diff < 0:
                #diff = api.api_funtion()*abs(diff)
                #print(diff)
                #print(api.api_funtion())
                message = f"[CASH DEFICIT] DAY: {day[num-1]}, AMOUNT: SGD{abs(diff)*api.api_funtion()}"
            else:
                continue
            print(message)
        if difference[0] > 0:
            message = f"[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY"
            print(message)

cash_on_hand_function()