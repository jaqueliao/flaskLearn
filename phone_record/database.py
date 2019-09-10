from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))

db = None


def close_db(e=None):
    db.close_all_sessions()


def db_init():
    db.create_all()


def init_app(app):
    global db
    db = SQLAlchemy(app)
    app.teardown_appcontext(close_db)
