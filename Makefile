.DEFAULT_GOAL := run-ingestion

pip-install:
	pip install -r requirements.txt

run-scheduler:
	docker compose up

run-local-ingestion:
	docker compose up -d db migrate && PYTHONPATH=src python -m src.main

run-local-scheduler:
	docker compose up -d db migrate && PYTHONPATH=src python -m src.scheduler

test:
	python -m pytest --cov=src --cov-fail-under=70 tests
