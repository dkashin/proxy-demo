
'''
app: Main app variable.
Local testing/debug server setup.
'''

import os

from .app import create_app
from .config import app_config

app = create_app()

# Local server setup. Debug/testing only.
if __name__ == '__main__':
	app.run(host = 'localhost', port = app_config.HTTP_PORT_TEST, debug = True)
