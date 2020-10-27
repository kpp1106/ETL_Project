from flask import Flask, render_template

# Import our pymongo library, which lets us connect our Flask app to our Mongo database.
import pymongo
from flask_table import Table, Col

# Create an instance of our Flask app.
app = Flask(__name__)

# Create variable for our connection string
conn = 'mongodb://localhost:27017'

# Pass connection string to the pymongo instance.
client = pymongo.MongoClient(conn)

# Connect to a database. 
# If the database doesn't already exist, our code will create it automatically as soon as we insert a record.
db = client.finance_db
db2 = client.currency_db

# Declare your table
class ItemTable(Table):
    symbols = Col('Symbol')
    close_usd = Col('Close (USD)')
    close_cny = Col('Close (CNY)')
    close_eur = Col('Close (EUR)')
    close_inr = Col('Close (INR)')
    close_php = Col('Close (PHP)')


# Set route
@app.route('/')
def index():
    # Store the entire team collection in a list
    symbols = list(db.symbol.find())
    close_usd = list(db.close_usd.find())
    close_cny = list(db.close_cny.find())
    close_eur = list(db.close_eur.find())
    close_inr = list(db.close_inr.find())
    close_php = list(db.close_php.find())

    # Return the template with the players list passed in
    # return render_template('index.html', symbol=symbol, close_usd=close_usd, close_cny=close_cny, close_eur=close_eur, close_inr=close_inr, close_php=close_php)
    return render_template('index.html', symbols=symbols)

    
if __name__ == "__main__":
    app.run(debug=True)
