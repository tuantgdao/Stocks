import json

def dataToJson(data) :
    dataStr = str(data)
    dataObj = dataStr.split()
    startIndex = 9
    lineInterval = 6
    dataJson = {}
    while startIndex < len(dataObj):
        comp = dataObj[startIndex:startIndex+lineInterval]
        dataJson[comp[0]] = {
            'open' : comp[1],
            'high' : comp[2],
            'low' : comp[3],
            'close' : comp[4],
            'volume' : comp[5]
        }
        startIndex = startIndex+lineInterval + 2
    dataJson = json.dumps(dataJson)
    return dataJson

def massSerialize(data):
    print(data)