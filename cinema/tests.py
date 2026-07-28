from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Movie


class MovieAPITests(APITestCase):

    def setUp(self):
        self.movie = Movie.objects.create(
            title="Test Movie",
            description="Test Description",
            duration=120
        )

    def test_get_movie_list(self):
        url = reverse('movie-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_movie_detail(self):
        url = reverse('movie-detail', args=[self.movie.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_movie(self):
        url = reverse('movie-list')
        data = {
            "title": "New Movie",
            "description": "New Description",
            "duration": 90
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_movie(self):
        url = reverse('movie-detail', args=[self.movie.id])
        data = {
            "title": "Updated Movie",
            "description": "Updated Description",
            "duration": 150
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_movie(self):
        url = reverse('movie-detail', args=[self.movie.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
