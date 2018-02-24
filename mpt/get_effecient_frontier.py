import numpy as np
import pandas as pd

TOTAL_NUMBER_OF_DAYS_IN_YEAR = 250 #Working Days in a Year 250/252

def get_sharpe_ratio(expected_portfolio_asset_return, risk_free_return, portfolio_std):
    return (expected_portfolio_asset_return - risk_free_return)/portfolio_std


def get_effecient_frontier(data, assets, num_of_portfolios=50000, risk_free_return = 0.1):
    daily_return = data.pct_change()
    annual_return = daily_return.mean() * TOTAL_NUMBER_OF_DAYS_IN_YEAR

    # get daily and covariance of returns of the stock
    daily_covariance = daily_return.cov()
    annual_covariance = daily_covariance * TOTAL_NUMBER_OF_DAYS_IN_YEAR
    
    num_assets = len(assets)
    port_returns = []
    port_volatility = []
    stock_weights = []
    sharpe_ratio = []

    for single_portfolio in range(num_of_portfolios):
        weights = np.random.rand(num_assets)
        weights /= np.sum(weights)
        returns = np.dot(weights, annual_return)
        volatility = np.sqrt(np.dot(weights.T, np.dot(annual_covariance, weights)))
        sharpe_ratio.append(get_sharpe_ratio(returns, risk_free_return, volatility))
        port_returns.append(returns)
        port_volatility.append(volatility)
        stock_weights.append(weights)

    portfolio = {
                    'Returns': port_returns,
                    'Volatility': port_volatility,
                    'Sharpe Ratio': sharpe_ratio
                }

    for counter,symbol in enumerate(assets):
        portfolio[symbol+' weight'] = [weight[counter] for weight in stock_weights]
 
    # make a nice dataframe of the extended dictionary
    df = pd.DataFrame(portfolio)

    # get better labels for desired arrangement of columns
    column_order = ['Returns', 'Volatility', 'Sharpe Ratio'] + [stock+' weight' for stock in assets]
    # reorder dataframe columns
    df = df[column_order]

    return df

