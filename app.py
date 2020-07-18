from datetime import datetime

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

from games import Minesweeper

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
    moves = db.Column(db.Integer, nullable=False)
    game_object = db.Column(db.PickleType, nullable=False)


@app.route('/api/users', methods=['POST'])
def new_user():
    email = request.form['email']
    if User.query.filter_by(email=email).first() == None:
        user = User(email=email)
        db.session.add(user)
        db.session.commit()
        return jsonify(data={'id': user.id, 'email': user.email})
    else:
        return jsonify(error={'code': 11}, message='User is already registered')

@app.route('/api/games', methods=['POST'])
def new_game():
    game = Game(
        user_id = 1,
        game_over = False,
        moves = 0,
        game_object = Minesweeper()
    )
    db.session.add(game)
    db.session.commit()
    return jsonify(
        game_id = game.id,
        user_id = game.user_id,
        game_over = game.game_over,
        moves = game.moves
    )

@app.route('/api/games/<gameid>', methods=['GET'])
def game_info(gameid):
    game = Game.query.filter_by(id=gameid).first()
    if game != None:
        user_board = game.game_object.get_user_board()
        return jsonify(
            data = {
                'id': game.id,
                'user_id': game.user_id,
                'date_created': game.date_created,
                'game_over': game.game_over,
                'game_id': game.id,
                'user_board': user_board
            }
        )
    else:
        return jsonify(error={'code': 21}, message='Game doesn\'t exist')
