
'''
Create and init main app
'''

from flask import Flask

from .config import app_config
from .database import db_init

import proxy.proxy_jwt, os


def create_app():
	'''
	Flask app creation and init.

	Returns:
        - app: Flask app
	'''
	app = Flask(__name__)
	app.config.from_object(app_config)
	db_init(app)
	register_blueprints(app)

	return app


def register_blueprints(app):
	'''
	Register Flask blueprints.

	url_prefix: <string> could be used for API versions.
	'''
	url_prefix = '/api/v1'
	app.register_blueprint(proxy.proxy_jwt.views.blueprint, url_prefix = url_prefix)
	return
