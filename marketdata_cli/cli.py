#!/usr/bin/env python3

import fire
import json

from marketdata_cli.yfinancedata import ticker

def getdata(symbol):
    result = ticker(symbol)

    print(json.dumps(result, indent=4))

if __name__ == '__main__':
    fire.Fire(getdata)