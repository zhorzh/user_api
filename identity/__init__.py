from flask import Blueprint

identity = Blueprint('identity', __name__)

from identity.views import user_create
from identity.views import user_update
from identity.views import user_authenticate
from identity.views import user_unauthenticate
from identity.views import user_register
