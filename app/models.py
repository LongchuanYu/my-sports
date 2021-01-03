import base64, os, json, jwt
from app import db
from hashlib import md5
from time import time
from flask import url_for,current_app
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime,timedelta

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(8), index=True)
    password_hash=db.Column(db.String(128))
    mydata = db.relationship('MyData', backref='user', lazy='dynamic', cascade='all,delete-orphan')
    def __repr__(self):
        return '<User %r>' % self.username

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash,password)


class MyData(db.Model):
    __tablename__ = 'mydatas'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), index=True)
    timestamp = db.Column(db.DateTime, index=True)
    # data for everyday
    data = db.Column(db.Text)

    def __repr__(self):
        return '<MyData %r>' % self.id