import yfinance as yf
import datetime
import sys
from Services.Util import jsonSerializer as serializer
from Services.Util import prettyPrinter as printer
from Services.Util import getStockTickers as gt

def updateTicker(ticker):
    stock = yf.Ticker(ticker)
    data = stock.history(period='1d', interval='1d')
    json = serializer.dataToJson(data)
    return json

def updateAllTickers(tickers):
    tickersString = ' '.join([ticker[0] for ticker in tickers])
    data = yf.download(tickersString, period='1d', interval='1d')
    serializer.massSerialize(data)

if len(sys.argv) < 2:
    print("Usage: python updateTicker.py (all|ticker1, ticker2, ...)", file=sys.stderr)
elif len(sys.argv) == 2 and sys.argv[1] == 'all':
    print('Updating ALL tickers')
    tickers = gt.getStockTickers()
    for ticker in tickers:
        updateTicker(ticker[0])
    # updateAllTickers(tickers)
else:
    for arg in range(1, len(sys.argv)):
        ticker = sys.argv[arg]
        print('Updating tickers {}'.format(ticker))
        updateTicker(ticker)
