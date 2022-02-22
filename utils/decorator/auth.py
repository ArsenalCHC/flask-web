from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth, MultiAuth
from database.core import db, Redis
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired
from flask import current_app
from utils.http.response import ResMsg
from utils.http.code import ResponseCode
from database.base_model import Staff

basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth('Bearer')
multi_auth = MultiAuth(basic_auth, token_auth)


def generate_auth_token(username_in: str, expiration=650):
    s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
    return s.dumps({'id': username_in})


@basic_auth.verify_password
def verify_password(username: str, password: str):
    staff_info = db.session.query(Staff).filter(Staff.login_name == username).first()
    if staff_info:
        passwd = staff_info.password
        if password == passwd:
            return True
        else:
            return False
    else:
        return False


@token_auth.verify_token
def verify_token(token: str):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
        username = data['id']
        auth_token = Redis.hget('login', username)
        if auth_token == token:
            return True
        else:
            return False
    except BadSignature:
        # AuthFailed 自定义的异常类型
        return False
    except SignatureExpired:
        return False


@basic_auth.error_handler
def basic_err():
    res = ResMsg()
    res.update(code=ResponseCode.AccountOrPassWordErr)
    return res.data


@token_auth.error_handler
def token_err():
    res = ResMsg()
    res.update(code=ResponseCode.AccountOrPassWordErr)
    return res.data


def get_token_user(token: str):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
        username = data['id']
        return username
    except BadSignature:
        # AuthFailed 自定义的异常类型
        return False
    except SignatureExpired:
        return False
