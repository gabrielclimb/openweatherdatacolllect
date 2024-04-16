.DEFAULT_GOAL := run-schedule

setup:
	python -m venv .venv && \
	. .venv/bin/activate && $(MAKE) pip-install && \
	pre-commit install

pip-install:
	pip install -U pip && \
	pip install -r requirements.txt

run-scheduler:
	docker compose up

stop-scheduler:
	docker compose down

run-local-ingestion:
	docker compose up -d db migrate && PYTHONPATH=src python -m src.main

run-local-scheduler:
	docker compose up -d db migrate && PYTHONPATH=src python -m src.scheduler

test:
	python -m pytest --cov=src --cov-fail-under=70 tests
