from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from movieapi.cinema.models import Movie
from movieapi.cinema.serializers import MovieSerializer


class MovieList(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDetail(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
