from identity import identity
from models import User
from core.services import sqlite
from flask import jsonify
from flask import request


@identity.route('/user/<int:user_id>', methods=['PATCH'])
def user_update(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify(error='404 Not Found: user not found'), 404

    try:
        user.email = request.get_json()['data']['email']
    except KeyError:
        pass

    try:
        user.set_password(request.get_json()['data']['password'])
    except KeyError:
        pass

    sqlite.session.commit()
    return jsonify(user=user.serialize()), 200
