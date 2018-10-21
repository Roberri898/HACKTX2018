from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
	items={"lats":30.2627,"lot":-97.7431}
	return render_template("index.html",lot=items["lot"],lats=items["lats"])