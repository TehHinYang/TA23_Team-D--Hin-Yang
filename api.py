import requests,json
api_key= "RNPKUJP5Z7T08SJ0"
url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_key}"
response = requests.get(url)
data = response.json()
forex = data["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
forex = float(forex)

def api_funtion():
    api_key= "RNPKUJP5Z7T08SJ0"
    url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    #data.keys()
    #json.dumps(data["Realtime Currency Exchange Rate"], indent=4)
    forex = data["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
    forex = float(forex)
    message = f"[REAL TIME CURRENCY RATE] USD1 = SGD{forex}"
    return message

print(api_funtion())