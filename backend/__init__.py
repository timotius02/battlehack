from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager, UserMixin, login_required

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

app.secret_key = 'awdawdawd'

app.config["MAIL_USERNAME"] = 'contact@example.com'
app.config["MAIL_PASSWORD"] = 'your-password'

from backend import views, models
