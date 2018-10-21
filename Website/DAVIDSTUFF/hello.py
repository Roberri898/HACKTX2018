from flask import Flask
from flask import render_template
from flask import request
import requests
import functions

app = Flask(__name__)

@app.route('/')
def hello_world():
	APIKEY="eaf63414ac97fea73d11cdea989d87b8"
	r = requests.get('http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID={0}'.format(APIKEY))
	return render_template("index.html")

@app.route('/reserve')
def reserve():

	return render_template("reserve.html")


@app.route('/search', methods=['GET'])
def search():
	Arriving = request.args.get("Arriving")
	Departing = request.args.get("Departing")
	Date = request.args.get("Date")
	URL = "http://localhost:3030/flights?origin=" + Departing + "&destination=" + Arriving + "&date=" + Date
	
	r = requests.get(URL)
	parsedFlightList = functions.parseFlightList(r.content)
	return render_template("search.html", list=parsedFlightList, url=URL)


@app.route('/purchase', methods=['GET'])
def purchase():
	data = request.args.get("id")
	print "data" + data
	return data

