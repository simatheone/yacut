import os
import string

VALID_SYMBOLS = string.ascii_letters + string.digits
SYMBOLS_LENGTH = 6
USER_INPUT_LIMIT = 16


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')
