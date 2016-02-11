from behave import given, when, then
import requests
import json
import jwt
from core.config import SECRET_KEY

HOST = 'http://localhost:5000'


@given('valid user')
def set_valid_user(context):
    context.user = {
        'data': {
            'email': 'bob@gmail.com',
            'password': '123456'}}


@given('invalid user with wrong password')
def set_invalid_user_wrong_password(context):
    context.invalid_user = {
        'data': {
            'email': 'bob@gmail.com',
            'password': 'FAKE-PASSWORD'}}


@given('invalid user with wrong email')
def set_invalid_user_wrong_email(context):
    context.invalid_user = {
        'data': {
            'email': 'FAKE-EMAIL@gmail.com',
            'password': '123456'}}


@given('invalid user with email only')
def set_invalid_user_email_only(context):
    context.user = {
        'data': {
            'email': 'bob@gmail.com'}}


@given('invalid user with password only')
def set_invalid_user_password_only(context):
    context.user = {
        'data': {
            'password': '123456'}}


@given('valid email')
def set_valid_email(context):
    context.email = {
        'data': {
            'email': 'updated_email@gmail.com'}}


@given('valid password')
def set_valid_password(context):
    context.password = {
        'data': {
            'password': '123456'}}


@when('POST user')
def post_user(context):
    context.response = requests.post(HOST + '/user')
    if context.response.status_code == 200:
        context.token = context.response.json()['token']


@when('register user with email and password')
def register_user(context):
    url = HOST + '/user/register'
    headers = {'content-type': 'application/json',
               'Authorization': 'Bearer ' + context.token}
    data = json.dumps(context.user)
    context.response = requests.patch(url=url,
                                      headers=headers,
                                      data=data)


@when('unauthenticate user with email and password')
def unauthenticate_user(context):
    url = HOST + '/user/unauthenticate'
    headers = {'content-type': 'application/json',
               'Authorization': 'Bearer ' + context.token}
    data = json.dumps(context.user)
    context.response = requests.post(url=url,
                                     headers=headers,
                                     data=data)
    if context.response.status_code == 200:
        context.token = context.response.json()['token']


@when('authenticate user with email and password')
def authenticate_user(context):
    url = HOST + '/user/authenticate'
    headers = {'content-type': 'application/json',
               'Authorization': 'Bearer ' + context.token}
    data = json.dumps(context.user)
    context.response = requests.post(url=url,
                                     headers=headers,
                                     data=data)
    if context.response.status_code == 200:
        context.token = context.response.json()['token']


@when('authenticate invalid user with email and password')
def authenticate_invalid_user(context):
    url = HOST + '/user/authenticate'
    headers = {'content-type': 'application/json',
               'Authorization': 'Bearer ' + context.token}
    data = json.dumps(context.invalid_user)
    context.response = requests.post(url=url,
                                     headers=headers,
                                     data=data)
    if context.response.status_code == 200:
        context.token = context.response.json()['token']


@when('update user email')
def update_user_email(context):
    url = HOST + '/user/' + str(context.response.json()['user']['id'])
    headers = {'content-type': 'application/json',
               'Authorization': 'Bearer ' + context.token}
    data = json.dumps(context.email)
    context.response = requests.patch(url=url,
                                      headers=headers,
                                      data=data)


@when('update user password')
def update_user_password(context):
    url = HOST + '/user/' + str(context.response.json()['user']['id'])
    headers = {'content-type': 'application/json',
               'Authorization': 'Bearer ' + context.token}
    data = json.dumps(context.password)
    context.response = requests.patch(url=url,
                                      headers=headers,
                                      data=data)


@then('response status code is {status_code:d}')
def check_status_code(context, status_code):
    context.response.status_code == status_code


@then('response contains JWT')
def check_jwt(context):
    assert 'token' in context.response.json()


@then('response token scope is {scope}')
def check_anonymous_token(context, scope):
    token = jwt.decode(context.token, SECRET_KEY)
    assert token['scope'] == scope


@then('response not contains JWT')
def check_no_jwt(context):
    assert 'token' not in context.response.json()


@then('response contains user')
def check_user_id(context):
    assert 'user' in context.response.json()
    assert 'id' in context.response.json()['user']
    assert 'email' in context.response.json()['user']


@then('user email is updated')
def check_email_updated(context):
    user_email = context.response.json()['user']['email']
    new_email = context.email['data']['email']
    assert user_email == new_email
