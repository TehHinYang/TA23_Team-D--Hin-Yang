# import modules
from pathlib import Path
import csv,api

# create a function to determine the difference in net profit between each day
def profit_loss_function():
    """
    -This function reads the data from csv file and extracts both the day and net profit values to find the difference in net profit each day. 
    -It then determines which whether the business has a surplus or a deflict based on the values.
    """
  
    # create an empty list
    net_profit = []
    # create an empty list
    day = []
    # create a file path to profit and loss csv file
    file_path = Path.cwd()/"csv_reports"/"profit-and-loss-usd (1).csv"
    # open file to read the data in the file
    with file_path.open(mode="r", encoding="UTF-8") as file:
        # read the data in the csv file
        reader = csv.reader(file)
        # skip the header in the data
        next(reader)
        # for loop to iterate each item in the 'reader'
        for line in reader:
            # extract the days from the csv file
            days = line[0]
            # extract the net profit from the csv file
            data = line[4]
            # append the data into the empty list
            net_profit.append(data)
            # append the days into the empty list
            day.append(days)
         # create a variable 'num' and assign a value of 1 to represent the index position of the data
        num = 1
        # create an empty list
        difference =[]
        # create an empty list
        messages = []
        # create a while loop to add in the profit deficit from day 40 to 50
        while num < len(net_profit):
            try:
                # extract the amount and change it into a float and find the difference on net profit between each day
                diff = float (net_profit[num]) - float(net_profit[num-1])
            except ValueError:
                return "Make sure it is a number"
            else:
                # append the difference into an empty list
                difference.append(diff)
            # sort the data in the list from smallest to largest.
            difference.sort()
            # add a value of 1 to 'num'
            num += 1
            # if statement to have a condition of the 'diff' less than 1
            if diff <= 0:
                # change the amount in difference from USD to SGD
                diff = api.forex*abs(diff)
                # append all the message into an empty list
                messages.append(f"[PROFIT DEFICIT] DAY: {day[num-1]}, AMOUNT: SGD{round(diff, 2)}")
            # if statement to have a condition for 'diff' more than 0
            else:
                # skip on to the next iteration
                continue
        # if statment to have a condition of the first data in 'difference' being positive
        if difference[0] > 0:
            # append the message into an empty list
            messages.append("[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
        # return information on the net profit
        return messages

# print function to show result
print(profit_loss_function())
