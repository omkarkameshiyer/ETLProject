import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import request
from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine('sqlite:///movies.sqlite', echo=False)


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################


@app.route("/api/v1.0/allDataForAYear")
def yearDataCall():
    year = request.args.get('year', default = 1, type = int)
    resultData = engine.execute("SELECT title FROM movies where year =  "+str(year)).fetchall()
    # Create a dictionary from the row data and append to a list of all_passengers
    return str(resultData)

@app.route("/api/v1.0/starsData")
def titleCall():
    title = request.args.get('title', default = 1, type = str)
    print(title)
    resultData = engine.execute("SELECT stars FROM movies where title like  \'"+title+"\'").fetchall()
    # Create a dictionary from the row data and append to a list of all_passengers
    return str(resultData)

@app.route("/api/v1.0/revenueData")
def revenueCall():
    title = request.args.get('title', default = 1, type = str)
    print(title)
    resultData = engine.execute("SELECT revenue FROM movies where title like  \'"+title+"\'").fetchall()
    # Create a dictionary from the row data and append to a list of all_passengers
    return str(resultData)


@app.route("/api/v1.0/revenueData")
def yearCall():
    title = request.args.get('title', default = 1, type = str)
    print(title)
    resultData = engine.execute("SELECT year FROM movies where title like  \'"+title+"\'").fetchall()
    # Create a dictionary from the row data and append to a list of all_passengers
    return str(resultData)

@app.route("/api/v1.0/sqlQuery")
def runAQuery():
    query = request.args.get('query', default = 1, type = str)
    print(query)
    resultData = engine.execute(query).fetchall()
    # Create a dictionary from the row data and append to a list of all_passengers
    return str(resultData)

if __name__ == '__main__':
    app.run(debug=True)
