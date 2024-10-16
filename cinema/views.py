from rest_framework import generics
from cinema.models import Movie
from cinema.serializers import MovieSerializer
from django.http import HttpResponse
from django.views import View


# List all movies and create a new movie
class MovieListCreateView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


# Retrieve, update, and delete a movie by ID
class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class HomeView(View):
    def get(self, request):
        return HttpResponse(
            "<h1>Welcome to the Cinema API</h1><p>Use /api/cinema/movies/ to view the movies.</p>"
        )
