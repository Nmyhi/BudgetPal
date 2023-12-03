# import db from the application package and UserMixin from Flask_login
from budgetpal import db
from flask_login import UserMixin


# define the database tables
class User(UserMixin, db.Model):
    # schema for the user model
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    balance = db.Column(db.Float, default=0.0, nullable=False)
    savings = db.Column(db.Float, default=0.0, nullable=False)
    expenses = db.relationship('Expense', backref='user', lazy=True)


class Expense(db.model):
    # schema for expense
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey(user_id), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category_id'), nullable=True)
    category = db.relationship('Category', backref='expenses', lazy=True)


class Category(db.Model):
    # schema for category
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    # Ill call it as logo_url for now which will be a pre coded category logo
    logo_url = db.Column(db.String(255), nullable=False)