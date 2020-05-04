from . import db, bcrypt

class Wish(db.Model):

    __tablename__ = 'wishes'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(1000), unique=True)
    like = db.Column(db.Boolean)
    date = db.Column(db.String(100))
    user_id = db.Column(db.Integer)