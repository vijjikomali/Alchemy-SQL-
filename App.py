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


app = Flask(__name__)


@app.route("/")
def vij():
        return "This is a test message !!"

if __name__ == '__main__':
        app.run(debug=True) 