import yfinance as yf

class Stock:

    period = '1mo'
    interval = '1wk'

    def __init__(self, ticker, name):
        self.ticker = ticker
        self.name = name
        self.price_history = {}
        self.events = {}
        data = self.getData()
        self.populateData(data)

    def getData(self):
        stock = yf.Ticker(self.ticker)
        data = stock.history(period=Stock.period, interval=Stock.interval)
        return data

    def populateData(self, data):
        print(data)

amd = Stock('msft', 'advanced')