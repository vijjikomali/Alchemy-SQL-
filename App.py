#1. Import Flask

import datetime as dt
import pandas as pd
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#-----------------------------------------------
# Flask App Setup                              |
#-----------------------------------------------

engine = create_engine("sqlite:///hawaii.sqlite")

Base = automap_base()

Base.prepare(engine, reflect=True)

# Measurement = Base.classes.measurement
# Station = Base.classes.station

# session = Session(bind=engine)

# 2.reate an app
app = Flask(__name__)

# 3. Define static routes
@app.route("/")
def vij():
       
        return (
                "<h1>Hello, Everyone</h1><p>Welcome to the Climate Analysis of Hawaii!</p>"
                
                f"<a href='/api/v1.0/precipitation'>/api/v1.0/precipitation</a><br/>"
                f"<a href='/api/v1.0/stations'>/api/v1.0/stations</a><br/>"
                f"<a href='/api/v1.0/tobs'>/api/v1.0/tobs</a><br/>"    
        )
# 4. Define main behavior
if __name__ == '__main__':
        app.run(debug=True) 

# 5. Define static route - precipitation on Measurement Table
@app.route("/api/v1.0/precipitation")
def precipt():
       
        month_presp= session.query(Measurement.date).order_by(Measurement.id.desc()).first()
        last_year = dt.date(2017,8,23) - dt.timedelta(days=365)
        rain = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= last_year).\
        order_by(Measurement.date).all()
        presp_df = pd.DataFrame(rain)

        return (
                f"<H3>Welcome to the Hawaii Climate Analysis API!<br/><br />"
                f"<b> Routes of this area </b>"
                f"<a href='/api/v1.0/precipitation'>/r of  Routes:<br/></b>"api/v1.0/precipitation</a><br/>"
                f"<a href='/api/v1.0/stations'>/api/v1.0/stations</a><br/>"
                f"<a href='/api/v1.0/tobs'>/api/v1.0/tobs</a><br/>"
        )
if __name__ == '__main__':
        app.run(debug=True)

@app.route("/api/v1.0/stations")
def stations():
       
        list_st= session.query(Measurement.tobs).order_by(Measurement.tobs.desc()).first()
        active_station = session.query(Measurement.station, func.count(Measurement.tobs)).group_by(Measurement.station).\
        order_by(func.count(Measurement.tobs).desc()).all()
        hitemp_obsrv= session.query(Measurement.station, Measurement.tobs).\
        filter(Measurement.station  == 'USC00519281').\
        filter(Measurement.date > last_year).all()

        return (
                
        )

if __name__ == '__main__':
        app.run(debug=True)