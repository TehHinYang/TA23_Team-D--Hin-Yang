# import modules
from pathlib import Path
import cash_on_hand,overheads,profit_loss,api

# create a function to add all the information into a text file
def mainsoultion_function():
    # create a file path and create a new file 'summary_report.txt
    fp = Path.cwd()/"summary_report.txt"
    # Create the file
    fp.touch()
    # create a variable 'num' and assign a value of 0 to represent the index position of the data
    num = 0
    # create a variable 'num' and assign a value of 0 to represent the index position of the data
    num1 = 0
    # open file path to write data in the file
    with fp.open(mode="w", encoding="UTF-8", newline="") as file:
        # write the output of 'api_functiion()' from api file into the file
        file.writelines(api.api_funtion())
    # open file path to append data in the file
    with fp.open(mode="a", encoding="UTF-8", newline="") as file:
        # append the output of 'overheads_function()' from overheads file into the file in next line
        file.writelines(f"\n{overheads.overheads_function()}")
        # create a while loop to append the output into the file
        while num < len(cash_on_hand.cash_on_hand_function()):
            # extract the messages from a list in the 'cash_on_hand_function()' from cash_on_hand file and append into the file
            file.writelines(f"\n{cash_on_hand.cash_on_hand_function()[num]}")
            # add a value of 1 to 'num'
            num += 1
        # create a while loop to append the output into the file
        while num1 < len(profit_loss.profit_loss_function()):
            # extract the messages from a list in the 'profit_loss_function()' from profit_loss file and append into the file
            file.writelines(f"\n{profit_loss.profit_loss_function()[num1]}")
            # add a value of 1 to 'num1'
            num1 += 1

# excute the function
mainsoultion_function()