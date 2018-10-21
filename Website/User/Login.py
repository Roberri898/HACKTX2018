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
    r = requests.get('http://localhost:3030/user',params = {"email":request.form.get('username')})
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        return "ok??????????????????"
    else:
        return "asd"
    return home()
 