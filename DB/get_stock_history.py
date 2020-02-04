import yfinance as yf

def populateStockHistory(ticker, period, interval):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period, interval=interval)
    print(data)

populateStockHistory('AMD')
# msft = yf.Ticker('MSFT')
# # history = msft.history(period="1mo")
# # print(history)

# data = yf.download(tickers='AMD', period='1mo', interval='1wk')
# print(data)