#!/bin/python3
from stockIndex import StockIndex

if __name__ == '__main__':
  bankUrl = "https://csi-web-dev.oss-cn-shanghai-finance-1-pub.aliyuncs.com/static/html/csindex/public/uploads/file/autofile/closeweight/399986closeweight.xls"
  bank = StockIndex(bankUrl)
  bank.sortOnDivid()
  print(bank)
