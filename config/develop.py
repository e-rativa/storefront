import os

class Config(object):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = f"sqlite:///auth.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PROPAGATE_EXCEPTIONS = True
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    ORDER_TOPIC = 'nuevas-ordenes'
    BROKER_URL = 'localhost'


class Test(object):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = f"sqlite:///auth_test.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PROPAGATE_EXCEPTIONS = True
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024