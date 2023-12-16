from budgetpal import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from sqlalchemy.orm import relationship


# define the database tables
class User(UserMixin, db.Model):
    # schema for the user model
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, index=True)
    balance = db.Column(db.Float, default=0.0, nullable=False)
    savings = db.Column(db.Float, default=0.0, nullable=False)
    expenses = db.relationship('Expense', backref='user', lazy=True)
    joined_at = db.Column(db.DateTime(), default=datetime.utcnow, index=True)
    # functions for flask login functionality

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_id(self):
        return str(self.id)

    def is_authenticated(self):
        return True  # Return True if the user is authenticated, else False

    def is_active(self):
        return True  # Return True if the user is active, else False

    def is_anonymous(self):
        return not self.is_authenticated()


class Expense(db.Model):
    # schema for expense model
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(255))
    expense_date = db.Column(db.Date, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    category_id = db.Column(
        db.Integer, db.ForeignKey('category.id'), nullable=True)
    category = db.relationship('Category', backref='expenses', lazy=True)


class Category(db.Model):
    # schema for category model
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    logo_url = db.Column(db.String(255), nullable=False)

    def init_categories():
        # Query all of the categories
        existing_categories = Category.query.all()
        # check if the categories already existing_categories
        if not existing_categories:
            # pre-defined categories
            # if the categories do not exist create them
            income_category = Category(
                name="Income", logo_url="static/images/income_icon.png")
            rent_category = Category(
                name="Rent", logo_url="static/images/rent_icon.png")
            utility_category = Category(
                name="Utility", logo_url="static/images/utility_icon.png")
            car_category = Category(
                name="Car Expense", logo_url="static/images/car_icon.png")
            leisure_category = Category(
                name="Leisure", logo_url="static/images/leisure_icon.png")
            family_category = Category(
                name="Family", logo_url="static/images/family_icon.png")
            other_category = Category(
                name="Other", logo_url="static/images/other_icon.png")
            travel_category = Category(
                name="Travel", logo_url="static/images/travel_icon.png")
            education_category = Category(
                name="Education", logo_url="static/images/education_icon.png")
            saving_category = Category(
                name="Saving", logo_url="static/images/saving_icon.png")

            db.session.add_all([income_category, rent_category, utility_category, car_category, leisure_category,
                               family_category, other_category, travel_category, education_category, saving_category])
            db.session.commit()
