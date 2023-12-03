from flask import render_template
from budgetpal import app, db
# import the tables from the app package
from budgetpal.models import User, Expense, Category


@app.route("/")
def home():
    return render_template("base.html")
