from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from cinema.models import Movie


MOVIES_DATA = [
    {
        "title": "The Departed",
        "description": (
            "An undercover cop and a mole in the police attempt "
            "to identify each other while infiltrating an "
            "Irishgang in South Boston."
        ),
        "duration": 151,
    },
    {
        "title": "Inception",
        "description": (
            "A thief who steals corporate secrets through the use of "
            "dream-sharing technology is given the inverse task of "
            "planting an idea into the mind of a C.E.O."
        ),
        "duration": 148,
    },
    {
        "title": "The Matrix",
        "description": "A hacker discovers the world is a simulated reality.",
        "duration": 136,
    },
]


class MovieTests(APITestCase):
    def test_get_movies_empty_database(self):
        url = reverse("cinema:movies-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])

    def test_get_movies_with_three_movies(self):
        for movie_data in MOVIES_DATA:
            Movie.objects.create(**movie_data)
        url = reverse("cinema:movies-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data[0]["title"], MOVIES_DATA[0]["title"])
        self.assertEqual(response.data[1]["title"], MOVIES_DATA[1]["title"])
        self.assertEqual(response.data[2]["title"], MOVIES_DATA[2]["title"])

    def test_post_movie_with_valid_data(self):
        url = reverse("cinema:movies-list")
        response = self.client.post(url, [MOVIES_DATA[0]], format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Movie.objects.count(), 1)

    def test_post_movies_with_valid_data(self):
        url = reverse("cinema:movies-list")
        response = self.client.post(url, MOVIES_DATA, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Movie.objects.count(), 3)

    def test_post_movies_with_empty_data(self):
        url = reverse("cinema:movies-list")
        response = self.client.post(url, {}, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_movies_with_invalid_fields(self):
        url = reverse("cinema:movies-list")
        data = [{"wrong": "field"}]
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_movie_detail_existing_movie(self):
        movie = Movie.objects.create(**MOVIES_DATA[0])
        url = reverse("cinema:movie-detail", args=[movie.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], MOVIES_DATA[0]["title"])
        self.assertEqual(
            response.data["description"], MOVIES_DATA[0]["description"]
        )
        self.assertEqual(response.data["duration"], MOVIES_DATA[0]["duration"])

    def test_get_movie_detail_missing_movie(self):
        url = reverse("cinema:movie-detail", args=[1])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_put_movie_with_valid_data(self):
        movie = Movie.objects.create(**MOVIES_DATA[0])
        url = reverse("cinema:movie-detail", args=[movie.id])
        data = {"title": "Updated title"}
        response = self.client.put(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], data["title"])
        self.assertEqual(
            response.data["description"], MOVIES_DATA[0]["description"]
        )

    def test_put_movie_with_invalid_data(self):
        movie = Movie.objects.create(**MOVIES_DATA[0])
        url = reverse("cinema:movie-detail", args=[movie.id])
        data = {"duration": "wrong"}
        response = self.client.put(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_movie_existing_movie(self):
        movie = Movie.objects.create(**MOVIES_DATA[0])
        url = reverse("cinema:movie-detail", args=[movie.id])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Movie.objects.count(), 0)

    def test_delete_movie_missing_movie(self):
        url = reverse("cinema:movie-detail", args=[1])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
