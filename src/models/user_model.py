

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(100), unique=True)
    name = db.Column(db.String(100))
    appealName = db.Column(db.String(100))
    password = db.Column(db.String(100))