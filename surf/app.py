#main code for surftrack web app

#import required packages

from cs50 import SQL
from flask import Flask, redirect, render_template, request
from datetime import datetime
from helpers import lookup_forecast

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


@app.route("/add_surf_spot", methods=['GET', 'POST'])
def add_surf_spot():
    # access route via GET
    if request.method == 'GET':
        return render_template("add_surf_spot.html")
    #access route via POST
    else:
        #get spot values from user form
        nickname = request.form.get('spot_nickname')
        surfline_spot_id = request.form.get(surfline_spot_reference)

        #remember user input



    









    