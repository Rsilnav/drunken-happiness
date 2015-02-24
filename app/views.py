from flask import render_template, flash, redirect, session, url_for, request, \
    g, jsonify
from flask.ext.sqlalchemy import get_debug_queries
from datetime import datetime
from app import app, db
from .forms import LoginForm, EditForm, PostForm, SearchForm
from .models import Pregunta
from config import DATABASE_QUERY_TIMEOUT
from functools import wraps
import random as r



def correctsession(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('index'))
    return wrap



@app.route('/')
def index():
    return render_template('my-index.html')

@app.route('/contacto')
def contacto():
    return render_template('my-contacto.html')

@app.route('/populate')
def populate():
    db.session.remove()
    db.drop_all()

    db.create_all()

    with open("./prueba.csv") as f:
        for line in f:
            line = line.decode('utf-8')
            l = line.split("\t")
            q = Pregunta(l[1], l[2], l[3], l[4], l[5], int(l[6]))
            db.session.add(q)

    with open("./qmelectron.csv") as f:
        for line in f:
            line = line.decode('utf-8')
            l = line.split("\t")
            q = Pregunta(l[1], l[2], l[3], l[4], l[5], int(l[6]))
            db.session.add(q)

    db.session.commit()

    return "Populated"

@app.route('/preguntame')
def preguntame():
    return render_template('my-preguntame.html')


@app.route('/test')
def test():

    num = db.session.query(Pregunta).count()
    ps = db.session.query(Pregunta).all()
    p =  ps[r.randint(0, num-1)]

    session['harespondido'] = False
    session['pregunta'] = p.id

    if not 'numero' in session:
        session['numero'] = 0
    if 'acierto' in session and session['acierto'] == False:
        session['numero'] = 0

    return render_template('my-test.html', numero=session['numero']+1, pregunta=p)

@app.route('/answer/<int:id>')
def answer(id):

    p = None
    a = db.session.query(Pregunta).filter(Pregunta.id==session['pregunta']).first()

    

    if a.correcta == id:
        session['acierto'] = True
        session['numero'] = session['numero'] + 1
    else:
        session['acierto'] = False

    session['harespondido'] = True
    return redirect(url_for('answerw'))

@app.route('/answer')
def answerw():
    p = None
    return render_template('my-test.html', numero=session['numero'], pregunta=p)