#!/bin/python3

import yfinance as yf
import datetime

# Function to get the lowest closing price and date
def get_lowest_close(symbol):
    # Get the data for the specified symbol
    ticker = yf.Ticker(symbol)
    # Get the historical data for the last 60 days
    history = ticker.history(period='60d')

    # Get the date and lowest close price
    lowest_close = history['Low'].min()
    lowest_date = history[history['Low'] == lowest_close].index[0].strftime('%Y-%m-%d')

    return lowest_close, lowest_date

# Example usage
symbol = '000300.SS'
lowest_close, lowest_date = get_lowest_close(symbol)

# Print the result
print("The lowest closing price for ", symbol, "in the last 60 days was ", lowest_close, " on ", lowest_date)
symbol = "159929.SZ"
lowest_close, lowest_date = get_lowest_close(symbol)
print("The lowest closing price for ", symbol, "in the last 60 days was ", lowest_close, " on ", lowest_date)
symbol = "399006.SZ"
lowest_close, lowest_date = get_lowest_close(symbol)
print("The lowest closing price for ", symbol, "in the last 60 days was ", lowest_close, " on ", lowest_date)
symbol = "000932.SS"
lowest_close, lowest_date = get_lowest_close(symbol)
print("The lowest closing price for ", symbol, "in the last 60 days was ", lowest_close, " on ", lowest_date)
