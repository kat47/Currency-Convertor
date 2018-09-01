"""
Alpha Vantage Frequncy Conversion
To convert usd to inr using api calls
api key : get your api key from https://www.alphavantage.co/support/#api-key
"""
import requests
import json
def convert(conv):
    data = requests.get('https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=INR&\
    apikey=demo') # change demo with api key
    #print(type(data.content))
    val = json.loads(data.content)
    #print(type(val))
    from_cur = val['Realtime Currency Exchange Rate']['1. From_Currency Code']
    to_cur = val['Realtime Currency Exchange Rate']['3. To_Currency Code']
    rate = float(val['Realtime Currency Exchange Rate']['5. Exchange Rate'])
    final = conv*rate
    conv = format(conv,'.2f')
    final = format(final,'.2f')
    print(f"{conv} {from_cur} = {final} {to_cur}")

if __name__ == "__main__":
    conv = float(input('Enter a value to convert '))
    convert(conv)

