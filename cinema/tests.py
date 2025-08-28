from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Movie


class MovieAPITests(APITestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title="Test Movie", description="Test Description", duration=120
        )
        self.list_url = reverse("movie-list-create")
        self.detail_url = reverse("movie-detail", args=[self.movie.pk])

    def test_list_movies(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 1)

    def test_retrieve_movie(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["title"], "Test Movie")

    def test_create_movie(self):
        data = {"title": "New Movie", "description": "New Desc", "duration": 90}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Movie.objects.count(), 2)

    def test_update_movie(self):
        data = {
            "title": "Updated Movie",
            "description": "Updated Desc",
            "duration": 150,
        }
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.movie.refresh_from_db()
        self.assertEqual(self.movie.title, "Updated Movie")

    def test_delete_movie(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Movie.objects.count(), 0)
