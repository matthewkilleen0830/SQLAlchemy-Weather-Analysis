# SQLAlchemy Project: &nbsp;Surfs Up!

![surfs-up.png](Images/surfs-up.png)

Congratulations! &nbsp;You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii! &nbsp;To help with trip planning, we need to do some climate analysis on the area.

## Step 1: &nbsp;Climate Analysis and Exploration

To begin, we used Python and SQLAlchemy to do basic climate analysis and data exploration of our climate database. &nbsp;All of the following analyses were completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.

* Used SQLAlchemy `create_engine` to connect to your sqlite database.

* Used SQLAlchemy `automap_base()` to reflect your tables into classes, and saved a reference to those classes called `Station` and `Measurement`.

* Linked Python to the database by creating an SQLAlchemy session.

### Precipitation Analysis

* Started by finding the most recent date in the data set.

* Using this date, retrieved the last 12 months of precipitation data by querying the 12 preceding months of data.

* Selected only the `date` and `prcp` values.

* Loaded the query results into a Pandas DataFrame and set the index to the date column.

* Sorted the DataFrame values by `date`.

* Plotted the results using the DataFrame `plot` method.

  ![precipitation](Images/precipitation.png)

* Used Pandas to print the summary statistics for the precipitation data.

### Station Analysis

* Designed a query to calculate the total number of stations in the dataset.

* Designed a query to find the most active stations (i.e. which stations have the most rows?).

  * Listed the stations and observation counts in descending order.

  * Which station ID has the highest number of observations?

  * Using the most active station ID, calculated the lowest, highest, and average temperature.

* Designed a query to retrieve the last 12 months of temperature observation data (TOBS).

  * Filtered by the station with the highest number of observations.

  * Queried the last 12 months of temperature observation data for this station.

  * Plotted the results as a histogram with `bins=12`.

    ![station-histogram](Images/station-histogram.png)

- - -

## Step 2: &nbsp;Climate App

Next, we designed a Flask API based on the queries that you have just developed.

* Used Flask to create your routes.

### Routes

* `/`

  * Home page.

  * Listed all routes that are available.

* `/api/v1.0/precipitation`

  * Converted the query results to a dictionary using `date` as the key and `prcp` as the value.

  * Returned the JSON representation of your dictionary.

* `/api/v1.0/stations`

  * Returned a JSON list of stations from the dataset.

* `/api/v1.0/tobs`
  * Queried the dates and temperature observations of the most active station for the last year of data.

  * Returned a JSON list of temperature observations (TOBS) for the previous year.

* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`

  * Returned a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

  * When given the start only, calculated `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.

  * When given the start and the end date, calculated the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.

- - -

## Additional Analyses

### Temperature Analysis I

* Hawaii is reputed to enjoy mild weather all year. &nbsp;Is there a meaningful difference between the temperature in, for example, June and December?

* Used Pandas to perform this portion:

  * Converted the date column format from string to datetime.

  * Set the date column as the DataFrame index.

  * Dropped the date column.

* Identified the average temperature in June at all stations across all available years in the dataset. &nbsp;Did the same for December temperature.

* Used t-test to determine whether the difference in the means, if any, is statistically significant.

### Temperature Analysis II

* We are looking to take a trip from August 1 to August 7 of this year, but are worried that the weather will be less than ideal. &nbsp;Using historical data in the dataset, find out what the temperature has previously looked like.

* Used the `calc_temps` function to calculate the min, avg, and max temperatures for your trip using the matching dates from a previous year (i.e. used "2017-08-01").

* Plotted the min, avg, and max temperature from previous query as a bar chart.

  * Used "Trip Avg Temp" as the title.

  * Used the average temperature as the bar height (y value).

  * Used the peak-to-peak (TMAX-TMIN) value as the y error bar (YERR).

    ![temperature](Images/temperature.png)

### Daily Rainfall Average

* Now that we have an idea of the temperature, let's check to see what the rainfall has been. &nbsp;We don't want to go when it rains the whole time!

* Calculated the rainfall per weather station using the previous year's matching dates.

  * Sorted this in descending order by precipitation amount and list the station, name, latitude, longitude, and elevation.

* Calculated the daily normals. &nbsp;Normals are the averages for the min, avg, and max temperatures. &nbsp;Used a function called `daily_normals` that calculated the daily normals for a specific date. &nbsp;This date string will be in the format `%m-%d`.

  * Set the start and end date of the trip.

  * Used the date to create a range of dates.

  * Stripped off the year and saved a list of strings in the format `%m-%d`.

  * Used the `daily_normals` function to calculate the normals for each date string and append the results to a list called `normals`.

* Loaded the list of daily normals into a Pandas DataFrame and set the index equal to the date.

* Used Pandas to plot an area plot (`stacked=False`) for the daily normals.

  ![daily-normals](Images/daily-normals.png)
