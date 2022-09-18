
import os
from . import __file__

'''
Application configuration.
'''

class AppConfig(object):

    # Flask debug mode enable/disable
    FLASK_DEBUG = True

    # JWT algorithm
    JWT_ALGORITHM = 'HS512'
    # JWT secret key
    JWT_SECRET_KEY = 'a9ddbcaba8c0ac1a0a812dc0c2f08514b23f2db0a68343cb8199ebb38a6d91e4ebfb378e22ad39c2d01d0b4ec9c34aa91056862ddace3fbbd6852ee60c36acbf'
    # Upstream URL
    UPSTREAM_URL = 'http://localhost:8080/api/v1/echo'

    # App root path
    APP_ROOT = os.path.join(os.path.abspath(os.path.dirname(__file__)), os.path.pardir)
    # App root parent dir
    SYSTEM_ROOT = os.path.join(APP_ROOT, os.path.pardir)

    # Database dir
    DB_DIR = os.path.join(SYSTEM_ROOT, 'db')
    # Database name
    DB_NAME = 'proxy.db'
    # Database URL
    SQLALCHEMY_DATABASE_URI = os.path.join(f"sqlite:///{DB_DIR}", DB_NAME)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Log dir name
    LOG_DIR_NAME = 'logs'
    # Logs file extension
    LOG_FILE_EXT = '.log'
    # Logs dir
    LOG_DIR_ROOT = os.path.join(SYSTEM_ROOT, LOG_DIR_NAME)
    # System log file
    LOG_FILE_SYSTEM = os.path.join(LOG_DIR_ROOT, f'system{LOG_FILE_EXT}')
    # Database log file
    LOG_FILE_DB = os.path.join(LOG_DIR_ROOT, f'db{LOG_FILE_EXT}')
    # Log files max size
    LOG_SIZE_MAX = 10 * 1024 * 1024
    # Log debug level, 10 = DEBUG, 20 = INFO
    LOG_LEVEL = 10


app_config = AppConfig()

