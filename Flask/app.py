from flask import Flask, render_template, request
import csv
from os import path
app = Flask(__name__)

script_dir = path.dirname(path.abspath(__file__))

@app.route ("/")
def index():
    return render_template("index.html") 

@app.route("/submitted", methods=["GET", "POST"])
def hello():
    if request.method == "GET":
        return render_template("index.html") 
    filefullpath = script_dir + '//newTest.csv'
    with open(filefullpath, mode="w+") as file:
        fileWriter = csv.writer(file)
        fileWriter.writerow(['Time', 'HomeTeam', 'AwayTeam'])
    file.close()
    return "hello world"