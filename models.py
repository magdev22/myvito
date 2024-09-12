from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), primary_key=True)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.Email(100), nullable=False)
    number = db.Column(db.String(100), nullable=False)

class Auto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mark = db.Column(db.String(100), nullable=False)
    model = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)

class Chat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(100), nullable=False)
    time = db.Column(db.String(100), nullable=False)

class Clouds(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)

class Realty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    room = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)