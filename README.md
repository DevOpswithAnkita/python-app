# Python Flask App – With /api/docs Route

This is a basic Flask app you can run using:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
gunicorn --bind 0.0.0.0:8000 wsgi:app
