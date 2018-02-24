import numpy as np
import pandas as pd
import quandl_data_reading as qd
import pandas_datareader_data_reading as pdr
import matplotlib.pyplot as plt
import get_effecient_frontier as gf
import datetime
import plot_graph as plt

#assets = ['AAPL', 'FB', 'MSFT', 'TWTR', 'AIR', 'TSLA']
assets = ['CNP', 'F', 'WMT', 'GE', 'TSLA']
#assets = ['F']


startDate = datetime.datetime(2017, 1, 1)
endDate = datetime.datetime(2018, 12, 31) 

# Using Pandas_Data_Reader Data
#data_reader = pdr.getdata(startDate, endDate, assets, dataSource='robinhood', columnToRead = 'close_price')
#data_reader = pdr.getdata(startDate, endDate, assets, dataSource='morningstar', columnToRead = 'Close')
data_reader = pdr.getdata(startDate, endDate, assets)
df = gf.get_effecient_frontier(data_reader, assets, 50000, 0)
plt.drawGraph(df, 'Efficient Frontier Using Pandas_Data_Reader')

# Using Quandl Data
data = qd.getdata(startDate, endDate, assets)
df = gf.get_effecient_frontier(data, assets, 50000, 0)
plt.drawGraph(df, 'Efficient Frontier Using Quandl')
