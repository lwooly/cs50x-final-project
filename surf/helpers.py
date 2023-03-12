from pysurfline import SpotForecast
from datetime import  datetime

# params - spot id to be updated by user input

#Form to set up a new spot:
#Spot nick name
#Data source: surfline spotID

#def main():
   # functiontest = lookup_forecast("584204204e65fad6a77090d2")
    #print(functiontest)


# function to return key spot data for the current time 
def lookup_forecast(surfline_spot_id):

    # use pysurfline package to request spot data from the surfline.com API: https://giocaizzi.github.io/pysurfline/index.html
    # https://pypi.org/project/pysurfline/#description
    # note that this application is to be used for personal use only.  

    #define surfline spot parameters
    spot_params={
        "spotId":surfline_spot_id,
        "days":1,
        "intervalHours":1,
        }

    #call API to get spot data
    spot=SpotForecast(spot_params,verbose=False)
    if spot == None:
        return None
    
    for item in spot.api_log:
        if '400' in str(item):
            return None 


    # get key data at the current time. - further work could be to let user select time.
    current_timestamp = datetime.now().timestamp()

    #extract wave data from class
    wave_data = spot.wave
    # declare variable to count iterations - for use finding current data from other lists
    # check time stamp in wave data
    for hour in wave_data:
        # note data is exported with users local time. data is from 00.00 to 23.00 at the local timezone of the surf spot
        timestamp = hour['timestamp']
        if current_timestamp >= timestamp and current_timestamp < timestamp + 60 * 60:
            #time is within the current hour
            current_wave_data = hour
            

    #extract wind data from class
    wind_data = spot.wind
    # declare variable to count iterations - for use finding current data from other lists
    # check time stamp in wind data
    for hour in wind_data:
        # note data is exported with users local time. data is from 00.00 to 23.00 at the local timezone of the surf spot
        timestamp = hour['timestamp']
        if current_timestamp >= timestamp and current_timestamp < timestamp + 60 * 60:
            #time is within the current hour
            current_wind_data = hour
            

    #extract tide data from class
    tide_data = spot.tides
    # declare variable to count iterations - for use finding current data from other lists
    # check time stamp in wind data
    for hour in tide_data:
        # note data is exported with users local time. data is from 00.00 to 23.00 at the local timezone of the surf spot
        timestamp = hour['timestamp']
        if current_timestamp >= timestamp and current_timestamp < timestamp + 60 * 60:
            #time is within the current hour
            current_tide_data = hour
            

    #source units for reference {'temperature': 'C', 'tideHeight': 'M', 'swellHeight': 'FT', 'waveHeight': 'HI', 'windSpeed': 'KTS', 'pressure': 'MB'}

    #refine key data, change units and return dictionary of pairs for use in SQL 
    # some useful data omitted # for this version
    spot_data = {}

    #wave heights
    spot_data['surf_min'] = current_wave_data['surf_min']
    spot_data['surf_max'] = current_wave_data['surf_max']
    spot_data['surf_humanRelation'] = current_wave_data['surf_humanRelation']

    #swells
    primary_swell = current_wave_data['swells']

    #TODO - key primary swell index may not always be 1 - sort swells for max before printing
    
    spot_data['primary_swell_height'] = primary_swell[1]['height']
    spot_data['primary_swell_period'] = primary_swell[1]['period']
    spot_data['primary_swell_direction'] = primary_swell[1]['direction']

    #wind

    #convert to kph from knots
    spot_data['wind_speed'] = float(current_wind_data['speed']) * 1.852
    spot_data['wind_direction'] = current_wind_data['direction']
    spot_data['wind_direction_type'] = current_wind_data['directionType']
    spot_data['wind_gust'] = current_wind_data['gust']
    
    #tides 
    spot_data['tide_height'] = current_tide_data['height']

    return spot_data


#main()


    
    





    





