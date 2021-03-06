from core.config import SECRET_KEY
from identity import identity
from identity.models.user import User
from identity.decorators.anonymous_token_required import anonymous_token_required
from flask import jsonify
from flask import request
import jwt


@identity.route('/user/authenticate', methods=['POST'])
@anonymous_token_required
def user_authenticate():
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
                        'scope': 'authenticated'},
                       SECRET_KEY)
    return jsonify(token=token, user=user.serialize()), 200
