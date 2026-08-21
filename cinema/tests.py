from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from cinema.models import Movie


class MovieApiTests(APITestCase):
    def setUp(self) -> None:
        self.movie = Movie.objects.create(
            title="Inception",
            description="A dream-sharing thief receives a final task.",
            duration=148,
        )

    def test_list_movies(self) -> None:
        response = self.client.get(reverse("movie-list"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_movie(self) -> None:
        payload = {
            "title": "Looper",
            "description": "A time-travel thriller.",
            "duration": 119,
        }
        response = self.client.post(reverse("movie-list"), payload)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Movie.objects.filter(title="Looper").exists())

    def test_retrieve_movie(self) -> None:
        response = self.client.get(
            reverse("movie-detail", kwargs={"pk": self.movie.pk})
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.movie.title)

    def test_update_movie(self) -> None:
        payload = {
            "title": "Inception Updated",
            "description": self.movie.description,
            "duration": 150,
        }
        response = self.client.put(
            reverse("movie-detail", kwargs={"pk": self.movie.pk}),
            payload,
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.movie.refresh_from_db()
        self.assertEqual(self.movie.duration, 150)

    def test_delete_movie(self) -> None:
        response = self.client.delete(
            reverse("movie-detail", kwargs={"pk": self.movie.pk})
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Movie.objects.filter(pk=self.movie.pk).exists())

    def test_missing_movie_returns_404(self) -> None:
        response = self.client.get(
            reverse("movie-detail", kwargs={"pk": 999})
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_invalid_movie_returns_400(self) -> None:
        response = self.client.post(
            reverse("movie-list"),
            {"title": "Incomplete"},
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
