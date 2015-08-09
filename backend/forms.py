from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField, SubmitField, validators, ValidationError, PasswordField
from models import *
from backend import db


class GrocerySignupForm(Form):
  username = TextField("username",  [validators.Required("Please enter your username.")])
  password = TextField("password",  [validators.Required("Please enter your password.")])
  userType = ""
  def __init__(self, *args, **kwargs):
    Form.__init__(self, *args, **kwargs)
 
  def validate(self):
    if not Form.validate(self):
      return False
     
    user = GroceryUser.query.filter_by(username = self.username.data.lower()).first()
    if user:
      self.username.errors.append("That username is already taken")
      return False
    else:
      return True


class FoodbankSignupForm(Form):
  username = TextField("username",  [validators.Required("Please enter your username.")])
  password = TextField("password",  [validators.Required("Please enter your password.")])
  userType = ""
  def __init__(self, *args, **kwargs):
    Form.__init__(self, *args, **kwargs)
 
  def validate(self):
    if not Form.validate(self):
      return False
     
    user = FoodbankUser.query.filter_by(username = self.username.data.lower()).first()
    if user:
      self.username.errors.append("That username is already taken")
      return False
    else:
      return True

class GrocerySigninForm(Form):
  username = TextField("username",  [validators.Required("Please enter your username.")])
  password = TextField("password",  [validators.Required("Please enter your password.")])
  userType = ""
  def __init__(self, *args, **kwargs):
    Form.__init__(self, *args, **kwargs)
 
  def validate(self):
    if not Form.validate(self):
      return False
     
    user = GroceryUser.query.filter_by(username = self.username.data.lower()).first()
    if user and user.check_password(self.password.data):
      return True
    else:
      self.username.errors.append("Invalid e-mail or password")
      return False

class FoodbankSigninForm(Form):
  username = TextField("username",  [validators.Required("Please enter your username.")])
  password = TextField("password",  [validators.Required("Please enter your password.")])
  userType = ""
  def __init__(self, *args, **kwargs):
    Form.__init__(self, *args, **kwargs)
 
  def validate(self):
    if not Form.validate(self):
      return False
     
    user = FoodbankUser.query.filter_by(username = self.username.data.lower()).first()
    if user and user.check_password(self.password.data):
      return True
    else:
      self.username.errors.append("Invalid e-mail or password")
      return False


class SigninForm(Form):
  username = TextField("username",  [validators.Required("Please enter your username.")])
  password = TextField("password",  [validators.Required("Please enter your password.")])
  userType = ""
  
  def __init__(self, *args, **kwargs):
    Form.__init__(self, *args, **kwargs)
 
  def validate(self, userType):
    if not Form.validate(self):
      return False
     
    user = ""
    if userType == "grocery":
      user = GroceryUser.query.filter_by(username = self.username.data.lower()).first()
    else:
      user = FoodbankUser.query.filter_by(username = self.username.data.lower()).first()
    if user and user.check_password(self.password.data):
      return True
    else:
      self.username.errors.append("Invalid e-mail or password")
      return False
