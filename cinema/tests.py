from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from cinema.models import Movie


class MovieAPITests(TestCase):
    def setUp(self: 'MovieAPITests') -> None:
        self.client = APIClient()
        self.movie = Movie.objects.create(
            title='Inception',
            description='A science-fiction film.',
            duration=148,
        )
        self.list_url = reverse('cinema:movie-list')
        self.detail_url = reverse(
            'cinema:movie-detail',
            kwargs={'pk': self.movie.pk},
        )

    def test_get_movie_list(self: 'MovieAPITests') -> None:
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Inception')

    def test_get_movie_detail(self: 'MovieAPITests') -> None:
        response = self.client.get(self.detail_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Inception')

    def test_create_movie(self: 'MovieAPITests') -> None:
        data = {
            'title': 'Interstellar',
            'description': 'A space adventure.',
            'duration': 169,
        }

        response = self.client.post(self.list_url, data, format='json')

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )
        self.assertTrue(
            Movie.objects.filter(title='Interstellar').exists()
        )

    def test_update_movie(self: 'MovieAPITests') -> None:
        data = {
            'title': 'Inception Updated',
            'description': 'An updated description.',
            'duration': 150,
        }

        response = self.client.put(
            self.detail_url,
            data,
            format='json',
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.movie.refresh_from_db()
        self.assertEqual(self.movie.title, 'Inception Updated')
        self.assertEqual(self.movie.duration, 150)

    def test_delete_movie(self: 'MovieAPITests') -> None:
        response = self.client.delete(self.detail_url)

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT,
        )
        self.assertFalse(
            Movie.objects.filter(pk=self.movie.pk).exists()
        )

    def test_missing_movie_returns_404(
        self: 'MovieAPITests',
    ) -> None:
        response = self.client.get(
            reverse('cinema:movie-detail', kwargs={'pk': 99999})
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND,
        )

    def test_invalid_movie_returns_400(
        self: 'MovieAPITests',
    ) -> None:
        data = {
            'title': 'Invalid Movie',
            'description': 'Missing duration.',
        }

        response = self.client.post(
            self.list_url,
            data,
            format='json',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
        )
