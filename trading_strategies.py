import datetime
import yfinance as yf
import numpy as np

def get_ticker(symbol):
    # find keys we'd like to work with...
    # keys = ticker_information.keys()
    # for i in keys: 
    #     print(i)
    return symbol

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


def get_current_price(symbol, cur_period):
    ticker = get_ticker(symbol)
    usc = ticker.history(period = cur_period)['Close'][0]


def black_scholes_calc(S, K, T, r, sigma, option = 'call'): 
	#S: Current Stock Price
    #K: Strike price
    #T: Time to maturity in Years
    #r: Risk Free interest rate
    #sigma: Volatility of underlying asset
    
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = (np.log(S / K) + (r - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    
    if option == 'call':
        result = (S * si.norm.cdf(d1, 0.0, 1.0) - K * np.exp(-r * T) * si.norm.cdf(d2, 0.0, 1.0))
    if option == 'put':
        result = (K * np.exp(-r * T) * si.norm.cdf(-d2, 0.0, 1.0) - S * si.norm.cdf(-d1, 0.0, 1.0))
        
    return result

'''
Sample Run
'''
s = yf.Ticker('AAPL')
opt = s.option_chain('2022-08-19')
call= opt.calls 
# last price 
S = s.history(period = "max")['Close'].iloc[-1]
T = (datetime.date(2020,11,20) - datetime.date(2020,7,24)).days / 365.0
print(S, T)
for i in range(len(call)):
	v = call.iloc[i]['impliedVolatility']
	r = 0.17900 
	K = call.iloc[i]['strike']
	print(K)
	print ('Price: %.4f' % black_scholes_calc(S, K, T, 0.014, v))

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



