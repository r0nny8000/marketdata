#!/usr/bin/env python3

import fire
import json

from marketdata.yfinanceapi import ticker

def getdata(symbol='MMM'):
    result = ticker(symbol)

    # print(json.dumps(result, indent=4))
    print("----")
    print(result['longName'] + " " + result['sector'] + " " + result['industry'])

def main():
  fire.Fire(getdata)

if __name__ == '__main__':
     main()
