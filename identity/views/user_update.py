from identity import identity
from identity.models.user import User
from identity.decorators.authentication_token_required import authentication_token_required
from core.services import postgres
from flask import jsonify
from flask import request


@identity.route('/user/<int:user_id>', methods=['PATCH'])
@authentication_token_required
def user_update(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify(error='404 Not Found: user not found'), 404

    try:
        email = request.get_json()['data']['email']
        user.email = email
    except KeyError:
        pass

    try:
        user.set_password(request.get_json()['data']['password'])
    except KeyError:
        pass

    postgres.session.commit()
    return jsonify(user=user.serialize()), 200
