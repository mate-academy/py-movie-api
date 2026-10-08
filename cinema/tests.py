from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from cinema.models import Movie


class MovieApiTests(APITestCase):
    def setUp(self) -> None:
        self.movie = Movie.objects.create(
            title="The Matrix",
            description="A science fiction movie",
            duration=136,
        )

    def test_list_movies(self) -> None:
        response = self.client.get(reverse("cinema:movie-list"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_movie(self) -> None:
        response = self.client.get(
            reverse("cinema:movie-detail", args=[self.movie.pk])
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.movie.title)

    def test_create_movie(self) -> None:
        payload = {
            "title": "Interstellar",
            "description": "A space adventure",
            "duration": 169,
        }

        response = self.client.post(
            reverse("cinema:movie-list"), payload, format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Movie.objects.filter(title="Interstellar").exists())

    def test_update_movie(self) -> None:
        payload = {
            "title": "The Matrix Reloaded",
            "description": "A science fiction sequel",
            "duration": 138,
        }

        response = self.client.put(
            reverse("cinema:movie-detail", args=[self.movie.pk]),
            payload,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.movie.refresh_from_db()
        self.assertEqual(self.movie.title, payload["title"])

    def test_delete_movie(self) -> None:
        response = self.client.delete(
            reverse("cinema:movie-detail", args=[self.movie.pk])
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Movie.objects.filter(pk=self.movie.pk).exists())

    def test_missing_movie_returns_404(self) -> None:
        response = self.client.get(
            reverse("cinema:movie-detail", args=[9999])
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_invalid_movie_returns_400(self) -> None:
        payload = {
            "title": "Invalid movie",
            "description": "Negative duration",
            "duration": -1,
        }

        response = self.client.post(
            reverse("cinema:movie-list"), payload, format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
