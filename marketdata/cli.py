#!/usr/bin/env python3

import fire
import json

from marketdata.yfinanceapi import ticker

def getdata(symbol='MMM'):
    result = ticker(symbol)

    print(json.dumps(result, indent=4))
    print(result['sector'])

if __name__ == '__main__':
    fire.Fire(getdata)