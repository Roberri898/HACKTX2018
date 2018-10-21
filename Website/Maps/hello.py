from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
	APIKEY="eaf63414ac97fea73d11cdea989d87b8"
	return render_template("index.html")