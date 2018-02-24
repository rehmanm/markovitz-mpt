import pandas_datareader as web
import pandas as pd
def getdata(start, end, assets, dataSource = 'iex', columnToRead = 'close'):

    data = {}
    for a in assets:
        d = web.DataReader(a, dataSource, start, end)[columnToRead]
        data[a] = d
 
    data = pd.DataFrame(data)

    return data