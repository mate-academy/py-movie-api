from rest_framework import generics
from .models import Movie
from cinema.serializer import MovieSerializer

class MovieListCreateView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        response.status_code = status.HTTP_200_OK
        return response

class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
