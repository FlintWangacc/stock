#!/bin/python3
import stockenv
from bankStock import BankStockIndex

if __name__ == '__main__':
  bankUrl = "https://csi-web-dev.oss-cn-shanghai-finance-1-pub.aliyuncs.com/static/html/csindex/public/uploads/file/autofile/closeweight/931354closeweight.xls"
  #bankUrl = "/home/hmsjwzb/Downloads/399986closeweight_2.xls"
  bank = BankStockIndex(bankUrl)
  bank.sortOnDivid()
  print(bank)
