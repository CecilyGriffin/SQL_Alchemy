import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask
from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")
# reflect an existing database into a new model
base = automap_base()
# reflect the tables
base.prepare(engine, reflect=True)
# Save reference to the table
measurement = base.classes.measurement
station = base.classes.station
# Create our session (link) from Python to the DB
session = session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    return (
        "Welcome to the Climate API!<br/>"
        "Available Routes:<br/>"
       "/api/v1.0/precipitation<br/>"
       "/api/v1.0/stations<br/>"
       "/api/v1.0/tobs<br/>"
        "/api/v1.0/<start>" and "/api/v1.0/<start>/#<end>"
    )

@app.route("/about")
def about():
    print("Server received request for 'About' page...")
    return "Welcome to my 'About' page!"

@app.route("/api/v1.0/precipitation")
def precipitation():
    print("Server received request for 'precipitation' page...")
    return "Welcome to the Precipitation API!"

@app.route("/api/v1.0/stations")
def stations():
    print("Server received request for 'stations' page...")
    return "Welcome to the Stations API!"   

@app.route("/api/v1.0/tobs")
def tobs():
    print("Server received request for 'tobs' page...")
    return "Welcome to the Temperature API!"  

@app.route("/api/v1.0/<start>")
def tobs():
    print("Server received request for 'tobs' page...")
    return "Welcome to the Temperature API!"  

if __name__ == "__main__":
    app.run(debug=True)
