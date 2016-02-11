import jwt
from functools import wraps
from flask import request
from flask import jsonify
from core.config import SECRET_KEY


def anonymous_token_required(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        # check authentication header
        if not request.headers.get('Authorization'):
            return jsonify(error='No authorization header')

        header = request.headers.get('Authorization')

        if not header.split()[0] == 'Bearer':
            return jsonify(error='No Bearer token')
        elif not len(header.split()) == 2:
            return jsonify(error='Invalid token')

        # verify access token
        token = header.split()[1]
        try:
            payload = jwt.decode(token, SECRET_KEY)
        except jwt.DecodeError:
            return jsonify(error='JWT is not valid')

        # verify authorization scope
        if not payload['scope'] == 'anonymous':
            return jsonify(error=payload['scope'])

        # return initial function
        return function(*args, **kwargs)

    return wrapper
