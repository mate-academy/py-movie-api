from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from cinema.models import Movie
from cinema.serializers import MovieSerializer

VALID_PAYLOAD = {
    "title": "Heat",
    "description": "A detective hunts a crew of professional robbers.",
    "duration": 170,
}


def list_url() -> str:
    return reverse("cinema:movie-list")


def detail_url(movie_id: int) -> str:
    return reverse("cinema:movie-detail", args=[movie_id])


class MovieModelTests(TestCase):
    def test_str_returns_title(self) -> None:
        movie = Movie(title="Looper", description="Time travel.", duration=119)

        self.assertEqual(str(movie), "Looper")


class MovieApiTests(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.inception = Movie.objects.create(
            title="Inception",
            description="A thief plants an idea into a mind.",
            duration=148,
        )
        cls.looper = Movie.objects.create(
            title="Looper",
            description="A hitman meets his future self.",
            duration=119,
        )

    def test_urls_end_with_slash(self) -> None:
        self.assertEqual(list_url(), "/api/cinema/movies/")
        self.assertEqual(detail_url(1), "/api/cinema/movies/1/")

    def test_list_returns_all_movies(self) -> None:
        response = self.client.get(list_url())

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected = MovieSerializer(Movie.objects.all(), many=True).data
        self.assertEqual(response.data, expected)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_movie(self) -> None:
        response = self.client.get(detail_url(self.inception.id))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, MovieSerializer(self.inception).data)

    def test_retrieve_missing_movie_returns_404(self) -> None:
        response = self.client.get(detail_url(999))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_movie(self) -> None:
        response = self.client.post(list_url(), VALID_PAYLOAD, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        movie = Movie.objects.get(id=response.data["id"])
        self.assertEqual(MovieSerializer(movie).data, response.data)
        self.assertEqual(response.data, {"id": movie.id, **VALID_PAYLOAD})

    def test_create_without_required_field_returns_400(self) -> None:
        for field in VALID_PAYLOAD:
            with self.subTest(missing=field):
                payload = {
                    key: value
                    for key, value in VALID_PAYLOAD.items()
                    if key != field
                }
                response = self.client.post(list_url(), payload, format="json")

                self.assertEqual(
                    response.status_code, status.HTTP_400_BAD_REQUEST
                )
                self.assertIn(field, response.data)
        self.assertEqual(Movie.objects.count(), 2)

    def test_create_with_invalid_duration_returns_400(self) -> None:
        for duration in (0, -5, "abc"):
            with self.subTest(duration=duration):
                payload = {**VALID_PAYLOAD, "duration": duration}
                response = self.client.post(list_url(), payload, format="json")

                self.assertEqual(
                    response.status_code, status.HTTP_400_BAD_REQUEST
                )
                self.assertIn("duration", response.data)
        self.assertEqual(Movie.objects.count(), 2)

    def test_update_movie(self) -> None:
        response = self.client.put(
            detail_url(self.inception.id), VALID_PAYLOAD, format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.inception.refresh_from_db()
        self.assertEqual(
            MovieSerializer(self.inception).data,
            {"id": self.inception.id, **VALID_PAYLOAD},
        )
        self.assertEqual(response.data, MovieSerializer(self.inception).data)

    def test_update_requires_all_fields(self) -> None:
        response = self.client.put(
            detail_url(self.inception.id), {"title": "Renamed"}, format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.inception.refresh_from_db()
        self.assertEqual(self.inception.title, "Inception")

    def test_update_missing_movie_returns_404(self) -> None:
        response = self.client.put(
            detail_url(999), VALID_PAYLOAD, format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_movie(self) -> None:
        response = self.client.delete(detail_url(self.looper.id))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Movie.objects.filter(id=self.looper.id).exists())
        self.assertEqual(Movie.objects.count(), 1)

    def test_delete_missing_movie_returns_404(self) -> None:
        response = self.client.delete(detail_url(999))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_unsupported_methods_return_405(self) -> None:
        not_allowed = (
            ("PUT", list_url()),
            ("DELETE", list_url()),
            ("POST", detail_url(self.inception.id)),
            ("PATCH", detail_url(self.inception.id)),
        )
        for method, url in not_allowed:
            with self.subTest(method=method, url=url):
                response = self.client.generic(method, url)

                self.assertEqual(
                    response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED
                )
