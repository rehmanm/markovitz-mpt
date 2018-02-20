import numpy as np
import pandas as pd
import quandl_data_reading as qd


print(qd.getdata('2017-01-01', '2018-12-31', ['AAPL', 'FB', 'YHOO']))
