from flask import Flask, render_template, jsonify
#from csv import Table, Col
# Import our pymongo library, which lets us connect our Flask app to our Mongo database.
import pymongo

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, and_

# Create an instance of our Flask app.
app = Flask(__name__)

# Create engine
pg_user = 'postgres'
pg_password = '****'
db_name = 'finance_db'                         

connection_string = f"{pg_user}:{pg_password}@localhost:5432/{db_name}"
engine = create_engine(f'postgresql://{connection_string}')

# reflect an existing database into a new model
Base = automap_base()
Base.prepare(engine, reflect=True)
Base.classes.keys()

# Save reference to the table
data_sym_price = Base.classes.data_sym_price
# Candidate_Votes = Base.classes.candidate_votes

# Conn = "mongodb://localhost:27017"
# client = pymongo.MongoClient(Conn)

# db = client.finance_db

@app.route("/")
def index():
  # with open('data_sym_price.csv') as csv_file:
    # data = Mongo.reader(csv_file)
    # first_line = True
    # stocks = list(db.stocks.find())
    # for row in data:
    #   if not first_line:
    #     stocks.append({
    #       "Symbol": Col[0],
    #       "Close(USD)": Col[1],
    #       "Close(CNY)": Col[2],
    #       "Close(EUR)": Col[3],
    #       "Close(INR)": Col[4],
    #       "Close(PHP)": Col[5]
    #     })
    #   else:
    #     first_line = False
  return render_template("index.html", stocks=stocks)

    
if __name__ == "__main__":
    app.run(debug=True)
