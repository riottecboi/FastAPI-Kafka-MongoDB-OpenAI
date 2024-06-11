# Set the Python environment variables
PYTHON_ENV=venv
PYTHON=$(PYTHON_ENV)/bin/python
PIP=$(PYTHON_ENV)/bin/pip

# Set the project variables
PROJECT_NAME=FastAPI-Kafka-MongoDB-OpenAI
MAIN_FILE=main.py

# Set the Docker variables
DOCKER_IMAGE=Dockerfile
DOCKER_COMPOSE=docker-compose

# Create a virtual environment
$(PYTHON_ENV):
	python3 -m venv $(PYTHON_ENV)

# Install dependencies
install: $(PYTHON_ENV)
	$(PIP) install -r requirements.txt

# Run the FastAPI application locally
run:
	$(PYTHON) $(MAIN_FILE)

# Run tests
test:
	$(PYTHON) -m pytest tests/

# Build the Docker image
build:
	docker build -t $(DOCKER_IMAGE) .

# Run the Docker containers
up:
	$(DOCKER_COMPOSE) up -d

# Stop the Docker containers
down:
	$(DOCKER_COMPOSE) down

# Clean up (remove virtual environment, build files, etc.)
clean:
	rm -rf $(PYTHON_ENV) build dist *.egg-info

# Set up the project (create virtual environment and install dependencies)
setup: $(PYTHON_ENV) install

# Set up the project and run the application
start: setup run

# Set up the project, run tests, and start the application
ci: setup test run

# Set up the project, run tests, and start the Docker containers
docker: setup test build up