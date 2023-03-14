# SURFTRACK
#### Video Demo:  https://youtu.be/3oegp_MaSag
#### Description:

Introduction:
Surftrack is a web based application to enable surfers to record in detail their surf sessions, allowing for a better appreciation of the factors that impact and effect surf conditions at local surf spots. This in turn will allow for a greater understanding of future forecasts provided by Surfline.com, resulting in optimal time and spot choice for the best waves.

Surfline.com is a global surf forecasting website which provides accurate surf forecasting data for hundreds of surf spots around the globe.  Surftrack accesses this data via an API and provides recording, presentation and filtering features to enable a surfer to have a look at current forecasts and compare them to previous records of actual surf sessions.

Files:
app.py

Primary python file for the application which sets up the flask framework, data base and manages all application routes and data base execution. In addition to this it also contains additonal logic to manage the information inputted to the database to enhance the accuracy and useability of the data the user sees.

Further information on the routes and functionality are included in the web app features section below:


Web app features:
'/add_surf_spot.html'
The Add surf spot page allows the user to input a surf spot name, direction and surfline forecast spotID. The name is unrelated to the surfline ID allowing a user to implement several surfspots from the same forecast data. (surfspots may face different directions or be more sheltered so need a seperate record) The direction allows for the calculation of the wind direction. (On-shore, Cross-shore or Offshore). The surfline.com spot ID is to be copied from the surfline.com url: For example: The Pipeline in Hawaii (USA) has the following surfline.com URL https://www.surfline.com/surf-report/pipeline/5842041f4e65fad6a7708890where 5842041f4e65fad6a7708890 is the spotId of the spot.  For further details please refer to the helpers.py section below.

All inputs are validated, errors managed and the spot added to the surf_spots table in the surftrack.db database using sqlite3.

'/' (record surf session)
Record surf session allows the user to select a location from the list of surf spots added with the above form and presented in '/' using jinga., select a surf rating from 1 to 5 with 5 being the highest and then add a description. This is key to the functionality and benefit of the app as it allows the user to compare this real experience data against the forecast data that is retrieved from Surfline.com via the forecast_lookup function in helpers.py for the surf session. This will allow the user to make valid future comparisons and assessments. 

All inputs are validated, errors managed and the spot added to the sessions table in the surftrack.db using sqlite3.

'/history.html'
history.html presents the data from from the recorded surf sessions in a simple to scan table, created using bootstrap5 cards, headers and tables. The data is extracted from the database and inputed to the html file using a jinja loop. 

Javascript enhances the usability of the table with a filter button allowing for  additional filtering functionality of the table through any of the column headers. For example a surfer could filter by a specific spot, tide and wind direction to see a previous record. Further to this the table is formated in browser using Javascript to add a Red Amber Green reference system to both the previous surf rating and the wind column. These are the two key data points which are useful to be able to understand initially before further understanding of the presented data.


helpers.py
Contains the forecast look up function which utilises the pysurfline 0.0.3 python package (https://pypi.org/project/pysurfline/) to request forecast data for the current day at one hour intervals for the spotID provided. Surfline provides the full 24 hours of data via the API as a minimum. The lookup_forecast function then processes this data, extracting the key information for the current hour, processes the data to find key items such as wave height, maximum swell and wind directing and then exports these key value pairs in a dictionary. If the API fails to return forecast data the function returns None.

The file also contains an apology function to present the user with a html file to handle errors.

surftrack.db
Two tables surf_spots and sessions.

Formating
The webpage is formatted primarily using bootstrap forms and containers.
A layout.html file is used to reduce html repetition with all previously mentioned files extending it. 
Includes head files, bootstrap5 navbar and background image containers.
styles.css
General css style file containing the background images and style features.

Note: the surftrack web app does not currently have functionality for multiple users.



