import pandas as pd
import requests as req
import datetime


def getdata(start, end, assets):

    #data = {}
    #for a in assets:
    #    d = historicalData(a)
    #    data[a] = d['timestamp', 'close']
  
    BTC = historicalData("BTC")#['timestamp', 'close']
    ETH = historicalData("ETH")#['timestamp', 'close']
    
    print(BTC.head())
    print(ETH.head())
    data = pd.concat([BTC, ETH])
    print(data.head())
    return data


def historicalData(symbol="BTC", comparison_symbol="USD", all_data=True, limit=1, aggregate=1, exchange=''):
    url = 'https://min-api.cryptocompare.com/data/histoday?fsym={}&tsym={}&limit={}&aggregate={}'\
            .format(symbol.upper(), comparison_symbol.upper(), limit, aggregate)
    if exchange:
        url += '&e={}'.format(exchange)
    if all_data:
        url += '&allData=true'
    page = req.get(url)
    data = page.json()['Data']
    #print(data)
    df = pd.DataFrame(data)
    df['timestamp'] = [datetime.datetime.fromtimestamp(d) for d in df.time]
    return df