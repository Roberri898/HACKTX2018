from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort, escape, url_for
import requests
import functions
import os
app = Flask(__name__)
app.secret_key = os.urandom(12)

@app.route('/')
def hello_world():
	return redirect(url_for('home'))

@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('home'))


@app.route('/login')
def home():
    if 'username' in session:
        return redirect(url_for('reserve'))
    return render_template("login.html")

@app.route('/login', methods=['POST'])
def user_login():
    r = requests.get('http://localhost:3030/user',params = {"email":request.form.get('username')})
    print(r.status_code)
    if r.status_code==200:
        session['username'] = request.form['username']
        return redirect(url_for('reserve'))

    else:
        return redirect(url_for('user_login'))
    return home()

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

	flightNumber = request.args.get("flightNumber")
	date = request.args.get("time")
	time = date[11:16]
	date = date[:10]
	latLon = functions.flightIdAndDateToCoordinates(flightNumber,date)
	latitude = latLon['latitude']
	longitude = latLon['longitude']

	
	# return latLon
	data = "Lat: " + latitude + " Lon: " + longitude + "    Date: " + date 
	return data
