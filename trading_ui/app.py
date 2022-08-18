#Package import
import re
from turtle import up
from flask import Flask, render_template, send_file, make_response, url_for, Response, redirect, request 
from trading import trade_simulator

import logging

#initialise app
app = Flask(__name__)

#decorator for homepage 
@app.route('/')
def index():
    return render_template('index.html',
                           PageTitle = "Landing page")

#These functions will run when POST method is used.
@app.route('/', methods = ["POST"] )
def plot_png():
    #gathering file from form
    inputted_symbol = request.values['txt_symbol']
    
    trade_simulator(inputted_symbol)

    #making sure its not empty
    if uploaded_file.filename != '':
        #reading the file
        text = uploaded_file.read()
        #converting to a string.
        text = str(text)
        #You can then run any scripts you want on our file. 
        #Here we used a text file so any sort of text analysis could be undertaken
        #You could even run machine learning on a csv dataset.
        function_that_does_something_1(text)
        function_that_does_something_2(text)
        function_that_does_something_3(text)

        #Here I want to visualise my output for my users - so I return a plot.
        #Plotting
        fig = plot_something()
        
        output = io.BytesIO()
        FigureCanvas(fig).print_png(output)
        return Response(output.getvalue(), mimetype = 'image/png')
        #The created image will be opened on a new page
    
    else:
        return render_template('index.html',
                        PageTitle = "Landing page")
      #This just reloads the page if no file is selected and the user tries to POST. 


if __name__ == '__main__':
    app.run(debug = True)