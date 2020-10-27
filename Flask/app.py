from flask import Flask, render_template

# Import our pymongo library, which lets us connect our Flask app to our Mongo database.
import pymongo
from flask_table import Table, Col
import csv

# Create an instance of our Flask app.
app = Flask(__name__)




@app.route("/")
def index():
  with open('data_sym_price.csv') as csv_file:
    data = csv.reader(csv_file)
    first_line = True
    stocks = []
    for row in data:
      if not first_line:
        stocks.append({
          "Symbol": Col[0],
          "Close(USD)": Col[1],
          "Close(CNY)": Col[2],
          "Close(EUR)": Col[3],
          "Close(INR)": Col[4],
          "Close(PHP)": Col[5]
        })
      else:
        first_line = False
  return render_template("index.html", stocks=stocks)

    
if __name__ == "__main__":
    app.run(debug=True)
