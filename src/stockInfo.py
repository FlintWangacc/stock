#!/bin/python3

import yfinance as yf
import sys
from datetime import date

class StockInfo:
  def __init__(self, stockCode, stockName, stockExchange):
    exMap = {'Shanghai Stock Exchange':'SS', 
             'Shenzhen Stock Exchange':'SZ'}
    self.stockName = stockName
    self.stockCode = str(stockCode).zfill(6)
    stockSymbol = self.stockCode + '.' + exMap[stockExchange]
    self.stockSymbol = stockSymbol
    try:
      self.stockInfo = yf.Ticker(self.stockSymbol)
      #self.currentPrice = None
      #self.lastDividend = None
    except Exception as e:
      print("An exception occured", str(e))
      traceback.print_exc()
      sys.exit(1)
      
  def getDividendLast(self):
    try:
      return self.stockInfo.dividends.get(self.lastDividendDate, 0)

    except Exception as e:
      print("An exception occured", str(e))
      traceback.print_exc()
      sys.exit(1)

  def getDividendLastDate(self):
    try:
      return self.stockInfo.dividends.index[-1].strftime("%Y-%m-%d")
    except IndexError as e:
      print(self.stockName + " has no dividends")
      return "0000-00-00"
    
  def getCurrentPrice(self):
    try:
      p = self.stockInfo.info['currentPrice']
      return p
    except Exception as e:
      print("An exception occured", str(e))
      traceback.print_exc()
      sys.exit(1)

  def getMarketCap(self):
    try:
      p = self.stockInfo.info['marketCap']
      return p
    except Exception as e:
      print("An exception occured", str(e))
      traceback.print_exc()
      sys.exit(1)

  def getLastTotalRevenue(self):
      try:
        currentYear = date.today().year
        lastDayLastYear = date(currentYear - 1, 12, 31)
        lastString = lastDayLastYear.strftime("%Y-%m-%d")
        r = self.stockInfo.financials.loc['Total Revenue'][lastString]
        return r
      except Exception as e:
        print("An exception occured", str(e))
        traceback.print_exc()
        sys.exit(1)

  def getDividPerShare(self):
    return self.lastDividend / self.currentPrice

  def __str__(self):
      percentString = "{:.3%}".format(self.dividPerShare)
      return "Name:{0}\tstockCode:{1}\tDividPerShare:{2}\n".format(self.stockName,
              self.stockCode, percentString)

  def __getattr__(self, name):
    methodMap = {'currentPrice' : self.getCurrentPrice,
                 'lastDividend' : self.getDividendLast,
                 'dividPerShare' : self.getDividPerShare,
                 'lastDividendDate': self.getDividendLastDate,
                 'marketCap': self.getMarketCap,
                 'lastTotalRevenue' : self.getLastTotalRevenue
                }
    self.__dict__[name] = methodMap[name]()
    return self.__dict__[name]


if __name__ == '__main__':
  stock = StockInfo(600362, '江西铜业', 'Shanghai Stock Exchange')
  print(stock.stockSymbol)
  print(stock.stockInfo.info['currentPrice'])
  print(stock.currentPrice)
  #print(stock.lastDividend /stock.currentPrice)
