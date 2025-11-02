SHELL := /bin/bash

.PHONY: up down build rebuild logs status clean init-db pipeline quickstart demo

up:
	docker compose up -d

down:
	docker compose down

build:
	docker compose build

rebuild:
	docker compose build --no-cache

logs:
	docker compose logs -f --tail=200

status:
	docker compose ps

clean:
	docker compose down -v --remove-orphans || true
	docker system prune -f || true

init-db:
	# create DB schema inside API container (uses src/db/init_schema.py)
	docker compose exec api python -m src.db.init_schema

pipeline:
	# placeholder for your end-to-end run (ingest -> topics -> forecast etc.)
	docker compose exec api python -m src.ingestion.ingest_data

quickstart: build up
	@echo "Waiting 10s for core services..."
	sleep 10
	$(MAKE) init-db
	$(MAKE) pipeline
	@echo "✅ Quickstart complete: API on :8000, Streamlit on :8501, MLflow on :5000"

demo:
	# simple smoke tests: hit API health and topics
	curl -s http://localhost:8000/health || true
	curl -s 'http://localhost:8000/topics?limit=5' || true
