import balance_sheet_metrics

def analyzeLiquidityRatios(ticker):
    QUICK_RATIO_THRESHOLD = 1
    CURRENT_RATIO_THRESHOLD = 1
    ERROR = 0.05 # (TODO) - intuition based on the balance sheet

    quickRatioFloat = balance_sheet_metrics.quick_ratio(ticker)
    currentRatioFloat = balance_sheet_metrics.currentRatio(ticker)
    # currently in production (TODO)
    # daysSalesOutstandingFloat = balance_sheet_metrics.daysSalesOutstanding(ticker) 
    if (quickRatioFloat >= QUICK_RATIO_THRESHOLD) and (currentRatioFloat >= CURRENT_RATIO_THRESHOLD):
        analysis_str = "Good"
    elif (quickRatioFloat >= (QUICK_RATIO_THRESHOLD * (1 - ERROR))) and (currentRatioFloat >= (CURRENT_RATIO_THRESHOLD * (1 - ERROR))):
        analysis_str =  "Depends"
    else:
        analysis_str = "Poor"
    return f"The Liquidity Ratios are: {analysis_str}"

def analyzeSolvencyRatios(ticker):
    DEBT_EQUITY_RATIO_THRESHOLD = 2.5
    INTEREST_COVERAGE_RATIO_THRESHOLD = 4.5
    SOLVENCY_RATIO_THRESHOLD = 1
    ERROR = 0.05 # TODO - using intuition rather than a source

    debtEquityRatioFloat = balance_sheet_metrics.debt_equity_ratio(ticker)
    interestCoverageRatioFloat = balance_sheet_metrics.interest_coverage_ratio(ticker)
    solvencyRatioFloat = balance_sheet_metrics.solvency_ratio(ticker)

    if (debtEquityRatioFloat >= DEBT_EQUITY_RATIO_THRESHOLD) and (interestCoverageRatioFloat >= INTEREST_COVERAGE_RATIO_THRESHOLD) and (solvencyRatioFloat >= SOLVENCY_RATIO_THRESHOLD):
        analysis_str = "Good"
    elif (debtEquityRatioFloat >= (DEBT_EQUITY_RATIO_THRESHOLD * (1 - ERROR))) and (interestCoverageRatioFloat >= (INTEREST_COVERAGE_RATIO_THRESHOLD * (1 - ERROR))) and (solvencyRatioFloat >= (SOLVENCY_RATIO_THRESHOLD * (1 - ERROR))):
        analysis_str = "Depends"
    else:
        analysis_str = "Poor"
    return f"The Solvency Ratios are: {analysis_str}"

def analyzeFinancialLeverageRatio(ticker):
    DEBT_CAPITAL_RATIO_THRESHOLD = 0.6 # (TODO) - function in progress
    DEBT_ASSET_RATIO_THRESHOLD = 1 # source: https://www.investopedia.com/terms/d/debtratio.asp#:~:text=Generally%20speaking%2C%20a%20debt%2Dto,to%2Dequity%20ratios%20than%20others.
    FINANCIAL_LEVERAGE_RATIO = 2
    ERROR = 0.5 # using intuition rather than a source

    # debtCapitalRatioFloat = balance_sheet_metrics.debt_capital_ratio(ticker)
    debtAssetsRatioFloat = balance_sheet_metrics.debt_asset_ratio(ticker)
    financialLeverageRatioFloat = balance_sheet_metrics.financialLeverageRatio(ticker)

    if (debtAssetsRatioFloat <= DEBT_ASSET_RATIO_THRESHOLD) and (financialLeverageRatioFloat <= FINANCIAL_LEVERAGE_RATIO):
        analysis_str = "Good"
    else: 
        analysis_str = "Bad" # TODO - need to add a depends block
    return f"The Financial Leverage Ratios are: {analysis_str}"