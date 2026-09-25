from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from cinema.models import Movie


class MovieAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        Movie.objects.create(title="Harry Potter",
                             description="long film",
                             duration=150)
        Movie.objects.create(title="Lord of Rings",
                             description="superb film",
                             duration=200, )

    def test_get_movies(self):
        response = self.client.get("/api/cinema/movies/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        movies_title = [movie["title"] for movie in response.data]
        self.assertEqual(movies_title,
                         ["Harry Potter",
                          "Lord of Rings"])

    def test_post_movies(self):
        response = self.client.post("/api/cinema/movies/",
                                    {"title": "Matrix",
                                     "description": "top1",
                                     "duration": 200})

        movies = Movie.objects.all()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(movies.count(), 3)
        self.assertEqual(movies.filter(title="Matrix").count(), 1)

    def test_get_invalid_movie(self):
        response = self.client.get("/api/cinema/movies/1000/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_put_movies(self):
        response = self.client.put("/api/cinema/movies/1/",
                                   {"title": "Harry Potter 2",
                                    })
        movie = Movie.objects.get(pk=1)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(movie.title, "Harry Potter 2")

    def test_delete_movies(self):
        response = self.client.delete("/api/cinema/movies/1/")
        movie = Movie.objects.filter(pk=1)

        self.assertEqual(movie.count(), 0)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_invalid_movies(self):
        response = self.client.delete("/api/cinema/movies/1000/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_post_duration_below_minimum(self):
        response = self.client.post("/api/cinema/movies/",
                                    {"title": "Matrix",
                                     "description": "top1",
                                     "duration": 0})

        movies = Movie.objects.all()

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(movies.count(), 2)
        self.assertIn("duration", response.data)

    def test_post_duration_at_minimum(self):
        response = self.client.post("/api/cinema/movies/",
                                    {"title": "Matrix",
                                     "description": "top1",
                                     "duration": 1})

        movies = Movie.objects.all()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(movies.count(), 3)
        self.assertEqual(movies.get(title="Matrix").duration, 1)

    def test_post_duration_at_maximum(self):
        response = self.client.post("/api/cinema/movies/",
                                    {"title": "Matrix",
                                     "description": "top1",
                                     "duration": 300})

        movies = Movie.objects.all()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(movies.count(), 3)
        self.assertEqual(movies.get(title="Matrix").duration, 300)

    def test_post_duration_above_maximum(self):
        response = self.client.post("/api/cinema/movies/",
                                    {"title": "Matrix",
                                     "description": "top1",
                                     "duration": 301})

        movies = Movie.objects.all()

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(movies.count(), 2)
        self.assertIn("duration", response.data)
