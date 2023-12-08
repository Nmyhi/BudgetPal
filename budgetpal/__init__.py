import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):
    import env  # noqa
from flask_login import LoginManager

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")


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
