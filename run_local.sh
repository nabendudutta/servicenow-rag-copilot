#!/bin/bash

echo "Starting ServiceNow Copilot..."

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

echo "Starting API..."
uvicorn api.app:app --port 8000