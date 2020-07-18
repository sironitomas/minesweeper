# Minesweeper

RESTful API Demo (work in progress)

## Requirements

* Design and implement a documented RESTful API for the game

## RESTful API endpoints (can be extended/modified)

To add a new user:
* POST `/api/users`

To get user info:
* GET `/api/users/<userid>`

To create a new game:
* POST `/api/games`

To get a list of games:
* GET `/api/games`

To get game information:
* GET `/api/games/<gameid>`

To play game:
* PUT `/api/games/<gameid>`

## Other details

* SQLAlchemy used as ORM
