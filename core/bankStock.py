#!/bin/python3

from stockIndex import StockIndex

class BankStockIndex(StockIndex):
  def __init__(self, url):
    super().__init__(url)

  def __str__(self):
    ps = ""
    for t in self.stockIndex:
      try:
        ps += str(t) + '\t' + '{:.2%}\t'.format(self.stockToWeight[t])
        ps += '{:.2%}\t'.format(self.dividends[t])
        ps += '{:.2%}\n'.format(self.roe[t])
      except Exception as e:
        print(f"An error occurred {e}")
    return ps
