from core.config import SECRET_KEY
from identity import identity
from models import User
from core.services import sqlite
from flask import jsonify
from flask import request
import jwt


@identity.route('/user/register', methods=['PATCH'])
def user_register():
    header = request.headers.get('Authorization')
    token = header.split()[1]

    user_id = jwt.decode(token, SECRET_KEY)['user_id']
    user = User.query.get(user_id)
    if not user:
        return jsonify(error='404 Not Found: user not found'), 404

    try:
        user.email = request.get_json()['data']['email']
    except KeyError:
        return jsonify(error='422 Unprocessable Entity: no email'), 422

    try:
        user.set_password(request.get_json()['data']['password'])
    except KeyError:
        return jsonify(error='422 Unprocessable Entity: no password'), 422

    sqlite.session.commit()

    token = jwt.encode({'user_id': user.id,
                        'scope': 'authenticated'},
                       SECRET_KEY)
    return jsonify(token=token, user=user.serialize()), 200
