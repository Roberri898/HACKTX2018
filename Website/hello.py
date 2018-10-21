from flask import Flask
from flask import render_template
import request
app = Flask(__name__)

@app.route('/')
def hello_world():
	APIKEY="eaf63414ac97fea73d11cdea989d87b8"
	r = requests.get('http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID={0}'.format(APIKEY))
	return render_template("index.html")