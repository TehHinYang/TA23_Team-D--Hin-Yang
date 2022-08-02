# import modules
import requests,json

# assign api key into a string
api_key= "RNPKUJP5Z7T08SJ0"
# f-string to insert api key into the url to get the exchange rate
url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_key}"
# request access to exchanges rate of usd to sgd and assign it as a variable called response
response = requests.get(url)
# retrieve data from response and save as data
data = response.json()
# use data.keys() to retrieve keys of a dictionary
# json.dumps(data["Realtime Currency Exchange Rate"], indent=4) to see the dictionary clearer
# extract the exchange rate
forex = data["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
# use the extracted data into a float
forex = float(forex)

# create a function
def api_funtion():
    # assign api key into a string
    api_key= "RNPKUJP5Z7T08SJ0"
    # f-string to insert api key into the url to get the exchange rate
    url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_key}"
    # request access to exchanges rate of usd to sgd and assign it as a variable called response
    response = requests.get(url)
    # retrieve data from response and save as data
    data = response.json()
    # use data.keys() to retrieve keys of a dictionary
    # json.dumps(data["Realtime Currency Exchange Rate"], indent=4) to see the dictionary clearer
    # extract the exchange rate
    forex = data["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
    # use the extracted data into a float
    forex = float(forex)
    # create a variable message with f-string about the information of the exchange rate
    message = f"[REAL TIME CURRENCY RATE] USD1 = SGD{forex}"
    # return information of exchange rate
    return message

# print function to show the result
print(api_funtion())