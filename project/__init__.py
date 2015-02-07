#################
#### imports ####
#################

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt
import os

################
#### config ####
################

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config.from_object('config.BaseConfig')
db = SQLAlchemy(app)

from project import views
from models import User

