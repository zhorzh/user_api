from flask import Flask
from services import sqlite
from identity import identity

app = Flask(__name__)
app.config.from_object('core.config')
sqlite.app = app
sqlite.init_app(app)
app.register_blueprint(identity)
