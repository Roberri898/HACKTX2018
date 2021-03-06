from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort, escape, url_for
import requests
import functions
import os
import json
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
    if 'username' in session:
        return render_template("reserve.html")
    else:
        return redirect(url_for('home'))

@app.route('/search', methods=['GET'])
def search():
    Arriving = request.args.get("Arriving")
    Departing = request.args.get("Departing")
    Date = request.args.get("Date")
    
    URL = "http://localhost:3030/flights?origin=" + Departing + "&destination=" + Arriving + "&date=" + Date
    r = requests.get(URL)
    parsedFlightList = functions.parseFlightList(r.content)
    date = parsedFlightList[0]['departureTime']
    time = date[11:16]
    date = date[:10]

    return render_template("search.html", list=parsedFlightList, url=URL, time = time, date = date)



@app.route('/purchase', methods=['GET'])
def purchase():
    flightNumber = request.args.get("flightNumber")
    date = request.args.get("time")
    time = date[11:16]
    date = date[:10]
    latLon = functions.flightIdAndDateToCoordinates(flightNumber,date)
    latitude = latLon['latitude']
    longitude = latLon['longitude']

    api_key = 'eaf63414ac97fea73d11cdea989d87b8'
    url = "https://api.openweathermap.org/data/2.5/forecast?lat={}&lon={}&appid={}".format(latitude,longitude,api_key)

	
	#date = "{}-{}-{}".format(year, month, day)
    with requests.session() as sess:
        data = json.loads(sess.get(url).text)['list']
        w_data = []
        for x in data:
            w_date = x['dt_txt']
            if date == w_date[:10]:
                time = functions.convertTime(w_date[11:-3])
                description = x['weather'][0]['description']
                temp = functions.convertTemp(float(x['main']['temp']))
                t = (time, description, temp)
                w_data.append(t)

    show = False
    if(len(w_data) == 0):
        show = True

    items={"lats":30.2627,"lot":-97.7431}
    return render_template("index.html",lot=longitude,lats=latitude,d=w_data, s = show)






@app.route('/')
def getData(year=2018, month=10, day=22):
    date = "{}-{}-{}".format(year, month, day)
    with requests.session() as sess:
        data = json.loads(sess.get(url).text)['list']
        w_data = []
        for x in data:
            w_date = x['dt_txt']
            if date == w_date[:10]:
                time = functions.convertTime(w_date[11:-3])
                description = x['weather'][0]['description']
                temp = functions.convertTemp(float(x['main']['temp']))
                t = (time, description, temp)
                w_data.append(t)

    show = False
    if(len(w_data) == 0):
        show = True

    items={"lats":30.2627,"lot":-97.7431}
    return render_template("index.html",lot=items["lot"],lats=items["lats"],d=w_data, s = show)
