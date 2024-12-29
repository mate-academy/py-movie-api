rw# Movie API

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
