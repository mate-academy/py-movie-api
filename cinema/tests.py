from django.test import TestCase

from rest_framework.test import APIClient
from rest_framework import status

from cinema.serializers import MovieSerializer
from cinema.models import Movie


class MovieApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        Movie.objects.create(
            title="test_title1",
            description="Test description 1",
            duration=120,
        )
        Movie.objects.create(
            title="test_title2",
            description="Test description 2",
            duration=240,
        )

    def test_get_movies(self):
        movies = self.client.get("/cinema/movies/")
        serializer = MovieSerializer(Movie.objects.all(), many=True)
        self.assertEqual(movies.status_code, status.HTTP_200_OK)
        self.assertEqual(movies.data, serializer.data)

    def test_post_movies(self):
        response = self.client.post(
            "/cinema/movies/",
            {
                "title": "test_title3",
                "description": "Test description 3",
                "duration": 360,
            },
        )
        movies = Movie.objects.all()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(movies.count(), 3)
        self.assertTrue(movies.filter(title="test_title3").exists())

    def test_post_invalid_movies(self):
        response = self.client.post(
            "/cinema/movies/",
            {
                "title": "test_title3",
                "description": "Test description 3",
                "duration": "wrong_duration",
            },
        )
        movies = Movie.objects.filter(title="test_title3")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(movies.count(), 0)

    def test_get_movie_detail(self):
        response = self.client.get("/cinema/movies/1/")
        serializer = MovieSerializer(
            Movie(
                id=1,
                title="test_title1",
                description="Test description 1",
                duration=120,
            )
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_invalid_movie_detail(self):
        response = self.client.get("/cinema/movies/10/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_put_movie_detail(self):
        self.client.put(
            "/cinema/movies/1/",
            {
                "title": "test_title3",
                "description": "Test description 3",
                "duration": 360,
            },
        )
        movie = Movie.objects.get(id=1)
        self.assertEqual(movie.title, "test_title3")
        self.assertEqual(movie.description, "Test description 3")
        self.assertEqual(movie.duration, 360)

    def test_put_invalid_movie_detail(self):
        response = self.client.put(
            "/cinema/movies/1/",
            {
                "title": "test_title3",
                "description": "Test description 3",
                "duration": "wrong_duration",
            },
        )
        movie = Movie.objects.get(id=1)
        self.assertEqual(movie.duration, 120)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_movie_detail(self):
        response = self.client.delete(
            "/cinema/movies/1/",
        )
        movies = Movie.objects.all()
        self.assertFalse(movies.filter(id=1).exists())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_invalid_movie_detail(self):
        response = self.client.delete(
            "/cinema/movies/10/",
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
