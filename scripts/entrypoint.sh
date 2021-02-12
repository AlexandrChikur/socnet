#!/bin/sh

.venv/bin/python3 -m uvicorn app.main:app --reload --host 0.0.0.0 --port $PORT