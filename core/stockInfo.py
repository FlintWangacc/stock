#!/bin/python3

import yfinance as yf
import sys
from datetime import date, datetime

class NocurrentPrice(Exception):
  def __init__(self, stockCode):
    self.stockCode = stockCode
    super().__init__(self.stockCode)

class StockInfo:
  def __init__(self, stockCode, stockName, stockExchange):
    exMap = {'Shanghai Stock Exchange':'SS', 
             'Shenzhen Stock Exchange':'SZ'}
    self.stockName = stockName
    self.stockCode = stockCode
    stockSymbol = self.stockCode + '.' + exMap[stockExchange]
    self.stockSymbol = stockSymbol
    try:
      print(f"{stockCode}:{stockName}")
      self.stockInfo = yf.Ticker(self.stockSymbol)
      #self.currentPrice = None
      #self.lastDividend = None
      self.financials = self.stockInfo.financials
      self.balanceSheet = self.stockInfo.balance_sheet
    except Exception as e:
      print("An exception occured", str(e))
      sys.exit(1)
      
  def getROE(self):
    try:
      netIncome = self.financials.loc['Net Income Common Stockholders'].iloc[0]
      shareholderEquity = self.balanceSheet.loc['Stockholders Equity'].iloc[0]
      roe = netIncome / shareholderEquity
      return roe

    except KeyError as e:
      print(f"KeyError: {e}.")

  def getLastYearDividend(self):
      try:
        currentYear = datetime.now().year
        lastYear = currentYear - 1
        div = 0.0
        for ts, d in self.stockInfo.dividends.items():
          if ts.year == lastYear:
            div += d
      except Exception as e:
        print(e)
      return div

  def getDividendForYear(year):
      divHistory = self.stockInfo.dividends

      if divHistory.empty:
          print(f"No dividen data available for {ticker}.")
          return 0

      divHistoryYear = divHistory[divHistory.index.year == year]

      totalDividend = divHistoryYear.sum()

      return totalDividend

  def getRateOfDividend(self):
      dividend = self.getLastYearDividend()
      price = self.getCurrentPrice()
      print(f"dividend:{dividend}")
      print(f"price:{price}")
      return dividend / price

  def getDividendLast(self):
    try:
      return self.stockInfo.dividends.get(self.lastDividendDate, 0)

    except Exception as e:
      print("An exception occured", str(e))
      sys.exit(1)

  def getDividendLastDate(self):
    try:
      return self.stockInfo.dividends.index[-1].strftime("%Y-%m-%d")
    except IndexError as e:
      print(self.stockName + " has no dividends")
      return "0000-00-00"
    
  def getCurrentPrice(self):
    try:
      print(self.stockInfo)
      if 'currentPrice' in self.stockInfo.info:
        p = self.stockInfo.info['currentPrice']
      else:
        p = self.stockInfo.info['open']
        #e = NocurrentPrice(self.stockCode)
        #print(f"raise {e}")
        #raise e
        #p = self.stockInfo.info['open']
      return p
    except Exception as e:
      print(e)

  def getMarketCap(self):
    try:
      p = self.stockInfo.info['marketCap']
      return p
    except Exception as e:
      print("An exception occured", str(e))
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
        sys.exit(1)

  def getDividPerShare(self):
    try:
      currentYear = datetime.now().year
      lastYear = currentYear - 1
      ret = self.getDividendForYear(lastYear) / self.getCurrentPrice()
    except NocurrentPrice as e:
      raise e
    except Exception as e:
      print(f"An error occured {e}")
      #raise e
      ret = 0
    return ret

  def __str__(self):
      percentString = "{:.3%}".format(self.dividPerShare)
      return "Name:{0}\tstockCode:{1}".format(
              self.stockName, self.stockCode)

  def __getattr__(self, name):
    methodMap = {'currentPrice' : self.getCurrentPrice,
                 'lastDividend' : self.getDividendLast,
                 #'dividPerShare' : self.getDividPerShare,
                 'dividPerShare' : self.getRateOfDividend,
                 'lastDividendDate': self.getDividendLastDate,
                 'marketCap': self.getMarketCap,
                 'lastTotalRevenue' : self.getLastTotalRevenue
                }
    try:
        self.__dict__[name] = methodMap[name]()
        return self.__dict__[name]
    except Exception as e:
        if name == 'lastDividend':
          self.__dict__[name] = 0
        raise e


if __name__ == '__main__':
  stock = StockInfo(600362, '江西铜业', 'Shanghai Stock Exchange')
  print(stock.stockSymbol)
  print(stock.stockInfo.info['currentPrice'])
  print(stock.currentPrice)
  #print(stock.lastDividend /stock.currentPrice)
