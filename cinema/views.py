from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from cinema.serializers import MovieSerializer
from cinema.models import Movie


class MovieListView(APIView):
    def get(self, request, format=None):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class MovieDetailView(APIView):
    def _get_movie(self, pk):
        return get_object_or_404(Movie, pk=pk)

    def get(self, request, pk, format=None):
        serializer = MovieSerializer(self._get_movie(pk))
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        serializer = MovieSerializer(self._get_movie(pk), data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk, format=None):
        movie = self._get_movie(pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
