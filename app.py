import json
import random
import time
from datetime import datetime
from flask import Flask, Response, render_template, jsonify, request, url_for
import requests

app= Flask(__name__)

url = "http://flaskosa.herokuapp.com"

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/cmd")
def command_prompt():
    data = requests.get(url + "/cmd").text
    return data 

@app.route("/cmd/TRACE", methods=["GET", "POST"])
def traceData():
    data = requests.get(url + "/cmd/TRACE").json()
    return data
    
@app.route("/cmd/START")
def startInstrument():
    data = requests.get(url + "/cmd/START").text
    return data  

@app.route("/cmd/STOP")
def stopInstrument():
    data = requests.get(url + "/cmd/STOP").text
    return data  

@app.route("/cmd/IDN")
def getIdentificationString():
    data = requests.get(url + "/cmd/IDN").text
    return data  

@app.route("/cmd/LIM")
def xaxisLimits():
    data = requests.get(url + "/cmd/LIM").text
    return data 

@app.route("/cmd/ECHO/<string>")
def return_string(string):
    data = requests.get(url + "/cmd/ECHO/{}".format(string)).text 
    return data 

@app.route("/cmd/LIM/[<min>,<max>]")
def getOSATrace(min, max):
    data = requests.get(url + "/cmd/LIM/[{},{}]".format(min, max)).text 
    return data

@app.route("/cmd/PING")
def getPong():
    data = requests.get(url + "/cmd/PING").text 
    return data  

@app.route("/cmd/STATE")
def fetchState():
    data = requests.get(url + "/cmd/STATE").text 
    return data 

@app.route("/cmd/SINGLE")
def getSingleScan():
    data = requests.get(url + "/cmd/SINGLE").text 
    return data 

@app.route("/instructions")
def instructions():
    return render_template("instructions.html")

if __name__ == '__main__':
    app.run(debug=True)
