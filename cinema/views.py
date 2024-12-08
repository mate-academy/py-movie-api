from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from cinema.models import Movie
from cinema.serializes import MovieSerializer


class MovieListCreateView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
