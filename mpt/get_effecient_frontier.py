import numpy as np

TOTAL_NUMBER_OF_DAYS_IN_YEAR = 250 #Working Days in a Year 250/252

def get_effecient_frontier(data):
    daily_return = data.pct_change()
    annual_return = daily_return.mean() * TOTAL_NUMBER_OF_DAYS_IN_YEAR

    # get daily and covariance of returns of the stock
    daily_covariance = daily_return.cov()
    annual_covariance = daily_covariance * TOTAL_NUMBER_OF_DAYS_IN_YEAR
  
    return annual_covariance

