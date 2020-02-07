from flask import Flask, request
import Services.UpdateService.updateTicker as update

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello there from docker"

@app.route('/updateTicker')
def updateTicker():
    ticker = request.args.get('ticker')
    if ticker == "all":
        return update.updateAllTickers()
    else:
        return update.updateTicker(ticker)