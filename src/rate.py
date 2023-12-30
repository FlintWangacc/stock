#!/bin/python3

import yfinance as yf

# Define the ticker symbol of the stock you want to compare
ticker_symbol = '600036.SS'

# Create a Ticker object for the specified stock
stock = yf.Ticker(ticker_symbol)

# Retrieve the historical dividend data for the stock
dividend_data = stock.dividends

# Filter the dividend data for the past year
one_year_dividends = dividend_data.loc['2021-01-01':'2021-12-31']

# Calculate the average dividend rate for the past year
forward_dividend_rate = stock.info['forwardDividendRate']

# Print the average dividend rate for the past year
print(f"The average dividend rate for {ticker_symbol} over the past year is: {forward_dividend_rate:.2f}")
