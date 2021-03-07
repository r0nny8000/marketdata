#!/usr/bin/env python3

import fire

from marketdata_cli.yfinancedata import ticker

def ticker(symbol):
    print(symbol + ': ' + ticker(symbol))

if __name__ == '__main__':
    fire.Fire(hello)