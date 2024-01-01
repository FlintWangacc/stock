#!/bin/python3

from stockIndex import StockIndex

class BankStockIndex(StockIndex):
  def __init__(self, url):
    self.dividends = {}
    super().__init__(url)
    for s in self.stockIndex:
      self.dividends[s] = s.getDividendLast() / s.currentPrice

  def __str__(self):
    ps = ""
    for t in self.stockIndex:
      ps += str(t) + '\t' + '{:.2%}\t'.format(self.stockToWeight[t])
      ps += '{:.2%}\n'.format(self.dividends[t])
    return ps
