from rest_framework import generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .models import Movie
from .serializers import MovieSerializer


class MovieListCreateView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def post(self, request, *args, **kwargs):
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def put(self, request, *args, **kwargs):
        movie = get_object_or_404(Movie, pk=kwargs["pk"])
        serializer = MovieSerializer(movie, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        movie = get_object_or_404(Movie, pk=kwargs["pk"])
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
