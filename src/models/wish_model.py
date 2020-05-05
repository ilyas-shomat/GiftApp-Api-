from . import db
from  sqlalchemy.sql.expression import func, select
import random
from sqlalchemy.sql import func
from sqlalchemy.orm import load_only

class Wish(db.Model):

    __tablename__ = 'wishes'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(10000))
    like = db.Column(db.Boolean)
    date = db.Column(db.String(100))
    user_id = db.Column(db.Integer)

    def add_wish(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all_wishes():

        return Wish.query.all()

    @staticmethod
    def get_wish_by_id(id):
        return Wish.query.filter_by(id=id).first()

    def update_wish_data(self, data):

        for key, value in data.items():
            if key == 'text':
                self.text = value
            if key == 'date':
                self.date = value
        db.session.commit()

    def delete_wish(self):

        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_random_wish():
        return random.choice(Wish.query.all())
