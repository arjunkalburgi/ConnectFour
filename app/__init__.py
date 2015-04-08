from flask import Flask
# from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config.from_object("config")
# db = SQLAlchemy(app)

app.secret_key = 'you-will-never-guess'

from app import views


# import os
# from flask.ext.login import LoginManager
# from flask.ext.openid import OpenID
# from config import basedir

# lm = LoginManager()
# lm.init_app(app)
# oid = OpenID(app, os.path.join(basedir, 'tmp'))