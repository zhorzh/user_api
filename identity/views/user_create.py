from core.config import SECRET_KEY
from identity import identity
from models import User
from core.services import sqlite
from flask import jsonify
import jwt


@identity.route('/user', methods=['POST'])
def user_create():
    user = User()
    sqlite.session.add(user)
    sqlite.session.commit()

    token = jwt.encode({'user_id': user.id,
                        'scope': 'anonymous'},
                       SECRET_KEY)
    return jsonify(token=token), 200
