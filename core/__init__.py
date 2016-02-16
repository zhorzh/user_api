from flask import Flask
from services import postgres
from identity import identity

app = Flask(__name__)
app.config.from_object('core.config')
postgres.app = app
postgres.init_app(app)
app.register_blueprint(identity)
