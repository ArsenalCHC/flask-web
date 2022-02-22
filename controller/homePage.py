from flask import Blueprint
from service.service_staff import get_staff_info
from utils.http.response import ResMsg

home_bp = Blueprint("home", __name__, url_prefix='/')


@home_bp.route('/', methods=["GET"])
def home():
    res = ResMsg()
    response, data = get_staff_info('root')
    res.update(code=response, data=data)
    return res.data
