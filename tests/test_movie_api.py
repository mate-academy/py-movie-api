from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from cinema.models import Movie


class BaseMovieAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.movie_data = {
            "title": "Test Movie",
            "description": "description",
            "duration": 123,
        }
        self.movie = Movie.objects.create(**self.movie_data)


class MovieAPITest(BaseMovieAPITest):
    def test_get_all_movies(self):
        response = self.client.get(reverse("cinema:movies-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_movie_detail(self):
        response = self.client.get(
            reverse("cinema:movie-detail", kwargs={"pk": self.movie.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_movie(self):
        response = self.client.post(
            reverse("cinema:movies-list"), self.movie_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_movie(self):
        updated_data = self.movie_data
        response = self.client.put(
            reverse("cinema:movie-detail", kwargs={"pk": self.movie.pk}),
            updated_data,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_movie(self):
        response = self.client.delete(
            reverse("cinema:movie-detail", kwargs={"pk": self.movie.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
