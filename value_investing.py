import yfinance as yf
from matplotlib import pyplot as plt

def get_ticker(symbol):
    ticker = yf.Ticker(symbol)
    return ticker

# create a time series graph for stocks
def create_time_series(symbol):
    ticker = get_ticker(symbol)
    month_data = ticker.history(period="30d")

    for key in month_data.keys():
        data = month_data[key]
        plt.plot(data)
        plt.title(key)
        plt.xlabel("Days")
        plt.ylabel(key)
        plt.figure()
    return "Done"

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
    print(f"The P/B ratio for {symbol} is {pb}")
    return pb

def get_list_of_symbols():
    pass

def find_under_valued_stocks(symbols):
    pb_thresh = 6 # should be 3 (source: https://www.investopedia.com/ask/answers/010915/what-considered-good-price-book-ratio.asp#:~:text=The%20price%2Dto%2Dbook%20(,P%2FB%20value%20under%203.0.)
    uv_stocks = []
    for symbol in symbols:
        if pb_ratio(symbol) <= pb_thresh:
            uv_stocks.append(symbol)
    return uv_stocks

def run():
    print("Value Investing Algorithm")
    decision = input("Enter 1 for custom tickers, or enter 2 for our database: ")
    if (float(decision) == 1):
        symbols = []
        while (True):
            cur_symbol = input("Enter a ticker: ")
            symbols.append(cur_symbol)
            check_break = input("Input Y for continue, N for calculation: ")
            if (check_break == "N"):
                break
        print("Now loading P/B ratios..")
        print(find_under_valued_stocks(symbols))
    elif(float(decision) == 2): 
        # pseudo database.
        symbols = ["A", "AA", "AAC", "AACG"]
        print("Now loading P/B ratios..")
        print(find_under_valued_stocks(symbols))
