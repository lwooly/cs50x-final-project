#main code for surftrack web app

#import required packages

from cs50 import SQL
from flask import Flask, redirect, render_template, request
from datetime import datetime
from helpers import lookup_forecast, apology

app = Flask(__name__)


# set debug mode to True
app.debug = True



# configure SQL database to store data
db = SQL("sqlite:///surftrack.db")

ratings = [1, 2, 3, 4, 5]

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

#initial version - assume only one user - add login feature if time capacity

# define index route
@app.route("/", methods=['GET','POST'])
def index():
    # user route via GET - present form to record session
    if request.method == 'GET':

        #get saved spots
        locations = []
        location_data = db.execute("SELECT nickname FROM surf_spots;")
        for location in location_data:
            locations.append(location['nickname'])

        return render_template("index.html",locations=locations, ratings=ratings)

    # user route via POST
    else:
        #get user form input
        location = request.form.get('location').upper()
        user_rating = request.form.get('user_rating')
        user_text = request.form.get('user_text')

        #validate user input
        if not user_rating:
            return apology("select valid rating")
        
        if not location:
            return apology('add valid location')
        
        #could also check if location in db. should be captured by the drop down.

        if not user_text:
            user_text = ''

        #query db surf_spots for surfline reference
        surfline_spot_ref = db.execute("SELECT surfline_spot_id FROM surf_spots WHERE nickname = ?", location)

        # call lookup function
        session_data = lookup_forecast(surfline_spot_ref[0]['surfline_spot_id'])

        #query db surf_spots for surf_spots(spot_id)
        session_spot_id = db.execute("SELECT spot_id FROM surf_spots WHERE nickname = ?", location)
        session_spot_id = session_spot_id[0]['spot_id']
        #get current time
        session_time = datetime.now()

        #remember surf session data in db
        
        db.execute("""INSERT INTO sessions (
                    datetime,
                    spot_id,
                    surf_max,
                    surf_min,
                    surf_humanRelation,
                    primary_swell_height,
                    primary_swell_period,
                    primary_swell_direction,
                    wind_speed,
                    wind_direction,
                    wind_direction_type,
                    wind_gust,
                    tide_height,
                    user_rating,
                    user_text
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);""",
                session_time,
                session_spot_id,
                session_data['surf_max'],
                session_data['surf_min'],
                session_data['surf_humanRelation'],
                session_data['primary_swell_height'],
                session_data['primary_swell_period'],
                session_data['primary_swell_direction'],
                session_data['wind_speed'],
                session_data['wind_direction'],
                session_data['wind_direction_type'],
                session_data['wind_gust'],
                session_data['tide_height'],
                user_rating,
                user_text)
        
        return redirect('/history')

    
@app.route("/add_surf_spot", methods=['GET', 'POST'])
def add_surf_spot():
    # access route via GET
    if request.method == 'GET':
        return render_template("add_surf_spot.html")
    #access route via POST
    else:
        #get spot values from user form
        nickname = request.form.get('spot_nickname').upper()
        surfline_spot_id = request.form.get('surfline_spot_reference')
        spot_direction = request.form.get('direction_spot')

        #validate input
        if not nickname:
            return apology('Enter a spot name')
        
        # check nickname isn't in db already
        #get saved spots
        location_data = db.execute("SELECT nickname FROM surf_spots;")
        for location in location_data:
            if nickname == location['nickname']:
                return apology('Nickname already assigned')
        

        # call lookup_forecast and check valid.
        if lookup_forecast(surfline_spot_id) == None:
            return apology('Surfline spotId not valid')
        
        # validate direction input
        if not spot_direction:
            return apology('Enter direction as a positive integer')
        
        if spot_direction.isnumeric()==False:
            return apology('Enter direction as a positive integer')

        if int(spot_direction) < 0 or int(spot_direction) > 359:
            return apology('Enter direction as a positive integer')

        #calculate wind direction type for specific spot

        #remember user input
        db.execute("INSERT INTO surf_spots (nickname, surfline_spot_id, direction) VALUES (?, ?,?)", nickname, surfline_spot_id, spot_direction)
        
        return redirect("/")
    
@app.route("/history")
def history():
    '''user to view saved data'''
    #get data from db for all records
    record_data = db.execute("SELECT * FROM sessions JOIN surf_spots ON sessions.spot_id = surf_spots.spot_id ORDER BY session_id DESC;")

    return render_template("history.html", record_data=record_data)





    









    