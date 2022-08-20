# used data querying, theory and mathematics to calculate functions for the metrics
# https://attachments.convertkitcdnn2.com/424264/27899a4d-b26f-49c9-8456-9eb9a586af78/V2%20BS%20KPIs%20Free%20Download(2).pdf
import yfinance as yf

# Liquidity Ratios
def quick_ratio(ticker):
    current_assets = ticker.balancesheet.loc["Total Current Assets"][0]
    inventory = ticker.balancesheet.loc["Total Current Assets"][0]
    current_liabilities = ticker.balancesheet.loc["Total Current Liabilities"][0]
    return (current_assets - inventory) / current_liabilities

def currentRatio(ticker):
    current_assets = ticker.balancesheet.loc["Total Current Assets"][0]
    current_liabilities = ticker.balancesheet.loc["Total Current Liabilities"][0]
    return current_assets / current_liabilities

def daysSalesOutstanding(ticker):
    # cant find accounts receivable in balancesheet dataframe; closest thing is "Net Receivables"
    pass

# Solvency Ratios
def debt_equity_ratio(ticker):
    liabilities = ticker.balancesheet.loc['Total Liab'][0]
    # shareholders' equity is the net amount of a company's total assets and total liabilities,
    equity = ticker.balancesheet.loc['Total Stockholder Equity'][0]
    equity_ratio = liabilities / equity
    return equity_ratio

def interest_coverage_ratio(ticker):
    earnings_before_interest_and_tax = ticker.financials.loc['Ebit'][0]    
    interest_expense = ticker.financials.loc['Interest Expense'][0]
    interest_coverage_ratio = earnings_before_interest_and_tax / interest_expense
    return interest_coverage_ratio

def solvency_ratio(ticker):
    net_income = ticker.financials.loc['Net Income'][0]
    depreciation = ticker.get_cashflow().loc["Depreciation"][0]
    liabilities = ticker.balancesheet.loc['Total Liab'][0]    
    solvency_ratio = (net_income + depreciation) / liabilities
    return solvency_ratio

# financial leverage ratios
def debt_capital_ratio():
    # couldn't find data on yfinance
    pass

# total debts divided by total assets
def debt_asset_ratio(ticker):
    # long term debt is another key term for long term liabilities
    # https://www.bdc.ca/en/articles-tools/entrepreneur-toolkit/templates-business-guides/glossary/long-term-liabilities#:~:text=Long%2Dterm%20liabilities%2C%20also%20called,appear%20along%20with%20current%20liabilities.
    long_term_liabilities = ticker.balancesheet.loc['Long Term Debt'][0]
    current_liabilities = ticker.balancesheet.loc['Total Current Liabilities'][0]

    # what is total debt -  https://efinancemanagement.com/financial-analysis/how-to-calculate-debt-from-balance-sheet
    total_debt = long_term_liabilities + current_liabilities 
    total_assets = ticker.balancesheet.loc['Total Assets'][0]
    debt_asset_ratio = total_debt / total_assets
    return debt_asset_ratio

def financialLeverageRatio(ticker):
    totalAssets = ticker.balancesheet.loc["Total Assets"][0]
    totalEquity = ticker.balancesheet.loc['Total Stockholder Equity'][0]
    return totalAssets - totalEquity