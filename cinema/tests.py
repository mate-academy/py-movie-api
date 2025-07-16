from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Movie

class MovieAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.movie_data = {
            'title': 'Test Movie',
            'year': 2023  # Замените на актуальные поля вашей модели
        }
        self.url = reverse('movie-list')  # Убедитесь, что этот URL существует в urls.py

    def test_create_movie(self):
        response = self.client.post(self.url, self.movie_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_movies(self):
        Movie.objects.create(**self.movie_data)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
