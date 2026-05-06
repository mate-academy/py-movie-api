from django.test import TestCase
from cinema.models import Movie
from cinema.serializer import MovieSerializer
from rest_framework.test import APIClient


class MovieModelTest(TestCase):

    def test_str(self):
        movie = Movie.objects.create(
            title="Test_Film",
            description="Test_Description",
            duration=130
        )
        self.assertEqual(str(movie), "Test_Film")


class MovieSerializerTest(TestCase):

    def setUp(self):
        self.movie = Movie.objects.create(
            title="Old title",
            description="Old desc",
            duration=100
        )

        self.data = {
            "title": "Test_Film",
            "description": "Test_Description",
            "duration": 130
            }

    def test_valid_data(self):
        serializer = MovieSerializer(data=self.data)

        self.assertTrue(serializer.is_valid())

    def test_invalid_data(self):
        data = {"title": "",
                "description": "Test_Description",
                "duration": 130
                }
        serializer = MovieSerializer(data=data)

        self.assertFalse(serializer.is_valid())

    def test_create_movie(self):
        initial_count = Movie.objects.count()

        serializer = MovieSerializer(data=self.data)
        self.assertTrue(serializer.is_valid(), serializer.errors)

        movie = serializer.save()

        self.assertEqual(Movie.objects.count(), initial_count + 1)
        self.assertEqual(movie.title, self.data["title"])
        self.assertEqual(movie.description, self.data["description"])
        self.assertEqual(movie.duration, self.data["duration"])

    def test_update_movie(self):

        data = {
            "title": "New title",
            "description": "New desc",
            "duration": 120
        }

        serializer = MovieSerializer(self.movie, data=data)
        self.assertTrue(serializer.is_valid())

        updated_movie = serializer.save()

        self.assertEqual(updated_movie.title, "New title")
        self.assertEqual(updated_movie.description, "New desc")
        self.assertEqual(updated_movie.duration, 120)

    def test_partial_update(self):

        data = {"title": "New title"}

        serializer = MovieSerializer(self.movie, data=data, partial=True)
        self.assertTrue(serializer.is_valid(), serializer.errors)

        updated_movie = serializer.save()

        self.assertEqual(updated_movie.title, "New title")
        self.assertEqual(updated_movie.description, "Old desc")


class MovieApiTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_movies_list(self):

        for i in range(5):
            Movie.objects.create(
                title=f"Test_{i}",
                description=f"Desc{i}",
                duration=100 + i
            )

        url = "/api/cinema/movies/"
        response = self.client.get(url)

        titles = [movie["title"] for movie in response.data]

        self.assertEqual(response.status_code, 200)

        self.assertEqual(len(response.data), 5)
        for i in range(5):
            self.assertIn(f"Test_{i}", titles)

    def test_post_movie(self):
        url = "/api/cinema/movies/"

        data = {
            "title": "New Movie",
            "description": "Some desc",
            "duration": 120
        }

        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Movie.objects.count(), 1)

        movie = Movie.objects.first()

        self.assertEqual(movie.title, "New Movie")
        self.assertEqual(movie.description, "Some desc")
        self.assertEqual(movie.duration, 120)

    def test_get_movie(self):
        movie = Movie.objects.create(
            title="Test",
            description="Desc",
            duration=100
        )

        url = f"/api/cinema/movies/{movie.id}/"

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["id"], movie.id)
        self.assertEqual(response.data["title"], movie.title)
        self.assertEqual(response.data["description"], movie.description)
        self.assertEqual(response.data["duration"], movie.duration)

    def test_put_movie(self):
        movie = Movie.objects.create(
            title="Test",
            description="Desc",
            duration=100
        )

        url = f"/api/cinema/movies/{movie.id}/"

        data = {
            "title": "New_Test",
            "description": "New_Desc",
            "duration": 101
        }

        response = self.client.put(url, data, format="json")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["id"], movie.id)
        self.assertEqual(response.data["title"], "New_Test")
        self.assertEqual(response.data["description"], "New_Desc")
        self.assertEqual(response.data["duration"], 101)

    def test_delete_movie(self):
        movie = Movie.objects.create(
            title="Test",
            description="Desc",
            duration=100
        )

        url = f"/api/cinema/movies/{movie.id}/"

        response = self.client.delete(url)

        self.assertEqual(response.status_code, 204)
        self.assertFalse(Movie.objects.filter(id=movie.id).exists())
