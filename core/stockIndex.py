#!/bin/python3

from stockInfo import StockInfo
from io import BytesIO
import requests

class StockIndex:
  def __init__(self, url):
    self.stockIndex = []
    self.stockToWeight = {}
    self.dividends = {}
    self.roe = {}
    exMap = {'Shanghai Stock Exchange':'SS',
             'Shenzhen Stock Exchange':'SZ'}
    response = requests.get(url)

    if response.status_code == 200:
      data = response.content
      stocks = []

      import pandas as pd
      bytesIo = BytesIO(data)
      df = pd.read_excel(bytesIo)

      for _, row in df.iterrows():
        stockCode = row['成份券代码Constituent Code']
        stockName = row['成份券名称Constituent Name']
        stockEx = row['交易所英文名称Exchange(Eng)']
        stockWeight = row['权重(%)weight']
        s = StockInfo(stockCode, stockName, stockEx)
        #print(stockCode, stockName, stockEx, stockWeight)
        self.stockIndex.append(s)
        self.stockToWeight[s] = stockWeight / 100;
        self.dividends[s] = s.getDividendLast() / s.currentPrice
        self.roe[s] = s.getROE()

  def __str__(self):
    ps = ""
    for t in self.stockIndex:
      ps += str(t) + '\t' + '{:.1%}\n'.format(self.stockToWeight[t])
    return ps

  def sortOnDivid(self):
    self.stockIndex = sorted(self.stockIndex, key=lambda x:x.dividPerShare, reverse=True)

  def getIndexPE(self):
    pe = 0.0
    for stock, weight in self.stockToWeight.items():
      try:
        pe += stock.stockInfo.info['trailingPE'] * weight
      except Exception as e:
        print(stock.stockName)
        continue
    return pe

      

if __name__ == '__main__':
    url = "https://csi-web-dev.oss-cn-shanghai-finance-1-pub.aliyuncs.com/static/html/csindex/public/uploads/file/autofile/cons/399986cons.xls"
    url300 = "https://csi-web-dev.oss-cn-shanghai-finance-1-pub.aliyuncs.com/static/html/csindex/public/uploads/file/autofile/cons/000300cons.xls"
    url300weight = "https://csi-web-dev.oss-cn-shanghai-finance-1-pub.aliyuncs.com/static/html/csindex/public/uploads/file/autofile/closeweight/000300closeweight.xls"
    #si = StockIndex(url)
    #si.sortOnDivid()
    sci300 = StockIndex(url300weight)
    #print(sci300)
    print(sci300.getIndexPE())
    #print(si)

