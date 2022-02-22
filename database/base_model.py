from database.core import db
import datetime


class PubCol(db.Model):
    """
    base表基类，用于定义部分公共字段
    """
    __abstract__ = True
    create_time = db.Column(db.DateTime, default=datetime.datetime.now(), nullable=True)
    modify_time = db.Column(db.DateTime, nullable=True)
    is_delete = db.Column(db.String(1), default=0, nullable=True)
    delete_time = db.Column(db.DateTime, nullable=True)


class Staff(PubCol):
    """
    员工信息表
    """
    __tablename__ = 'base_staff'
    id = db.Column(db.Integer, primary_key=True)
    staff_code = db.Column(db.String(25), unique=True)
    staff_name = db.Column(db.String(25))
    login_name = db.Column(db.String(25), unique=True)
    password = db.Column(db.String(150))
    is_admin = db.Column(db.String(1), default=0, nullable=True)
    is_activate = db.Column(db.String(1), default=0, nullable=True)


class Dept(PubCol):
    """
    部门信息表
    """
    __tablename__ = 'base_dept'
    id = db.Column(db.Integer, primary_key=True)
    dept_name = db.Column(db.String(25))
    parent_dept_id = db.Column(db.Integer)

