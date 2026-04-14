<!-- @format -->

# Create Django project

django-admin startproject movie_project .

cd movie_project

# Create cinema app

python manage.py startapp cinema

# Create and Run Migrations

cd cinema

create migrations/**init**.py

## Create initial migration

python manage.py makemigrations

## Apply migrations

python manage.py migrate

# Install Requirements

pip install django djangorestframework

# Load Fixture Data

python manage.py loaddata cinema_service_db_data.json

# Run the Server

python manage.py runserver --noreload

# API Endpoints Testing:

## GET all movies

curl -X GET http://localhost:8000/api/cinema/movies/

## GET single movie

curl -X GET http://localhost:8000/api/cinema/movies/1/

## POST create movie

curl -X POST http://localhost:8000/api/cinema/movies/ \
 -H "Content-Type: application/json" \
 -d '{"title":"Inception","description":"A dream within a dream","duration":148}'

## PUT update movie

curl -X PUT http://localhost:8000/api/cinema/movies/1/ \
 -H "Content-Type: application/json" \
 -d '{"title":"Updated Title","description":"New description","duration":120}'

## DELETE movie

curl -X DELETE http://localhost:8000/api/cinema/movies/1/
