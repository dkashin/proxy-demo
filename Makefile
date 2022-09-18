
CONTAINER = ProxyDemo
HTTP_PORT = 8080

.PHONY: run build restart logs test

run:build
	@echo "Starting docker-compose (up)..."
	HTTP_PORT="$(HTTP_PORT)" docker-compose up --remove-orphans -d $(CONTAINER)
	@echo "$(CONTAINER) started."

build:
	@echo "Building docker image(s)..."
	HTTP_PORT="$(HTTP_PORT)" docker-compose build --force-rm --no-cache $(CONTAINER)
	HTTP_PORT="$(HTTP_PORT)" docker-compose ps "$(CONTAINER)"
	@echo "$(CONTAINER) build."

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

default: run
