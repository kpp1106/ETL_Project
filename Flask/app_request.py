from flask import Flask, render_template

# Import our pymongo library, which lets us connect our Flask app to our Mongo database.
import pymongo

# Create an instance of our Flask app.
app = Flask(__name__)

# Create variable for our connection string
conn = 'mongodb://localhost:27017'

# Pass connection string to the pymongo instance.
client = pymongo.MongoClient(conn)

# Connect to a database. 
# If the database doesn't already exist, our code will create it automatically as soon as we insert a record.
db = client.team_db

# Drops collection if available to remove duplicates
# NOTE: This is only for demo purposes.
db.roster.drop()

# Creates a collection in the database and inserts two documents
db.roster.insert_many(
    [
        {
            'name': 'Cassandra',
            'position': 'Point Guard'
        },
        {
            'name': 'Felipe',
            'position': 'Center'
        }
    ]
)


# Set route
@app.route('/')
def index():
    # Store the entire team collection in a list
    players = list(db.roster.find())
    print(players)

    # Return the template with the players list passed in
    return render_template('index.html', players=players)

# Define route to insert new players into the database
@app.route('/insert/<name>/<position>')
def insert(name, position):
    new_player = {
                    'name': name, 
                    'position': position
                  }
    db.roster.insert_one(new_player)
    return f"{name} has been inserted into the database!"


# Below is another option to capture arguments from the url using Flask's request function.
# This approach would use the below URL format:
    # http://localhost:5000/new_player?name=Jane Doe&position=Point Guard
from flask import request
@app.route('/new_player')
def new_player():
    name = request.args.get('name')
    position = request.args.get('position')
    new_player = {
                    'name': name, 
                    'position': position
                  }
    db.roster.insert_one(new_player)

    return f"{name} has been inserted into the database!"

if __name__ == "__main__":
    app.run(debug=True)
