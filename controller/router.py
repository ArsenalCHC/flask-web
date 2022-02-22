from controller.test import test_bp
from controller.auth import auth_bp
from controller.homePage import home_bp

router = [
    test_bp,
    auth_bp,
    home_bp
]
