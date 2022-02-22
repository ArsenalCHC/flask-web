from utils.decorator.auth import generate_auth_token, get_token_user
import base64
import re
from database.core import Redis
from utils.http.code import ResponseCode
from service.service_staff import get_staff_info


def login(authorization: str) -> dict:
    return_dict = {}
    pre_auth = re.compile('^Basic.*')
    if pre_auth.match(authorization):
        auth = authorization.split(' ')[1]
        username = base64.b64decode(auth).decode().split(':')[0]
        token = generate_auth_token(username).decode()
        response, data = get_staff_info(username)
        return_dict["staff_info"] = data
        return_dict["token"] = token
        return_dict["response"] = response
        Redis.hset('login', username, token)
        return return_dict


def logout(authorization: str):
    pre_auth = re.compile('^Bearer.*')
    if pre_auth.match(authorization):
        auth = authorization.split(' ')[1]
        username = get_token_user(auth)
        Redis.hdel('login', username)
        return ResponseCode.Success
