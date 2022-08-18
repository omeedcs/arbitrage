from trading_functions import get_user_ticker, get_user_cash, get_current_closing_price
from value_investing import run

def trade_simulator(symbol):
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("Hello, welcome to Zachary and Omeed's trading bot.") 
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

    ticker = get_user_ticker(symbol)


    # malleable, be smart with this value.
    number_of_desired_trades = 100

    # establish a simple desired strategy here.
    
    result = build_trading_strategy(ticker) 
    if (result == "N/A"):
        print("Trading strategy build failed.")
        return
    if (result == "VALUE_INVESTING_DONE"):
        return
    
    print("Now implementing strategy and simulating trade, please wait...")
    print()
    day1_ticker_price = get_current_closing_price(ticker, str(1) + "d")
    day30_ticker_price = get_current_closing_price(ticker, str(30) + "d")    #  simulate the desired strategy
    share_1 = 0
    share_2 = 0
    for i in range(number_of_desired_trades):
        if (cash_one >= 1):
            print("Share # bought for today:", i)
            share_1 += 1
            cash_one -= day1_ticker_price
    
    for i in range(number_of_desired_trades):
        if (cash_two >= 1):
            print("Share # bought for 30 days ago:", i)
            share_2 += 1
            cash_two -= day30_ticker_price
    print("Number of shares bought today:", share_1)
    print("Number of shares bought 30 days ago", share_2)
# utilizing a range of available, hand implemented trading strategies in 
# our alternative script, we will combine these to create an optimal 
# mathematical strategy to simulate.
def build_trading_strategy(ticker):
    print("Making API call to Yahoo Finance...")
    try:
        recent_closing_price = get_current_closing_price(ticker, "1d")
        print("Found. Recent closing price of ticker is:", recent_closing_price)
    except:
        print("Error. Could not find recent closing price. Error with YF.")
    
    print()
    print("What trading strategy would you like to simulate from the options below...")
    print("1 - Recent Price Strategy")
    print("2 - Value Investing Strategy" ) 
    print("3 - TBD Strategy")
    selected_trading_strategy = input("Enter: ")
    print()
    prices = []
    if (float(selected_trading_strategy) == 1):
        # for i in range(30):
        #     cur_ticker_price = get_current_closing_price(ticker, str(i) + "d")
        #     prices.append(cur_ticker_price)
        day1_ticker_price = get_current_closing_price(ticker, str(1) + "d")
        day30_ticker_price = get_current_closing_price(ticker, str(30) + "d")
        difference = day30_ticker_price - day1_ticker_price
        return difference
    elif (float(selected_trading_strategy) == 2):
        run()
        return "VALUE_INVESTING_DONE"
    else:
        return "N/A"