from rest_framework import generics
from .models import Movie
from .serializers import MovieSerializer


# List and Create movies
class MovieListCreateAPIView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


# Retrieve, Update, Delete a movie
class MovieRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


# Create your views here.
