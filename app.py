from flask import Flask, jsonify, render_template
#from csv import Table, Col
# Import our pymongo library, which lets us connect our Flask app to our Mongo database.
import pymongo
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, and_
from sqlalchemy.ext.automap import automap_base
from config import pg_user, pg_password

# Create an instance of our Flask app.
app = Flask(__name__)

# Create engine   

db_name = 'finance_db'   

connection_string = f"{pg_user}:{pg_password}@localhost:5432/{db_name}"
engine = create_engine(f'postgresql://{connection_string}')

# reflect an existing database into a new model
Base = automap_base()
Base.prepare(engine, reflect=True)
Base.classes.keys()

# Save reference to the table
sym_price = Base.classes.sym_price

@app.route('/')
def home():
    session = Session(engine)
    results = session.query(sym_price).all()
    # close the session to end the communication with the database
    session.close()
    # Convert the query results to a dictionary
    summary_list = []
    for f in results:
        summary_dict = {}
        summary_dict["Symbol"] = f.symbol
        summary_dict["Close USA"] = f.close_usd
        summary_dict["Close China"] = f.close_cny
        summary_dict["Close Europe"] = f.close_eur
        summary_dict["Close India"] = f.close_inr
        summary_dict["Close Phillipines"] = f.close_php

        
        summary_list.append(summary_dict)
    # Return the JSON representation of the dictionary
    return jsonify(summary_list)
    
if __name__ == "__main__":
    app.run(debug=True)