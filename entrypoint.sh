#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi
cd /home/app/backend
pip install -r requirements.txt
python manage.py collectstatic --no-input --clear

python manage.py migrate 

echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@gmail.com', 'admin')" | python manage.py shell

exec "$@"