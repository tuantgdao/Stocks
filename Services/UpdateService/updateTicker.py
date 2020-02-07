import yfinance as yf
import datetime
import sys
import json
from Services.Util import jsonSerializer as serializer
from Services.Util import prettyPrinter as printer
from Services.Util import getStockTickers as gt

def updateTicker(ticker):
    stock = yf.Ticker(ticker)
    #data = stock.history(start="2020-01-15", end="2020-01-22", interval='5d')
    data = stock.history(period="1wk", interval='1wk')
    json = serializer.dataToJson(data, ticker)
    return json

def updateAllTickers():
    print('Updating ALL tickers')
    tickers = gt.getStockTickers()
    data = {}
    for ticker in tickers:
        tickerJson = updateTicker(ticker[0])
        tickerPython = json.loads(tickerJson)
        data.update(tickerPython)
    return data

if len(sys.argv) < 2:
    print("Usage: python updateTicker.py (all|ticker1, ticker2, ...)", file=sys.stderr)
elif len(sys.argv) == 2 and sys.argv[1] == 'all':
    updateAllTickers()
else:
    for arg in range(1, len(sys.argv)):
        ticker = sys.argv[arg]
        print('Updating tickers {}'.format(ticker))
        updateTicker(ticker)
