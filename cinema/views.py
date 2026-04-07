from rest_framework import viewsets

from cinema.models import Movie
from cinema.serializer import MovieSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
