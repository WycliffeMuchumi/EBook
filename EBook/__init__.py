import psycopg2
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow



#initializing application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'af117adffa35391306eaddc2c413efba'
#database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12121994@127.0.0.1:5432/EBook'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
conn = psycopg2.connect("dbname='EBook' user='postgres' host='localhost' password='12121994'")

#creating SQLAlchemy instance
db = SQLAlchemy(app)

#initializing Marshmallow
ma = Marshmallow(app)

from EBook import views