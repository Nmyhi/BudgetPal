import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, url_for, flash, redirect
from flask_login import UserMixin, LoginManager, login_user, current_user, logout_user
from flask import render_template
from budgetpal.forms import RegistrationForm, LoginForm
from budgetpal.models import User, Expense, Category
from budgetpal import app, db


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["POST", "GET"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password1.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('registration.html', form=form)


@app.route("/loggin", methods=["GET", "POST"])
def loggin():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.check_password(form.password.data):
            login_user(user)
            next = request.args.get("next")
            return redirect(next or url_for('userpage'))
        flash('Invalid email address or Password.')
    return render_template('loggin.html', form=form)


@app.route("/loggout")
# @login_required
def loggout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/userpage")
def userpage():
    return render_template("userpage.html")


@app.route("/add_balance")
def add_balance():
    return render_template("add_balance.html")
