from backend import db
from werkzeug import generate_password_hash, check_password_hash

class GroceryUser(db.Model):
    __tablename__ = 'GroceryUsers'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), index=True, unique=True)
    pwdhash = db.Column(db.String(54))

    def __repr__(self):
        return '<GroceryUser %r>' % (self.username)

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)
     
    def set_password(self, password):
        self.pwdhash = generate_password_hash(password)
   
    def check_password(self, password):
        return check_password_hash(self.pwdhash, password)



class FoodbankUser(db.Model):
    __tablename__ = 'FoodbankUsers'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), index=True, unique=True)
    pwdhash = db.Column(db.String(54))

    def __repr__(self):
        return '<FoodbankUser %r>' % (self.username)

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)
     
    def set_password(self, password):
        self.pwdhash = generate_password_hash(password)
   
    def check_password(self, password):
        return check_password_hash(self.pwdhash, password)
