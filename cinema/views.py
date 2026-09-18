"""API views for cinema resources."""

from __future__ import annotations

from rest_framework import generics

from cinema.models import Movie
from cinema.serializers import MovieSerializer


class MovieListCreateView(generics.ListCreateAPIView):
    """List all movies or create one movie."""

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, replace, or delete one movie by primary key."""

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
