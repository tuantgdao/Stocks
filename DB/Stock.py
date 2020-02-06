import yfinance as yf
import json
import pprint

class Stock:

    period = '1wk'
    interval = '1d'

    def __init__(self, ticker, name):
        self.ticker = ticker
        self.name = name
        self.price_history = {}
        self.events = {}
        data = self.getData()
        self.populateData(data)

    def getHistory(self):
        data = json.loads(self.price_history)
        return data

    def getData(self):
        stock = yf.Ticker(self.ticker)
        data = stock.history(period=Stock.period, interval=Stock.interval)
        return data

    def populateData(self, data):
        dataStr = str(data)
        dataObj = dataStr.split()
        startIndex = 9
        lineInterval = 6
        while startIndex < len(dataObj):
            comp = dataObj[startIndex:startIndex+lineInterval]
            self.price_history[comp[0]] = {
                'open' : comp[1],
                'high' : comp[2],
                'low' : comp[3],
                'close' : comp[4],
                'volume' : comp[5]
            }
            startIndex = startIndex+lineInterval + 2
        self.price_history = json.dumps(self.price_history)

amd = Stock('amd', 'advanced')

testData = {'2020-02-05' : 
                {
                    'open' : '999',
                    'high' : '000',
                    'low' : '111',
                    'close' : '222',
                    'volume' : '123456789'
                }
            }
dataString = json.dumps(testData)
testJson = json.loads(dataString)
prettyPrint(testJson)
historyJson = amd.getHistory()
prettyPrint(historyJson)
historyJson.update(testJson)
prettyPrint(historyJson)