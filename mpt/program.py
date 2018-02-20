import numpy as np
import pandas as pd
import quandl_data_reading as qd
import matplotlib.pyplot as plt
import get_effecient_frontier as gf

data = qd.getdata('2016-01-01', '2018-12-31', ['AAPL', 'FB', 'MSFT', 'TWTR', 'AIR', 'TSLA'])

print(gf.get_effecient_frontier(data))

