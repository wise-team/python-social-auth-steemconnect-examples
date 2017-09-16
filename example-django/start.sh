#!/bin/sh
python manage.py migrate
/usr/local/bin/uwsgi --http :5000 \
    --wsgi-file /app/example/wsgi.py \
    --master \
    --processes 3 \
    --chdir /app \
    --harakiri 120 \
    --stats :1717 \
    --enable-threads \
    --single-interpreter \
    --max-requests 5000 \
    --static-map /static=/app/common/static

