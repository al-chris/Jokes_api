# import os
# import sys
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)


# app.secret_key= os.environ.get('SECRET_KEY')
app.secret_key = 'secrt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'

# # app.config['USE_NGROK'] = True
# app.config['FLASK_ENV']='development'

db=SQLAlchemy(app)

from app import models
from app import views