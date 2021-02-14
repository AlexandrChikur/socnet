#!/bin/sh

.venv/bin/python3 -m alembic revision --autogenerate
.venv/bin/python3 -m alembic upgrade head
.venv/bin/python3 -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000