import datetime
import yfinance as yf

# using a user input, this will return a ticker object from the yahoo
# finance API call. Further use of functions is neccesary to utilize 
# the auto conversion of dataframes.
def get_user_ticker(symbol):
    # ticker_input = input("Please input a stock ticker: ")
    ticker = yf.Ticker(symbol)
    return ticker

def get_user_cash():
    cash_input = input("Please input desired investment amount (in USD): ")
    cash = float(cash_input) 
    return cash

def get_current_closing_price(ticker, cur_period):
    current_closing_price = ticker.history(period = cur_period)['Close'][0]
    return current_closing_price

