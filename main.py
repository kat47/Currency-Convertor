"""
Alpha Vantage Frequncy Conversion
To convert usd to inr using api calls
api key : get your api key from https://www.alphavantage.co/support/#api-key
"""
import requests
import json
def convert(conv):
    data = requests.get('https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=INR&\
    apikey=demo') #replace your api key with demo
    #print(type(data.content))
    val = json.loads(data.content)
    #print(type(val))
    from_cur = val['Realtime Currency Exchange Rate']['1. From_Currency Code']
    to_cur = val['Realtime Currency Exchange Rate']['3. To_Currency Code']
    rate = float(val['Realtime Currency Exchange Rate']['5. Exchange Rate'])
    print(f"{conv} {from_cur} = {conv*rate} {to_cur}")

if __name__ == "__main__":
    conv = float(input('Enter a value to convert '))
    convert(conv)
