
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
	HTTP_PORT = os.environ.get('HTTP_PORT') or 8077
	os.environ['ENV'] = 'development'
	app.run(host = 'localhost', port = HTTP_PORT, debug = True)
