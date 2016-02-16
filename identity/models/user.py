from core.services import postgres
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash


class User(postgres.Model):
    id = postgres.Column(postgres.Integer, primary_key=True)
    email = postgres.Column(postgres.Text, default=None, unique=True)
    password = postgres.Column(postgres.Text, default=None)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def serialize(self):
        return dict(id=self.id,
                    email=self.email,
                    password=self.password)
