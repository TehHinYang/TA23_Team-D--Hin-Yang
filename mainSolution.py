import requests
api_key= "RNPKUJP5Z7T08SJ0"
url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_key}"

response = requests.get(url)
<<<<<<< HEAD
print(response.json())
print(response)
=======
data = response.json()
>>>>>>> 77f3eb71f3975e943ef787242b2cfb182cb18ef3
