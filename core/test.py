import yfinance as yf

# 定义股票代码
ticker = '002304.SZ'  # 洋河股份的股票代码

# 获取公司的财务数据
stock = yf.Ticker(ticker)

# 获取财务报表和资产负债表
financials = stock.financials
balance_sheet = stock.balance_sheet

# 打印可用的财务数据以检查关键字
print("财务报表:")
print(financials)

print("\n资产负债表:")
print(balance_sheet)

# 提取净利润和股东权益
try:
    net_income = financials.loc['Net Income Common Stockholders'].iloc[0]  # 根据实际关键字调整
    shareholder_equity = balance_sheet.loc['Stockholders Equity'].iloc[0]  # 根据实际关键字调整

    # 计算 ROE
    roe = net_income / shareholder_equity

    print(f"洋河股份的净资产收益率（ROE）: {roe:.2%}")
except KeyError as e:
    print(f"KeyError: {e}. 请检查财务报表中的可用关键字。")

