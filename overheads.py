# import modules
from pathlib import Path
import csv,api

# create a function to determine the highest overheads
def overheads_function():
  # create an empty list
  percentage = []
  # create an empty dictionary
  overheads = {}
  # create a file path to overheads csv file
  file_path = Path.cwd()/"csv_reports"/"overheads-day-50.csv"
  # open file to read the data in the file
  with file_path.open(mode="r", encoding = "UTF-8") as file:
    # read the data in the csv file 
    reader = csv.reader(file)
    # skip the header in the data
    next(reader)
    # for loop to iterate each item in the 'reader'
    for line in reader:
      # extract the percentage for each expense from the csv file and change it into a float
      data = float(line[1])
      # append the data into the empty list
      percentage.append(data)
      # extract the category from the csv file 
      cat = line[0]
      # add a new value pair into the empty dictionary
      overheads[data] = cat
    # extract the highest value in the 'percentage' list
    highest = max(percentage)
    # extract the category name for the highest percentage from the dictionary
    highest_cat = overheads[highest]
    # create a variable message with f-string showing the highest overheads in SGD
    message = f"[HIGHEST OVERHEADS] {highest_cat.upper()}: SGD{round(highest*api.forex,2)}"
    # return information on highest overheads
    return message

# print function to show the result    
print(overheads_function())
