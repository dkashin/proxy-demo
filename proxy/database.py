
'''
SQLAlchemy database structure init

db_session: variable contains sessions scope.
'''

import os

from sqlalchemy import create_engine, event
from sqlalchemy.engine import Engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from .config import app_config

try:
    os.mkdir(app_config.DB_DIR)
except OSError as error:
    pass

engine = create_engine(app_config.SQLALCHEMY_DATABASE_URI, convert_unicode = True)
db_session = scoped_session(sessionmaker(autocommit = False, autoflush = False, bind = engine))
Base = declarative_base()
Base.query = db_session.query_property()


# DB init
def db_init(app):
    '''
    Database init.

    Creating DB structure in a declarative way using Base class metadata.
    Removing session scope on app shutdown.

    Arguments:
        - app: Flask app
    '''
    with app.app_context():
        import proxy.models
        Base.metadata.create_all(bind = engine)

    # Remove scoped session on app shutdown
    @app.teardown_appcontext
    def shutdown_session(exception = None):
        db_session.remove()

    return


@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    '''
    Tuning SQLite3 database.
    Definig custom PRAGMA settings on connect.
    '''
    cursor = dbapi_connection.cursor()
#  cursor.execute("PRAGMA foreign_keys = ON")
    cursor.execute("PRAGMA page_size = 4096")
    cursor.execute("PRAGMA cache_size = 20000")
    cursor.execute("PRAGMA temp_store = MEMORY")
    cursor.execute("PRAGMA synchronous = NORMAL")
    cursor.execute("PRAGMA journal_mode = WAL")
    cursor.close()
