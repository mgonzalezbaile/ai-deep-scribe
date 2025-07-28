build:
	docker-compose build

run:
	docker-compose up --build

test:
	docker-compose run --rm api /app/.venv/bin/python -m pytest tests/
