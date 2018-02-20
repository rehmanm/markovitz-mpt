import quandl

def getdata(start, end, stock, column = ['date', 'ticker', 'adj_close']):
    quandl.ApiConfig.api_key = '_sbkgpPqyHKZTMdzkace'
    data = quandl.get_table('WIKI/PRICES', ticker = stock,
                        qopts = { 'columns': ['date', 'ticker', 'adj_close'] },
                        date = { 'gte': start, 'lte': end }, paginate=True)
    clean = data.set_index('date')
    table = clean.pivot(columns='ticker')
    return table