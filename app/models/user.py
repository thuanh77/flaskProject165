from app.extensions import db


class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def _init_(self, username, password, email):
        self.username = username
        self.password = password
        self.email=email