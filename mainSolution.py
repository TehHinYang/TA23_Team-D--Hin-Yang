from pathlib import Path
import cash_on_hand,overheads,profit_loss,api

def mainsoultion_function():
    fp = Path.cwd()/"summary_report.txt"
    fp.touch()
    data = cash_on_hand.cash_on_hand_function()
    data1 = profit_loss.profit_loss_function()
    num = 0
    num1 = 0
    with fp.open(mode="w", encoding="UTF-8", newline="") as file:
        file.writelines(api.api_funtion())
    with fp.open(mode="a", encoding="UTF-8", newline="") as file:
        file.writelines(f"\n{overheads.overheads_function()}")
        while num < len(data):
            file.writelines(f"\n{data[num]}")
            num += 1
        while num1 < len(data1):
            file.writelines(f"\n{data1[num1]}")
            num1 += 1

mainsoultion_function()