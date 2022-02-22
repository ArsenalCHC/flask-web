from database.core import db
from utils.common.data_with_dict import get_data
from database.base_model import Staff


def get_staff_info(staff_login_name: str) -> tuple[str, list[dict]]:
    staff_info = db.session.query(Staff).filter(Staff.login_name == staff_login_name)
    data = get_data(staff_info, 'one')
    return data
