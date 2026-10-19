# Movie API

- Read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) before starting.

In this task, you should implement an API that provides CRUD operations for the Movie model.

1. Create a Django project and a `cinema` app inside it.
2. `cinema` should have a `Movie` model that has the following fields:
    * `title` - a film title
    * `description` - a film description
    * `duration` - a film duration in minutes
3. Implement a serializer for this model.
4. Create api views for the following endpoints:
    * `GET api/cinema/movies/` - should return a list of the all movies
    * `GET api/cinema/movies/<pk>/` - should return a movie with given id 
    * `POST api/cinema/movies/` - should create a new movie based on passed data
    * `PUT api/cinema/movies/<pk>/` - should update the movie with given id based on passed data
    * `DELETE api/cinema/movies/<pk>/` - should delete the movie with given id

Use the following command to load prepared data from fixture to test and debug your code:

  `python manage.py loaddata cinema_service_db_data.json`


### Note: Check your code using this [checklist](checklist.md) before pushing your solution.

## Run the API

Requires Python 3.12 or newer.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
python manage.py migrate
python manage.py loaddata cinema_service_db_data.json
python manage.py runserver
```

Open http://127.0.0.1:8000/api/cinema/movies/ to use the DRF browsable API,
or send requests with `Content-Type: application/json`.

| Method | URL | Success |
| --- | --- | --- |
| GET | /api/cinema/movies/ | 200, list of movies |
| POST | /api/cinema/movies/ | 201, created movie |
| GET | /api/cinema/movies/1/ | 200, movie details |
| PUT | /api/cinema/movies/1/ | 200, updated movie |
| DELETE | /api/cinema/movies/1/ | 204, empty response |

POST and PUT require `title` (up to 255 characters), `description`, and
`duration` (a positive integer in minutes). The movie `id` is read-only.
PUT replaces all editable fields. Invalid input returns 400; missing movies
return 404; unsupported methods return 405.

Example request body:

```json
{
  "title": "Inception",
  "description": "A team enters shared dreams.",
  "duration": 148
}
```

This learning API allows anonymous CRUD requests. Local development uses SQLite.
For another environment, set `DJANGO_SECRET_KEY`, `DJANGO_DEBUG=0`, and
`DJANGO_ALLOWED_HOSTS` (comma-separated hostnames).

## Verification

```bash
flake8
python manage.py check
python manage.py makemigrations --check --dry-run
python manage.py test
```

The 14 API tests cover CRUD persistence and responses, validation, read-only IDs,
full PUT updates, missing records, unsupported methods, malformed JSON, and the
supplied fixture. GitHub Actions runs these checks on Python 3.12.

The checklist requires a final blank line; flake8 W391 is excluded so that this
repository-specific rule can be followed. Double quotes are checked with
flake8-quotes.
