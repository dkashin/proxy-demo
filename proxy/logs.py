
'''
Logging management and logger scope init.
'''

import os, logging

from logging import Formatter, NullHandler, FileHandler
from logging.handlers import RotatingFileHandler

from .config import app_config


# Log manager class
class LogManager(object):
    '''
    Logging management allows to manage system logs in a simple way.
    '''
    def __init__(self, app_config):
        self.app_config = app_config

    def LogNull(self):
        '''
        Creates null logger.
        Returns:
            - logging object
        '''
        try:
            logger = logging.getLogger()
            logger.setLevel(self.app_config.LOG_LEVEL)
            logger.addHandler(NullHandler())
        except:
            logger = None
            print(f'[LogManager] LogNull: Excepion error')
        return logger

    def LogOpen(self, area, log_file):
        '''
        Creates a logger with pre-defined format and file handler settings.
        Arguments:
            - area: <string> class/function/scope where to collect log from
            - log_file: <string> log file path
        Returns:
            - logging object
        '''
        try:
            logger = logging.getLogger(area)
            if not logger.handlers:
                logger.setLevel(self.app_config.LOG_LEVEL)
                formatter = Formatter('%(asctime)s [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
                handler = FileHandler(log_file, mode = 'a')
                handler.setFormatter(formatter)
                logger.addHandler(handler)
        except:
            logger = self.LogNull()
            print(f'[LogManager] LogOpen: Excepion error')
        return logger


# App logging init
def logger_init(app_config, logger_scope):
    '''
    System wide logger init.

    logger_null: null logger, <getLogger() object>
    logger_system: Logger for system events, <getLogger() object>
    logger_db: Logger for database events, <getLogger() object>

    Arguments:
        - app_config: AppConfig() object
        - logger_scope: loggers scope dict
    Returns:
        - logger_scope: loggers scope dict
    '''
    _LogManager = LogManager(app_config)
    # Null logger
    logger_null = _LogManager.LogNull()
    # System logger
    logger_system = _LogManager.LogOpen('system', app_config.LOG_FILE_SYSTEM)
    # DB logger
    logger_db = _LogManager.LogOpen('sqlalchemy', app_config.LOG_FILE_DB)
    LL = { 10: 'DEBUG', 20: 'INFO' }
    try:
        logger_system.info(f'[SystemInit] Flask debug: {app_config.FLASK_DEBUG}')
    except:
        logger_system.info(f'[SystemInit] Flask debug: False')
    logger_system.info(f'[SystemInit] Log level: {LL.get(app_config.LOG_LEVEL)}')
    logger_scope = {
        'null': logger_null,
        'system': logger_system,
        'db': logger_db
    }
    return logger_scope


# Check and create log dir(s)
try:
    os.mkdir(app_config.LOG_DIR_ROOT)
except OSError as error:
    pass

# Init logger scope
logger_scope = logger_init(app_config, {})
logger_system = logger_scope.get('system')

