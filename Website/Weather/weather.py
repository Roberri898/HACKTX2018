import requests
import json
from flask import Flask
from flask import render_template


app = Flask(__name__)

api_key = 'eaf63414ac97fea73d11cdea989d87b8'
city = 'McAllen'
url = "https://api.openweathermap.org/data/2.5/forecast?q={}&appid={}".format(city,api_key)


def convertTime(time):
    _hour = int(time[:2])
    _min = time[3:]
    am_or_pm = "AM"

    if _hour >= 12:
        am_or_pm = "PM"
        _hour -= 12
    if _hour == 0:
        _hour = 12
        

    return "{}:{}{}".format(_hour, _min,am_or_pm)

def convertTemp(temp):
    f = temp *9/5 - 459.67
    c = temp - 273.15

    return "{}°F | {}°C".format(int(f), int(c))

@app.route('/weather')
def getWeather(year=2018, month=10, day=27):
    date = "{}-{}-{}".format(year, month, day)
    with requests.session() as sess:
        data = json.loads(sess.get(url).text)['list']
        w_data = []
        for x in data:
            w_date = x['dt_txt']
            if date == w_date[:10]:
                time = convertTime(w_date[11:-3])
                description = x['weather'][0]['description']
                temp = convertTemp(float(x['main']['temp']))
                t = (time, description, temp)
                w_data.append(t)

    show = False
    if(len(w_data) == 0):
        show = True
    return render_template("weather.html", d=w_data, s = show)

