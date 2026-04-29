from django.test import TestCase
from rest_framework import status

from cinema.models import Movie
from cinema.serializers import MovieSerializer
from rest_framework.test import APITestCase


class MovieModelTest(TestCase):
    def test_movie_str(self):
        movie = Movie.objects.create(
            title="Movie123",
            description="My favorite movie",
            duration=5,
        )
        self.assertEqual(str(movie), "Movie123")


class MovieSerializerTest(TestCase):
    def test_movie_serializer_invalid(self):
        valid_data = {}
        serializer = MovieSerializer(data=valid_data)
        self.assertFalse(serializer.is_valid())


    def test_movie_serializer_valid(self):
        valid_data = {
            "title": "Movie123",
            "description": "My favorite movie",
            "duration": 85
        }
        serializer = MovieSerializer(data=valid_data)
        self.assertTrue(serializer.is_valid())



class MovieListApiTest(APITestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title="Movie123",
            description="My favorite movie",
            duration=85,
        )
        self.URL_MOVIE_LIST = "/api/cinema/movies/"

    def test_movie_list_get_method(self):
        response = self.client.get(self.URL_MOVIE_LIST)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_movie_list_post_method_valid(self):
        valid_data = {
                "title": "Movie123123",
                "description": "My second favorite movie",
                "duration": 123,
            }
        response = self.client.post(self.URL_MOVIE_LIST, valid_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(Movie.objects.all()), 2)

    def test_movie_list_post_method_invalid(self):
        invalid_data = {}
        response = self.client.post(self.URL_MOVIE_LIST, invalid_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(len(Movie.objects.all()), 1)


class MovieDetailApiTest(APITestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title="Movie123",
            description="My favorite movie",
            duration=85,
        )
        self.URL_MOVIE_DETAIL = f"/api/cinema/movies/{self.movie.id}/"

    def test_movie_detail_get_method(self):
        response = self.client.get(self.URL_MOVIE_DETAIL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_movie_detail_put_method(self):
        valid_data = {"title": "Newtitle"}
        response = self.client.put(self.URL_MOVIE_DETAIL, valid_data)
        self.movie.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.movie.title, "Newtitle")

    def test_movie_detail_delete_method(self):
        response = self.client.delete(self.URL_MOVIE_DETAIL)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(len(Movie.objects.all()), 0)
