# import numpy as np
import datetime
# import scipy.stats as si
# import scipy.stats as si
import yfinance as yf

def get_ticker():
    user_input = input("Type in a stock Ticker: ")
    ticker = yf.Ticker(user_input)
    # find keys we'd like to work with...
    # keys = ticker_information.keys()
    # for i in keys: 
    #     print(i)
    return ticker

def cpi_inflation_calculator():
    # import cpi
    # first, let's refresh and update the consumer price index.
    cpi.refresh()

    # next, let's simualte the change of dollar value within the span of 1 recent year.
    # library is outdated.
    simulated_dollar = 100
    simulated_inflated_value = cpi.inflate(100, 2020, to = 2021)
    inflation = simulated_dollar / simulated_inflated_value # now we have the inflation percentage of 100 dollars.
    print(inflation)

# Arbitrage Pricing Theory is a model for asset pricing which relates various 
# macro-economic risk variables to the pricing of financial assets. 
# This was proposed by economist Stephen Ross in 1976.
# Source: https://corporatefinanceinstitute.com/resources/knowledge/finance/arbitrage-pricing-theory-apt/
def arbitrage_pricing_theory():
    
    # obtain the current ticker
    cur_ticker = get_ticker()

    print("What is the duration of your investment?")
    user_input = input("Please enter either 1 year, 2 year, 5 year, or 10 year.")
    investment_duration = float(user_input)
    # ticker_info = cur_ticker.info
    # print(ticker_info)

    # current inflation rate in 2022, subject to change:
    # it is typicaLly marked as a star.
    inflation = 9.73
    yield_of_treasury = 0
    # we need to match this to the investment duration.
    if (investment_duration == 1):
        yield_of_treasury = 3.24
    elif (investment_duration == 2):
        yield_of_treasury = 3.29
    elif (investment_duration == 5):
        yield_of_treasury = 3.04
    elif (investment_duration == 10):
        yield_of_treasury = 2.89
    
    # riskless rate of return
    # to calculate: we need to subtract the inflation rate from the yield of the
    #  Treasury bond matching the investment duration.
    rror = yield_of_treasury - inflation
    beta = cur_ticker.info['beta']
    print(cur_ticker.info['returnOnAssets'])
    expected_return = 6.5
    dija = expected_return - rror
    rp = dija / beta
    final_expected_return = rror + rp
    print(final_expected_return)
    return final_expected_return

def call_option_intrinsic_value(symbol):
    ticker = get_ticker(symbol)
    options = ticker.option_chain()
    calls = options.calls 
    usc = ticker.history(period="1d")['Close'][0]
    cs = calls.strike
    return usc - cs # call option intrinsic value

def put_option_intrinsic_value(symbol):
    ticker = get_ticker(symbol)
    options = ticker.option_chain()
    puts = options.puts
    usc = ticker.history(period="1d")['Close'][0]
    ps = puts.strike
    return ps - usc # put option intrinsic value


    


def voltality():
    # 554
    pass

def black_scholes():
    pass

def risk_arbitrage():
    pass

def retail_arbitrage():
    pass

def stat_arb():
    pass



print(arbitrage_pricing_theory())