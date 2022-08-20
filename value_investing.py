import yfinance as yf
# from matplotlib import pyplot as plt

def get_ticker(symbol):
    ticker = yf.Ticker(symbol)
    return ticker

# create a time series graph for stocks
# def create_time_series(symbol):
#     ticker = get_ticker(symbol)
#     month_data = ticker.history(period="30d")

#     for key in month_data.keys():
#         data = month_data[key]
#         plt.plot(data)
#         plt.title(key)
#         plt.xlabel("Days")
#         plt.ylabel(key)
#         plt.figure()
#     return "Done"

# calculate book value of a stock
def calc_book_value(symbol):
    # total assets - total liabilities
    ticker = get_ticker(symbol)
    balancesheet = ticker.quarterly_balancesheet
    return balancesheet.loc["Total Assets"][0] - balancesheet.loc["Total Liab"][0]

# calculate market value
def calc_market_value(symbol):
    ticker = get_ticker(symbol)
    info = ticker.info
    curr_stock_price = info["currentPrice"]
    num_shares = info["sharesOutstanding"]
    return curr_stock_price * num_shares

# calculate p/b ratio
def pb_ratio(symbol):
    pb = calc_market_value(symbol) / calc_book_value(symbol)
    return (f"The P/B ratio for {symbol} is {pb}") 