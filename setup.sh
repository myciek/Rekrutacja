#!/bin/sh

docker-compose build
docker-compose run web python manage.py makemigrations exams
docker-compose run web python manage.py migrate
docker-compose run web python manage.py create_data
docker-compose run web python manage.py test