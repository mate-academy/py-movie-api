import json

from django.test import TestCase

from cinema.models import Movie


class ModelTest(TestCase):
    def test_movie_str(self):
        movie = Movie.objects.create(
            title = "MovieTest",
            description = "MovieTest",
            duration = 50,
        )
        self.assertEqual(str(movie), f"{movie.title} - {movie.duration} minutes")

class ViewTest(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title = "MovieTest",
            description = "MovieTest",
            duration = 50,
        )
    def test_method_get(self):
        url= "http://127.0.0.1:8000/api/cinema/movies/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_method_post(self):
        url= "http://127.0.0.1:8000/api/cinema/movies/"
        data = {"title": "NewMovie", "description": "MovieTest", "duration": 5}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["title"], "NewMovie")

    def test_method_put(self):
        url= f"http://127.0.0.1:8000/api/cinema/movies/{self.movie.id}/"
        data = {"title": "MovieUpdated", "duration": 5}
        response = self.client.put(url, json.dumps(data), content_type="application/json")
        self.assertEqual(response.data["title"], "MovieUpdated")

    def test_method_delete(self):
        url= f"http://127.0.0.1:8000/api/cinema/movies/{self.movie.id}/"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Movie.objects.filter(id=self.movie.id).exists())


