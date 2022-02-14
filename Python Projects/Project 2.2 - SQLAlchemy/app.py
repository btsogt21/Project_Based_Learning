#imports
import json
from flask import Flask, jsonify

import numpy as np
import pandas as pd
import datetime as dt

#import sqlalchemy
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import  Session
from sqlalchemy import create_engine, func

#create the database connection
engine = create_engine("sqlite:///hawaii.3.sqlite")

#reflect existing database into a new model
Base = automap_base()

#reflect tables
Base.prepare(engine, reflect=True)

#save the references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

#Create the session
session = Session(engine)

#Flask set up
app = Flask(__name__)

#Flask Routes- Welcome, /api/v1.0/precipitation, /api/v1.0/stations, TOBS for last year, temp range
@app.route("/")
def index():
    return(
        f"Welcome to the Hawaii Climate App!<br/>"
        f"Available Routes:<br/> "
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/weatherstations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start>/<end>"
    )

# Route 1- precipitation info
@app.route("/api/v1.0/precipitation")
def precipitation():
    #get the Aug 2016 to Aug 2017 data
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days = 365)

    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()
    
    session.close()

    #return as json
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

@app.route("/api/v1.0/weatherstations")
def weatherstations(): 
    #return a list of all stations
    stations = Session.query(Station.station).all()

    session.close()

    #convert array into a list
    stations = list(np.ravel(stations))
    return jsonify(stations=stations)


@app.route("/api/v1.0/tobs")
def tobs():
    #for the most active station in the last year of data, return the prior year temp observations as a json
    prev_yr = dt.date(2017,8,23) - dt.timedelta(days=365)

    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_yr).all() 

    session.close()

    temps =list(np.ravel(results))
    return jsonify(temps=temps)


@app.route("/api/v1.0<start>")
@app.route("/api/v1.0/<start>/<end>")
def temp(start=None, end=None):

    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        start = dt.datetime.strptime(start, "%m%d%Y")
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        session.close()

        temps = list(np.ravel(results))
        return jsonify(temps=temps)

    start = dt.datetime.strptime(start, "%m%d%Y")
    end = dt.datetime.strptime(end, "%m%d%Y")

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all

    session.close()

    temps = list(np.ravel(results))
    return jsonify(temps=temps)



if __name__ =='__main__':
    app.run()

















