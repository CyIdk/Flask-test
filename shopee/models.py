from dis import Instruction
from enum import Flag
from pydoc import describe
from flask_sslify import SSLify
from flask_sqlalchemy import SQLAlchemy
from shopee import app

app.secret_key ="*0211_x23"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Enrpllment.db"
db =SQLAlchemy(app)
sslify = SSLify(app)


class Courses(db.Model):
    c_id = db.Column(db.Integer, primary_key=True, autoincrement= True)
    c_name = db.Column(db.Text, nullable=False)
    start_date = db.Column(db.Text, nullable=False)
    end_date = db.Column(db.Text, nullable=False)
    Instruction = db.Column(db.Text, nullable=False)
    description= db.Column(db.Text)

class Products(db.Model):
    pid = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.Text, nullable=False)
    origin = db.Column(db.Text)
    description = db.Column(db.Text)
    quantity = db.Column(db.Integer, nullable=False)
    unit_price = db.Column(db.Float, nullable=False)

    def __init__(
        self, pid, name, origin, description, quantity, unit_price
    ):
        self.pid = pid
        self.origing = origin
        self.description = description
        self.quantity = quantity
        self.unit_price = unit_price