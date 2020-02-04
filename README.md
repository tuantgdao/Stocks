# Stocks

## Description
This project has 2 goals:
1. Keep a database history of rises and drops in stock prices
2. Keep a timeline of events going back 5 years for stocks
3. Create a service for users to query the data from the database
4. Classify the events with price increase/drops
5. Use ML to try and predict upcoming changes based on upcoming events

## Components
1. DB to hold stock price history and events
    * Schema
        - Stocks (Table)
            - AMD (Entry)
                - Name
                - Price History
                    - Date
                        - Low
                        - High
                        - Closing
                        - Open
                        - Volume
                - Events
                    - Date
                        - Link(Nullable)
                        - Type
    * More read heavy since we only have to write once a week for each stock
    * Indexes where?
2. Service to fill out Stocks DB price history
    * Use yfinance
3. Service to scrape google and get past events
4. Service to get upcoming events
5. ML service to classify events
    * Reads each event and records its impact on 
6. ML service to predict increases/decreases to specific stocks
7. ML service to predict global increases/decreases to specific industries

## ToDo
- [x] SQL vs NoSQL for DB?
    NoSQL to learn
- [x] Service to get a list of all stock tickers
    http://www.eoddata.com/stocklist/NASDAQ/M.htm
    * Have to create a service to check this and update it weekly
