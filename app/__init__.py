from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from app import routes, models, utils

def _create_database():
    ''' Creates the database schema specified by the SQLAlchemy models '''
    print('Creating database schema ... ')
    db.create_all()
    print('Done!')