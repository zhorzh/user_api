from core.services import sqlite
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash


class User(sqlite.Model):
    id = sqlite.Column(sqlite.Integer, primary_key=True)
    email = sqlite.Column(sqlite.Text, default=None, unique=True)
    password = sqlite.Column(sqlite.Text, default=None)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def serialize(self):
        return dict(id=self.id,
                    email=self.email,
                    password=self.password)
