import requests
import webbrowser

# url = 'http://www.eoddata.com/Data/symbollist.aspx'
# chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito"

# webbrowser.get(chrome_path).open(url)

# # URL = 'http://www.eoddata.com/Data/symbollist.aspx'
# # PARAMS = {'e' : 'NASDAQ'}

# # r = requests.get(URL)


# print(html.fromstring(r.text))

def getStockTickers():
    stockTickers = open("Services/Util/testTickers.txt", "r")
    stockList = list()
    for stock in stockTickers.readlines():
        stock = stock.strip('\n')
        stockSymbol = stock.split("\t")
        stockList.append(stockSymbol)
    stockTickers.close()
    return stockList