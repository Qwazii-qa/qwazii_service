#!/bin/bash
echo ":::::::Collect static files"
python manage.py collectstatic --noinput

echo ":::::::Run gunicorn"
gunicorn -b 0:8000 -w 2 config.wsgi:application
