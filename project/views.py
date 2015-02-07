from project import app # pragma: no cover 
from flask import flash, redirect, render_template, request, \
    url_for   # pragma: no cover

@app.route('/') # pragma: no cover 
def index():
    return "Hola mundo"

@app.route('/login') # pragma: no cover 
def login():
    return "login"

@app.route('/home') # pragma: no cover 
def home():
    return "Hola user"