from datetime import datetime

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    games = db.relationship('Game', backref=db.backref('user'), lazy=True)


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now)
    game_over = db.Column(db.Boolean, nullable=False)
    system_board = db.Column(db.PickleType, nullable=False)
    user_board = db.Column(db.PickleType, nullable=False)


@app.route('/api/users', methods=['POST'])
def new_user():
    email = request.form['email']
    if User.query.filter_by(email=email).first() == None:
        user = User(email=email)
        db.session.add(user)
        db.session.commit()
        return jsonify(data={'id':user.id, 'email':user.email})
    else:
        return jsonify(error={'code': 11}, message='User is already registered')
