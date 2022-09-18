
'''
app: Main app variable.
Local testing/debug server setup.
'''

from .app import create_app

app = create_app()

# Local server setup. Only for debug and testing.
if __name__ == "__main__":
	app.run(host = "localhost", port = 8080, debug = True)
