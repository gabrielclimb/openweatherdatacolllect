.DEFAULT_GOAL := run-ingestion

pip-install:
	pip install -r requirements.txt

run-ingestion:
	PYTHONPATH=src python -m src.main

run-scheduler:
	PYTHONPATH=src python -m src.scheduler

test:
	python -m pytest --cov=src --cov-fail-under=70 tests
