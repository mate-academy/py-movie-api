from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from cinema.models import Movie


class MovieApiTests(APITestCase):
    def setUp(self):
        # Criando um filme inicial para os testes de GET (detail), PUT e DELETE
        self.movie = Movie.objects.create(
            title="The Departed", description="Irish gang in South Boston", duration=151
        )
        self.list_url = reverse("cinema_list")
        self.detail_url = reverse("cinema_detail", kwargs={"pk": self.movie.pk})

    def test_list_movies(self):
        """Testa se a listagem retorna 200 OK e os dados corretos"""
        res = self.client.get(self.list_url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]["title"], self.movie.title)

    def test_create_movie(self):
        """Testa a criação de um filme (POST)"""
        payload = {
            "title": "Inception",
            "description": "Dream-sharing technology",
            "duration": 148,
        }
        res = self.client.post(self.list_url, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Movie.objects.filter(title="Inception").exists())

    def test_get_movie_detail(self):
        """Testa o detalhe de um filme (GET com PK)"""
        res = self.client.get(self.detail_url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data["title"], self.movie.title)

    def test_update_movie(self):
        """Testa a atualização completa (PUT)"""
        payload = {
            "title": "The Departed - Updated",
            "description": "New description",
            "duration": 160,
        }
        res = self.client.put(self.detail_url, payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.movie.refresh_from_db()
        self.assertEqual(self.movie.title, "The Departed - Updated")

    def test_delete_movie(self):
        """Testa a remoção de um filme (DELETE)"""
        res = self.client.delete(self.detail_url)
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Movie.objects.filter(pk=self.movie.pk).exists())

    def test_get_invalid_movie(self):
        """Testa se retorna 404 quando o filme não existe (Uso do get_object_or_404)"""
        invalid_url = reverse("cinema_detail", kwargs={"pk": 999})
        res = self.client.get(invalid_url)
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)
