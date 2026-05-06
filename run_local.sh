#!/bin/bash

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

echo "Starting API..."
uvicorn api.app:app --reload --port 8000