from flask import Blueprint
from service.service_staff import get_staff_info
from utils.http.response import ResMsg

test_bp = Blueprint("test", __name__, url_prefix='/test')


@test_bp.route('/', methods=["GET"])
def test():
    res = ResMsg()
    response, data = get_staff_info('root')
    res.update(code=response, data=data)
    return res.data
