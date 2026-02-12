from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# create db object, no app yet
# db = SQLAlchemy() -> This creates the SQLAlchemy database object, but without connecting it to a Flask app yet.
db = SQLAlchemy()