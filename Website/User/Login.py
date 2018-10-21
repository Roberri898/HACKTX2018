from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort, escape, url_for
import requests
import os
 
app = Flask(__name__)
app.secret_key = os.urandom(12)
 
@app.route('/')
def home():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return render_template("login.html")


@app.route('/login', methods=['POST'])
def do_admin_login():
    # r = requests.get('http://localhost:3030/user',params = {"email":request.form.get('username')})
    # print(r.status_code)
    if request.form['username']=='ok':
        session['username'] = request.form['username']
        return redirect(url_for('home'))

    else:
        return "asd"
    return home()

@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('home'))
 