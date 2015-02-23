from hashlib import md5
import re
from app import db
from app import app


class Pregunta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    frase = db.Column(db.Text)
    res1 = db.Column(db.Text)
    res2 = db.Column(db.Text)
    res3 = db.Column(db.Text)
    res4 = db.Column(db.Text)
    correcta = db.Column(db.Integer)

    def __init__(self, f, r1, r2, r3, r4, c):
        self.frase = f
        self.res1 = r1
        self.res2 = r2
        self.res3 = r3
        self.res4 = r4
        self.correcta = c

    def __repr__(self):  # pragma: no cover
        return '<Pregunta %r %r>' % (self.id, self.frase)