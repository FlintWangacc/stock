#!/bin/python3

import requests
import yfinance as yf
import time

def get_dividends_and_yield(ticker):
    try:
        stock = yf.Ticker(ticker)
        dividends = stock.dividends
        #forward_dividends = stock.forward_dividends
        #forward_dividend_yield = stock.forward_dividend_yield

        return stock.dividends.tail(1)[0] / stock.info['previousClose'] 
    except:
        return 0

def get_csi300_stocks():
    #url = "https://csi-web-dev.oss-cn-shanghai-finance-1-pub.aliyuncs.com/static/html/csindex/public/uploads/file/autofile/cons/000300cons.xls"
    url = "https://csi-web-dev.oss-cn-shanghai-finance-1-pub.aliyuncs.com/static/html/csindex/public/uploads/file/autofile/cons/399986cons.xls"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.content
        stocks = []

        # Parse the data using a library like pandas
        # You may need to install pandas using pip install pandas
        import pandas as pd
        df = pd.read_excel(data, skiprows=1)

        for _, row in df.iterrows():
            #print(type(row))
            #print(row["指数代码 Index Code"])
            #print(row[0])
            #print('\n')
            stock_code = row[4]
            stock_name = row[5]
            stock_exchange = row[8]
            if stock_exchange == 'Shanghai Stock Exchange':
                stock_symbol = str(stock_code).zfill(6) + '.' + 'SS'
            if stock_exchange == 'Shenzhen Stock Exchange':
                stock_symbol = str(stock_code).zfill(6) + '.' + 'SZ'
            #time.sleep(0.5)
            print(stock_symbol)
            forward_dividend_yield = get_dividends_and_yield(stock_symbol)
            stocks.append((stock_code, stock_name, stock_exchange, stock_symbol, forward_dividend_yield))

        return stocks
    else:
        print("Failed to retrieve CSI300 stocks.")
        return []

# Usage example
stocks = get_csi300_stocks()
for stock_code, stock_name, stock_exchange, stock_symbol, forward_dividend_yield in stocks:
    #forward_dividend_yield = get_dividends_and_yield(stock_symbol)
    print(stock_code, stock_name, stock_exchange, stock_symbol, forward_dividend_yield)
    #print(stock_code, stock_name, stock_exchange, stock_symbol)

