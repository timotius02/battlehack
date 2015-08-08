from backend import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    social_id = db.Column(db.String(64), nullable=False, unique=True)
    nickname = db.Column(db.String(64), nullable=False, index=True, unique=True)
    email = db.Column(db.String(120), nullable=True, index=True, unique=True)

    def __repr__(self):
        return '<User %r>' % (self.nickname)
