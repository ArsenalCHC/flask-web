from flask import request, Blueprint
from utils.decorator.auth import basic_auth, token_auth
from utils.http.response import ResMsg
from service.service_auth import login, logout

auth_bp = Blueprint("auth", __name__, url_prefix='/auth')


@auth_bp.route('/login', methods=["POST"])
@basic_auth.login_required()
def auth_login():
    res = ResMsg()
    auth = request.headers.get('Authorization')
    data = login(auth)
    res.add_field(name='token', value=data["token"])
    res.update(code=data["response"], data=data["staff_info"])
    return res.data


@auth_bp.route('/logout', methods=["POST"])
@token_auth.login_required()
def auth_logout():
    res = ResMsg()
    auth = request.headers.get('Authorization')
    code = logout(auth)
    res.update(code=code)
    return res.data
