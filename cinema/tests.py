from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from cinema.models import Movie


class MovieApiTests(APITestCase):
    def setUp(self) -> None:
        self.movie = Movie.objects.create(
            title="Inception",
            description="A mind-bending thriller",
            duration=148,
        )

    def test_get_movie_list(self) -> None:
        url = reverse("cinema:movie-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], self.movie.title)

    def test_create_movie(self) -> None:
        url = reverse("cinema:movie-list")
        payload = {
            "title": "Interstellar",
            "description": "Exploration of space and time",
            "duration": 169,
        }
        response = self.client.post(url, payload)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], payload["title"])
        self.assertTrue(Movie.objects.filter(title="Interstellar").exists())

    def test_get_movie_detail(self) -> None:
        url = reverse("cinema:movie-detail", args=[self.movie.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.movie.title)

    def test_get_movie_detail_not_found(self) -> None:
        url = reverse("cinema:movie-detail", args=[9999])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_movie(self) -> None:
        url = reverse("cinema:movie-detail", args=[self.movie.id])
        payload = {
            "title": "Inception (Updated)",
            "description": "Updated description",
            "duration": 150,
        }
        response = self.client.put(url, payload)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.movie.refresh_from_db()
        self.assertEqual(self.movie.title, payload["title"])
        self.assertEqual(self.movie.duration, payload["duration"])

    def test_delete_movie(self) -> None:
        url = reverse("cinema:movie-detail", args=[self.movie.id])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Movie.objects.filter(id=self.movie.id).exists())
