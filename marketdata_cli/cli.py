#!/usr/bin/env python3

import fire

from marketdata_cli.yfinancedata import ticker

def getdata(symbol):
    print(ticker(symbol))

if __name__ == '__main__':
    fire.Fire(getdata)