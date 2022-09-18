from .app import create_app

app = create_app()

# Only for debugging while developing
if __name__ == "__main__":
	app.run(host = "localhost", port = 8080, debug = True)
