import requests
import json

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

    return "{}F/{}C".format(int(f), int(c))

def getWeather(year, month, day):
    date = "{}-{}-{}".format(year, month, day)
    with requests.session() as sess:
        data = json.loads(sess.get(url).text)['list']

        for x in data:
            w_date = x['dt_txt']
            if date == w_date[:10]:
                time = convertTime(w_date[11:-3])
                description = x['weather'][0]['description']
                temp = convertTemp(float(x['main']['temp']))
                print(time)
                print(description)
                print(temp)
                print('\n')
            

getWeather(2018,10,26)