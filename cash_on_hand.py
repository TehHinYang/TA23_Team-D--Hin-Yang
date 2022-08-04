# import modules
from pathlib import Path
import csv,api

# create a function to determine the difference in cash on hand between each day
def cash_on_hand_function():
  """
  - This function reads the cash on hand values in the csv files and calculates the differences for each days. It then determines whether it is a surplus of deflict
  """
  # create an empty list
  amt_coh = []
  # create an empty list
  day = []
  # create a file path to cash on hand csv file
  file_path = Path.cwd()/"csv_reports"/"cash-on-hand-usd.csv"
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
      # extract the amount of cash on hand from the csv file
      data = line[1]
      # append the data into the empty list
      amt_coh.append(data)
      # append the days into the empty list
      day.append(days)
    # create a variable 'num' and assign a value of 1 to represent the index position of the data
    num = 1
    # create an empty list
    difference =[]
    # create an empty list
    messages = []
    # create a while loop to add in the cash deficit from day 40 to 50
    while num < len(amt_coh):
      # start handling exception 
      try:
        # extract the amount and change it into a float and find the difference on cash on hand between each day
        diff = float(amt_coh[num]) - float(amt_coh[num-1])
      # handling ValueError
      except ValueError:
        # append the message for ValueError into an empty list
        messages.append("Make sure it is a number")
        # return the message for ValueError
        return messages
      # when there is no exceptions
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
        messages.append(f"[CASH DEFICIT] DAY: {day[num-1]}, AMOUNT: SGD{round(diff,2)}")
      # if statement to have a condition for 'diff' more than 0
      else:
        # skip on to the next iteration
        continue
    # if statment to have a condition of the first data in 'difference' being positive
    if difference[0] > 0:
      # append the message into an empty list
      messages.append("[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
    # return information on the cash on hand
    return messages

# print function to show result      
print(cash_on_hand_function())