
CONTAINER = ProxyDemo
HTTP_PORT = 8080

.PHONY: build start stop restart logs test

build:
	@echo "Building docker image(s)..."
	docker-compose build --force-rm --no-cache $(CONTAINER)
	docker-compose ps $(CONTAINER)
	@echo "$(CONTAINER) build."

start:build
	@echo "Starting docker-compose (up)..."
	HTTP_PORT="$(HTTP_PORT)" docker-compose up --remove-orphans -d $(CONTAINER)
	@echo "$(CONTAINER) started."

stop:
	@echo "Stopping docker-compose (down)..."
	HTTP_PORT="$(HTTP_PORT)" docker-compose down
	@echo "$(CONTAINER) stopped."

restart:
	@echo "Restarting docker-compose..."
	HTTP_PORT="$(HTTP_PORT)" docker-compose restart $(CONTAINER)
	HTTP_PORT="$(HTTP_PORT)" docker-compose ps $(CONTAINER)
	@echo "$(CONTAINER) restarted."

logs:
	@echo "Displaying $(CONTAINER) logs..."
	HTTP_PORT="$(HTTP_PORT)" docker-compose logs --tail 0 -f $(CONTAINER)

test:
	@echo "Installing Python requirements..."
	python3 -m pip install -r requirements.txt >/dev/null
	@echo "Starting $(CONTAINER) unittests..."
	python3 -m unittest tests/test_*
	@echo "$(CONTAINER) tests completed."

default: start
