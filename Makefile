
CONTAINER = ProxyDemo

.PHONY: build start stop restart logs test

build:
	@echo "Building docker image(s)..."
	docker-compose build --force-rm --no-cache $(CONTAINER)
	docker-compose ps $(CONTAINER)
	@echo "$(CONTAINER) build."

start:
	@echo "Starting docker-compose (up)..."
	docker-compose up --remove-orphans -d $(CONTAINER)
	@echo "$(CONTAINER) started."

stop:
	@echo "Stopping docker-compose (down)..."
	docker-compose down
	@echo "$(CONTAINER) stopped."

restart:
	@echo "Restarting docker-compose..."
	docker-compose restart $(CONTAINER)
	docker-compose ps $(CONTAINER)
	@echo "$(CONTAINER) restarted."

logs:
	@echo "Displaying $(CONTAINER) logs..."
	docker-compose logs --tail 0 -f $(CONTAINER)

test:
	@echo "Installing Python requirements..."
	python3 -m pip install -r requirements.txt >/dev/null
	@echo "Starting $(CONTAINER) unittests..."
	python3 -m unittest tests/test_*
	@echo "$(CONTAINER) tests completed."

default: start
