from . import db, bcrypt


class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(100), unique=True)
    name = db.Column(db.String(100))
    appealName = db.Column(db.String(100))
    password = db.Column(db.String(100))

    def add_user(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all_users():
        return User.query.all()

    def update_user_info(self, data):
        # for key, item in data.items():
        #     if key == 'password':
        #         self.password = self.__generate_hash(item)
        #     setattr(self, key, item)
        #
        for key, value in data.items():
            if key == 'name':
                self.name = value
            if key == 'appeal_name':
                self.appealName = value
            if key == 'password':
                self.password = User.generate_hashed_password(value)
        db.session.commit()

    def delete_user(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_user_by_name(value):
        return User.query.filter_by(name=value).first()

    @staticmethod
    def get_one_user(id):
        return User.query.filter_by(id=id).first()

    def generate_hashed_password(password):
        return bcrypt.generate_password_hash(password, rounds=10).decode("utf-8")

    def check_hashed_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

