.DEFAULT_GOAL := run-ingestion

pip-install:
	pip install -r requirements.txt

run-ingestion:
	PYTHONPATH=src python -m src.main

run-scheduler:
	PYTHONPATH=src python -m src.scheduler
