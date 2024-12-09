from django.test import TestCase
from cinema.models import Movie


class MovieModelTest(TestCase):

    def setUp(self):
        self.movie = Movie.objects.create(
            title="Inception",
            description="A mind-bending thriller",
            duration=148
        )

    def test_movie_creation(self):
        movie = Movie.objects.get(id=self.movie.id)
        self.assertEqual(movie.title, "Inception")
        self.assertEqual(movie.description, "A mind-bending thriller")
        self.assertEqual(movie.duration, 148)

    def test_movie_str_method(self):
        self.assertEqual(str(self.movie), " Movie: Inception")

    def test_movie_update(self):
        self.movie.title = "Interstellar"
        self.movie.description = "A journey beyond the stars"
        self.movie.duration = 169
        self.movie.save()

        updated_movie = Movie.objects.get(id=self.movie.id)
        self.assertEqual(updated_movie.title, "Interstellar")
        self.assertEqual(updated_movie.description, "A journey beyond the stars")
        self.assertEqual(updated_movie.duration, 169)

    def test_movie_deletion(self):
        movie_id = self.movie.id
        self.movie.delete()
        with self.assertRaises(Movie._meta.object_name.DoesNotExist):
            Movie.objects.get(id=movie_id)
