# Stocks

## Description

1. Keep a database history of rises and drops in stock prices
2. Keep a timeline of events going back 5 years for stocks
3. Create a service for users to query the data from the database
4. Classify the events with price increase/drops
5. Use ML to try and predict upcoming changes based on upcoming events

## Questions
1. What will I store in the DB?
    - Stock, price history, events
2. What do I need to retrieve from the DB?
    - Events, price history

## Components
- [x] DB to hold stock price history and events
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
- [x] Service to fill out Stocks DB price history
    * Use yfinance
- [ ] Service to scrape google and get past events
- [ ] Service to get upcoming events
- [ ] ML service to classify events
    * Reads each event and records its impact on 
- [ ] ML service to predict increases/decreases to specific stocks
- [ ] ML service to predict global increases/decreases to specific industries

## ToDo
- [x] SQL vs NoSQL for DB?
    NoSQL to learn
- [x] Service to get a list of all stock tickers
    http://www.eoddata.com/stocklist/NASDAQ/M.htm
    - [ ] Have to create a service to check this and update it on Saturdays
- [ ] Build a service to update histories on Saturdays
    - [ ] Once the data's in the db, updating the db is as easy as adding a new entry
- [ ] Create json serializer for parsing results from yfinance
- [ ] Setup a docker instance to execute the scripts
    - [ ] Setup the service in docker