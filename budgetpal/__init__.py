import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):
    import env  # noqa
from flask_login import LoginManager


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
if os.environ.get("DEVELOPMENT") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
else:
    uri = os.environ.get("DATABASE_URL")
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    app.config["SQLALCHEMY_DATABASE_URI"] = uri


# Initialize categories before the first request
@app.before_first_request
def before_first_request():
    with app.app_context():
        from budgetpal.models import Category
        Category.init_categories()


db = SQLAlchemy(app)
# add login_manager variables
login_manager = LoginManager(app)
login_manager.init_app(app)


# define the user loader function
@login_manager.user_loader
def load_user(user_id):
    from budgetpal.models import User
    return User.query.get(int(user_id))


from budgetpal import routes  # noqa
