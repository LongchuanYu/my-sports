import jwt
from flask import g, current_app
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from app.models import User, MyData
from app.error import error_response


basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()

@basic_auth.verify_password
def verify_password(username, password):
    print(username ,password)
    user = User.query.filter_by(username=username).first()
    if user is None:
        return False
    g.current_user = user
    return user.check_password(password)

@basic_auth.error_handler
def basic_auth_error():
    return error_response(401)

@token_auth.verify_token
def verify_token(token):
    if not token:
        return None
    try:
        payload = jwt.decode(
            token,
            current_app.config['SECRET_KEY'],
            algorithms=['HS256']
        )
    except (jwt.exceptions.ExpiredSignatureError, jwt.exceptions.InvalidSignatureError) as e:
        return False
    g.current_user = User.query.get(payload.get('user_id')) if token else None
    return g.current_user is not None

@token_auth.error_handler
def token_auth_error():
    return error_response(401)