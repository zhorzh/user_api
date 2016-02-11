import jwt
from flask import jsonify
from flask import request
from core.config import SECRET_KEY
from identity import identity
from identity.decorators.authentication_token_required import authentication_token_required
from identity.models.user import User


@identity.route('/user/unauthenticate', methods=['POST'])
@authentication_token_required
def user_unauthenticate():
    try:
        email = request.get_json()['data']['email']
    except KeyError:
        return jsonify(error='422 Unprocessable Entity: no email'), 422

    try:
        password = request.get_json()['data']['password']
    except KeyError:
        return jsonify(error='422 Unprocessable Entity: no password'), 422

    user = User.query.filter_by(email=email).first()
    if not user or not user.check_password(password):
        return jsonify(error='404 Not Found: user not found'), 404

    token = jwt.encode({'user_id': user.id,
                        'scope': 'anonymous'},
                       SECRET_KEY)
    return jsonify(token=token, user=user.serialize()), 200
