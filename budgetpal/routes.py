import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, url_for, flash, redirect
from flask_login import UserMixin, LoginManager, login_user, current_user, logout_user
from flask import render_template
from datetime import datetime
from budgetpal.forms import RegistrationForm, LoginForm
from budgetpal.models import User, Expense, Category
from budgetpal import app, db


# Home route
@app.route("/")
def home():
    """Render the home page"""
    return render_template("index.html")


# Register route
@app.route("/register", methods=["POST", "GET"])
def register():
    """Render the registration page and handles the registration"""
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password1.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('registration.html', form=form)


# Login route
@app.route("/sign_in_user", methods=["GET", "POST"])
def sign_in_user():
    """Render the login page and handles the login"""
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.check_password(form.password.data):
            login_user(user)
            next = request.args.get("next")
            return redirect(next or url_for('userpage'))
        flash('Invalid email address or Password.')
    return render_template('sign_in_user.html', form=form)


# Logout route
@app.route("/sign_out_user")
def sign_out_user():
    """Log the user out"""
    logout_user()
    return redirect(url_for('home'))


# Userpage route
@app.route("/userpage")
def userpage():
    """Render the user page"""
    # query the expenses of the current user
    if current_user.is_anonymous != True:
        expenses = Expense.query.filter_by(user_id=current_user.id).all()
        categories = Category.query.all()
        return render_template("userpage.html", expenses=expenses, categories=categories)
    else:
        return render_template("userpage.html")


# Add income route
@app.route("/add_income", methods=["GET", "POST"])
def add_income():
    """Render the add_income page and handle the user balance update"""
    if request.method == "POST":
        current_user_info = User.query.filter_by(id=current_user.id).first()
        income_amount = float(request.form.get("income_amount"))
        expense = Expense(
            amount=request.form.get("income_amount"),
            description=request.form.get("income_description"),
            expense_date=request.form.get("income_date"),
            user_id=current_user.id,
            category_id=request.form.get("income_category")
        )
        # Update the user's balance
        current_user_info.balance += income_amount
        db.session.add(expense)
        db.session.commit()
        return redirect(url_for('userpage'))
    categories = Category.query.all()
    return render_template("add_income.html", categories=categories)


# Add expense route
@app.route("/add_expense", methods=["GET", "POST"])
def add_expense():
    """Render the add_expense page and handle the user saving and balance update
    when the expense was a saving"""
    current_user_info = User.query.filter_by(id=current_user.id).first()
    if request.method == "POST":
        expense = Expense(
            amount=request.form.get("expense_amount"),
            description=request.form.get("expense_description"),
            expense_date=request.form.get("expense_date"),
            user_id=current_user.id,
            category_id=request.form.get("expense_category")
        )
        expense_amount = float(request.form.get("expense_amount"))
        category = Category.query.get(expense.category_id)
        if category.name == "Saving":
            # Update the user's savings
            current_user_info.savings += expense_amount
            db.session.add(expense)
            db.session.commit()
            # Update the user's balance
        current_user_info.balance -= expense_amount
        db.session.add(expense)
        db.session.commit()
        return redirect(url_for('userpage'))
    categories = Category.query.all()
    return render_template("add_expense.html", categories=categories)


# Edit income route
@app.route("/edit_income/<int:income_id>", methods=["GET", "POST"])
def edit_income(income_id):
    """Render the edit_income page and handle the user balance update"""
    expense = Expense.query.get_or_404(income_id)
    prev_amount = expense.amount
    categories = Category.query.all()
    if request.method == "POST":
        current_amount = float(request.form.get("income_amount"))
        # Logic for update the user's balance
        if prev_amount > current_amount:
            calculated_difference = prev_amount - current_amount
            current_user.balance -= calculated_difference

            expense.amount = request.form.get("income_amount")
            expense.description = request.form.get("expense_description")
            expense.expense_date = request.form.get("expense_date")
            expense.category_id = request.form.get("income_category")

            db.session.commit()
        # logic for update the user's balance
        if prev_amount < current_amount:
            calculated_difference = current_amount - prev_amount
            current_user.balance += calculated_difference

            expense.amount = request.form.get("income_amount")
            expense.description = request.form.get("expense_description")
            expense.expense_date = request.form.get("expense_date")
            expense.category_id = request.form.get("income_category")

            db.session.commit()
        expense.amount = request.form.get("income_amount")
        expense.description = request.form.get("expense_description")
        expense.expense_date = request.form.get("expense_date")
        expense.category_id = request.form.get("income_category")
        return redirect(url_for('userpage'))
    return render_template("edit_income.html", expense=expense, categories=categories)


# Edit saving route
@app.route("/edit_saving/<int:saving_id>", methods=["GET", "POST"])
def edit_saving(saving_id):
    """Render the edit_saving page and handle the user balance"""
    expense = Expense.query.get_or_404(saving_id)
    prev_amount = expense.amount
    categories = Category.query.all()
    if request.method == "POST":
        current_amount = float(request.form.get("saving_amount"))
        # Logic for update user balance and saving
        if prev_amount > current_amount:
            calculated_difference = prev_amount - current_amount
            current_user.balance += calculated_difference
            current_user.savings -= calculated_difference

            expense.amount = request.form.get("saving_amount")
            expense.description = request.form.get("expense_description")
            expense.expense_date = request.form.get("expense_date")
            expense.category_id = request.form.get("saving_category")

            db.session.commit()
        # Logic for update user balance and saving
        if prev_amount < current_amount:
            calculated_difference = current_amount - prev_amount
            current_user.balance -= calculated_difference
            current_user.savings += calculated_difference

            expense.amount = request.form.get("saving_amount")
            expense.description = request.form.get("expense_description")
            expense.expense_date = request.form.get("expense_date")
            expense.category_id = request.form.get("saving_category")

            db.session.commit()
        expense.amount = request.form.get("saving_amount")
        expense.description = request.form.get("expense_description")
        expense.expense_date = request.form.get("expense_date")
        expense.category_id = request.form.get("saving_category")
        return redirect(url_for('userpage'))
    return render_template("edit_saving.html", expense=expense, categories=categories)


# Edit expense route
@app.route("/edit_expense/<int:expense_id>", methods=["GET", "POST"])
def edit_expense(expense_id):
    """Render the edit_expense page and handle the user balance"""
    expense = Expense.query.get_or_404(expense_id)
    prev_amount = expense.amount
    categories = Category.query.all()
    if request.method == "POST":
        current_amount = float(request.form.get("expense_amount"))
        # Logic for update user balance
        if prev_amount > current_amount:
            calculated_difference = prev_amount - current_amount
            current_user.balance += calculated_difference

            expense.amount = request.form.get("expense_amount")
            expense.description = request.form.get("expense_description")
            expense.expense_date = request.form.get("expense_date")
            expense.category_id = request.form.get("expense_category")

            db.session.commit()
        # Logic for update user balance
        if prev_amount < current_amount:
            calculated_difference = current_amount - prev_amount
            current_user.balance -= calculated_difference

            expense.amount = request.form.get("expense_amount")
            expense.description = request.form.get("expense_description")
            expense.expense_date = request.form.get("expense_date")
            expense.category_id = request.form.get("expense_category")

            db.session.commit()
        expense.amount = request.form.get("expense_amount")
        expense.description = request.form.get("expense_description")
        expense.expense_date = request.form.get("expense_date")
        expense.category_id = request.form.get("expense_category")

        db.session.commit()
        return redirect(url_for('userpage'))
    return render_template("edit_expense.html", expense=expense, categories=categories)


# Delete expense route
@app.route("/delete_expense/<int:expense_id>")
def delete_expense(expense_id):
    """Delete the expense and handle the user income and saving if it was an income or saving"""
    expense = Expense.query.get_or_404(expense_id)

    # subtract the income amount from the balance if it was an income
    if expense.category.name == 'Income':
        current_user.balance -= expense.amount

    # deduct the saving amount from the user's savings if it was a saving
    elif expense.category.name == 'Saving':
        current_user.savings -= expense.amount
        current_user.balance += expense.amount

    # for any other category, add the amount back to the balance
    else:
        current_user.balance += expense.amount

    db.session.delete(expense)
    db.session.commit()

    return redirect(url_for('userpage'))


# Add category route
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    """Render the add_category page"""
    if request.method == "POST":
        category = Category(
            name=request.form.get("category_name"),
            logo_url=request.form.get("category_logo"),
        )
        db.session.add(category)
        db.session.commit()
        return redirect(url_for('userpage'))
    categories = Category.query.all()
    return render_template("add_category.html", categories=categories)
