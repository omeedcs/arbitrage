from flask import Flask, render_template, request
import value_investing
import balanceSheetAnalysis
import yfinance as yf

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():

   # get user inputs
   if request.method == 'POST':
      usr_symbol = request.form.get("symbol")
      usr_decision = request.form.get("decision")
      usr_bs_symbol = request.form.get("bs_symbol")
      
      calculations = []
      # pb_output = value_investing.pb_ratio(usr_symbol)
      pb_output = 0
      flr_analysis = 0 
      lr_analysis = 0
      sr_analysis = 0
      if (usr_symbol != None):
         pb_output = value_investing.pb_ratio(usr_symbol)
      elif (usr_bs_symbol != None):
         ticker = yf.Ticker(usr_bs_symbol )
         flr_analysis = balanceSheetAnalysis.analyzeFinancialLeverageRatio(ticker)
         lr_analysis = balanceSheetAnalysis.analyzeLiquidityRatios(ticker)
         sr_analysis = balanceSheetAnalysis.analyzeSolvencyRatios(ticker)
         data = usr_bs_symbol
      else:
         data = "None"
      return render_template("index.html", pb = pb_output, flr = flr_analysis, lr = lr_analysis, sr = sr_analysis)
      
   # print(usr_symbol)
   # print(usr_decision)

   # print(type(usr_symbol))
   # print(type(usr_symbol) == None)

   # calculating ratios and values
   # if usr_symbol.filename != '': 
   # pb_ratio = value_investing.pb_ratio(usr_symbol)

   return render_template("index.html")