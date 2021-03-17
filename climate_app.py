# Dependencies and setup
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func, desc
from flask import Flask, jsonify

# Create engine to hawaii.sqlite
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect an existing database into a new model
Base = automap_base()

# Reflect the tables
Base.prepare(engine, reflect = True)

# Save references to each table
measurement = Base.classes.measurement
station = Base.classes.station

# Create an app, being sure to pass __name__
app = Flask(__name__)

# List all routes that are available
@app.route("/")
def home():
    return (f"Welcome to my Climate App page!<br/>"
            f"-------------------------------------------<br/>"
            f"<br/>"
            f"Available routes:<br/>"
            f"<br/>"
            f"/api/v1.0/precipitation<br/>"
            f"/api/v1.0/stations<br/>"
            f"/api/v1.0/tobs<br/>"
            f"/api/v1.0/start_date<br/>"
            f"/api/v1.0/start_date/end_date<br/>")

# Define precipitation app route
@app.route("/api/v1.0/precipitation")
def precipitation():
    
    # Create our session (link) from Python to the database
    session = Session(engine)

    # Perform a query to retrieve the precipitation data
    precipitationData = session.query(measurement.date, measurement.prcp).all()

    # Convert query results to a dictionary using date as the key and prcp as the value
    precipitationDictionary = {}
    for date, prcp in precipitationData:
        precipitationDictionary[date] = prcp
    
    # Return the JSON representation of precipitation dictionary
    return jsonify(precipitationDictionary)

    # Close session
    session.close()

# Define stations app route
@app.route("/api/v1.0/stations")
def stations():

    # Create our session (link) from Python to the database
    session = Session(engine)

    # Perform a query to retrieve the stations data
    stationsData = session.query(station.id, station.station, station.name).all()
    
    # Return a JSON list of stations from the dataset
    return jsonify(list(stationsData))

    # Close session
    session.close()

# Define observations app route
@app.route("/api/v1.0/tobs")
def observations():

    # Create our session (link) from Python to the database
    session = Session(engine)

    # Perform a query to retrieve dates and temperature observations of the most active station for the last year of data
    mostActive_stations = session.query(measurement.station, func.count(measurement.station)).\
                          order_by(func.count(measurement.station).desc()).\
                          group_by(measurement.station).all()

    # Find the most active station
    mostActive_id = mostActive_stations[0][0]
    
    # Find most recent date in dataset, convert to date timestamp format, and calculate the date one year from the latest date in dataset
    stringRecent_date = session.query(measurement.date).order_by(measurement.date.desc()).first()[0]
    mostRecent_date = (dt.datetime.strptime(stringRecent_date, "%Y-%m-%d")).date()
    mostFormer_date = mostRecent_date - dt.timedelta(days = 365)

    # Perform a query to retrieve the date and temperature observations
    yearData = session.query(measurement.date, measurement.tobs).filter((measurement.station == mostActive_id)\
               & (measurement.date <= mostRecent_date)\
               & (measurement.date >= mostFormer_date)).all()    

    # Return the JSON representation of temperature observations
    return jsonify(yearData)

    # Close session
    session.close()

# Define starting date app route
@app.route("/api/v1.0/<start>")




if __name__ == "__main__":
    app.run(debug = True)