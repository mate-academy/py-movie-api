from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from cinema.models import Movie


class MovieAPITest(APITestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title="The Matrix",
            description="Virtual reality",
            duration=136
        )
        self.list_url = reverse("movie-list-create")
        self.detail_url = reverse("movie-detail", kwargs={"pk": self.movie.pk})

    def test_get_movie_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_movie(self):
        data = {
            "title": "Dune",
            "description": "Desert planet",
            "duration": 155
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Movie.objects.count(), 2)
        self.assertEqual(Movie.objects.latest("id").title, "Dune")

    def test_get_single_movie(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "The Matrix")

    def test_update_movie(self):
        data = {
            "title": "The Matrix Reloaded",
            "description": "Updated desc",
            "duration": 150
        }
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.movie.refresh_from_db()
        self.assertEqual(self.movie.title, "The Matrix Reloaded")

    def test_delete_movie(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Movie.objects.filter(pk=self.movie.pk).exists())
