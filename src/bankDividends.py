#!/bin/python3
from bankStock import BankStockIndex

if __name__ == '__main__':
  bankUrl = "https://csi-web-dev.oss-cn-shanghai-finance-1-pub.aliyuncs.com/static/html/csindex/public/uploads/file/autofile/closeweight/399986closeweight.xls"
  bank = BankStockIndex(bankUrl)
  bank.sortOnDivid()
  print(bank)
