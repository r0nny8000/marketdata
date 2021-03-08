import yfinance


def ticker(symbol):
    s = yfinance.Ticker(symbol)
    # s.history(period='5y')
    return s.info
    

