import yfinance


def ticker(symbol):
    s = yfinance.Ticker(symbol)
    return s.dividends
    

