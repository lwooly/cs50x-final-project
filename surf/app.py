#main code for surftrack web app

#import required packages

from cs50 import SQL
from flask import Flask, redirect, render_template, request
from datetime import datetime
from helpers.py import lookup_forecast

app = Flask(__name__)


# configure SQL database to store data
#db = SQL("sqlite:///surf_track.db")

#initial version - assume only one user - add login feature if time capacity

# define index route
@app.route("/", methods=['GET','POST'])
def index():
    # user route via GET - present form to choose surf spot
    if request.method == 'GET':
    # present form for record session
    # spot drop down from previous recorded
    # user comments
    # user rating 1 -5
        return render_template("index.html")

    # user route via POST

    #add data to sql using lookup etc.










    