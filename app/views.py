from flask import render_template, flash, redirect, session, url_for, request, \
    g, jsonify
from flask.ext.sqlalchemy import get_debug_queries
from datetime import datetime
from app import app, db
from .forms import LoginForm, EditForm, PostForm, SearchForm
from .models import User, Post
from config import DATABASE_QUERY_TIMEOUT



@app.route('/')
def index():
    return "holamundo"