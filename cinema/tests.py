import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from cinema.models import Movie
from cinema.serializers import MovieSerializer


def detail_url(movie_id: int) -> str:
    return reverse("cinema:movie-detail", args=[movie_id])


@pytest.fixture
def movies_url() -> str:
    return reverse("cinema:movie-list")


@pytest.fixture
def api_client() -> APIClient:
    return APIClient()


@pytest.fixture
def sample_movie() -> Movie:
    return Movie.objects.create(
        title="Inception",
        description="A thief who steals corporate secrets.",
        duration=148,
    )


@pytest.mark.django_db
class TestMovieAPI:
    def test_list_movies(self, api_client, movies_url, sample_movie):
        res = api_client.get(movies_url)
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)

        assert res.status_code == status.HTTP_200_OK
        assert res.data == serializer.data

    def test_retrieve_movie_detail(self, api_client, sample_movie):
        url = detail_url(sample_movie.id)
        res = api_client.get(url)
        serializer = MovieSerializer(sample_movie)

        assert res.status_code == status.HTTP_200_OK
        assert res.data == serializer.data

    def test_create_movie(self, api_client, movies_url):
        payload = {
            "title": "Interstellar",
            "description": "A team of explorers travel through a wormhole.",
            "duration": 169,
        }
        res = api_client.post(movies_url, payload)

        assert res.status_code == status.HTTP_201_CREATED
        assert Movie.objects.filter(title=payload["title"]).exists()

    def test_update_movie(self, api_client, sample_movie):
        payload = {
            "title": "Inception Remastered",
            "description": "Updated description.",
            "duration": 150,
        }
        url = detail_url(sample_movie.id)
        res = api_client.put(url, payload)

        assert res.status_code == status.HTTP_200_OK
        sample_movie.refresh_from_db()
        assert sample_movie.title == payload["title"]

    def test_delete_movie(self, api_client, sample_movie):
        url = detail_url(sample_movie.id)
        res = api_client.delete(url)

        assert res.status_code == status.HTTP_204_NO_CONTENT
        assert not Movie.objects.filter(id=sample_movie.id).exists()
