# FoodExpress - Python Flask Food Ordering Website

A food ordering application built with Python Flask and deployed using Jenkins to a separate target EC2 server.

## Run locally
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py

Open http://localhost:5000

## Test
pytest -q

## Production
gunicorn --bind 0.0.0.0:5000 app:app
