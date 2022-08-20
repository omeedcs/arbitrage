from flask import Flask, render_template, request
import value_investing

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():

   # get user inputs
   if request.method == 'POST':
      usr_symbol = request.form.get("symbol")
      usr_decision = request.form.get("decision")
      
      calculations = []
      pb_output = value_investing.pb_ratio(usr_symbol)
      
      return render_template("form.html", dataToRender=pb_output)

   # print(usr_symbol)
   # print(usr_decision)

   # print(type(usr_symbol))
   # print(type(usr_symbol) == None)

   # calculating ratios and values
   # if usr_symbol.filename != '': 
   # pb_ratio = value_investing.pb_ratio(usr_symbol)

   return render_template("form.html")