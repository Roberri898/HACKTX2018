from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import requests
import os
 
app = Flask(__name__)
 
@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('logged_in')


@app.route('/login', methods=['POST'])
def do_admin_login():
	r = requests.get('localhost:3030/user',params = {"email":request.form['username']})
    if r.status_code == requests.codes.ok:
        session['logged_in'] = True
        return "ok??????????????????"
    else:
        flash('wrong password!')
    return home()
 
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4000)