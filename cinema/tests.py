from rest_framework import status
from rest_framework.test import APITestCase

from cinema.models import Movie


class MovieApiTests(APITestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title="Inception",
            description="A thief enters dreams to steal ideas.",
            duration=148,
        )

    def test_list_movies(self):
        response = self.client.get("/api/cinema/movies/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], self.movie.title)

    def test_retrieve_movie(self):
        response = self.client.get(f"/api/cinema/movies/{self.movie.pk}/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], self.movie.pk)

    def test_create_movie(self):
        payload = {
            "title": "Interstellar",
            "description": "Explorers travel through a wormhole.",
            "duration": 169,
        }

        response = self.client.post("/api/cinema/movies/", payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Movie.objects.count(), 2)
        self.assertEqual(Movie.objects.get(title="Interstellar").duration, 169)

    def test_update_movie(self):
        payload = {
            "title": "Inception",
            "description": "A team plants an idea inside a dream.",
            "duration": 150,
        }

        response = self.client.put(
            f"/api/cinema/movies/{self.movie.pk}/",
            payload,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.movie.refresh_from_db()
        self.assertEqual(self.movie.description, payload["description"])
        self.assertEqual(self.movie.duration, 150)

    def test_delete_movie(self):
        response = self.client.delete(f"/api/cinema/movies/{self.movie.pk}/")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Movie.objects.filter(pk=self.movie.pk).exists())
