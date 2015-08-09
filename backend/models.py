from backend import db
from werkzeug import generate_password_hash, check_password_hash

class GroceryUser(db.Model):
    __tablename__ = 'groceryuser'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), index=True, unique=True)
    pwdhash = db.Column(db.String(54))
    products = db.relationship('Product', backref='grocery', lazy='dynamic')

    def __repr__(self):
        return '<GroceryUser %r>' % (self.username)

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)
     
    def set_password(self, password):
        self.pwdhash = generate_password_hash(password)
   
    def check_password(self, password):
        return check_password_hash(self.pwdhash, password)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    item_number = db.Column(db.Integer)
    expiration = db.Column(db.DateTime)
    quantity = db.Column(db.Integer)
    name = db.Column(db.String(64))
    price = db.Column(db.Float)
    sale = db.Column(db.Boolean, index=True)
    groceryUser_id = db.Column(db.Integer, db.ForeignKey('groceryuser.id'))

    def __repr__(self):
        return '<Product %r>' % (self.name)

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    item_number = db.Column(db.Integer)
    delivery = db.Column(db.DateTime)
    quantity = db.Column(db.Integer)
    name = db.Column(db.String(64))
    price = db.Column(db.Float)
    status = db.Column(db.String(64))
    foodbankUser_id = db.Column(db.Integer, db.ForeignKey('foodbankuser.id'))


class FoodbankUser(db.Model):
    __tablename__ = 'foodbankuser'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), index=True, unique=True)
    pwdhash = db.Column(db.String(54))
    transactions = db.relationship('Transaction', backref='foodbank', lazy='dynamic')

    def __repr__(self):
        return '<FoodbankUser %r>' % (self.username)

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)
     
    def set_password(self, password):
        self.pwdhash = generate_password_hash(password)
   
    def check_password(self, password):
        return check_password_hash(self.pwdhash, password)
