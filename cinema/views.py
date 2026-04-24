from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from cinema.serializers import MovieSerializer

from cinema.models import Movie


class MovieListView(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MovieDetailView(APIView):
    def get(self, request, **kwargs):
        movie = get_object_or_404(Movie, id=kwargs.get("pk"))
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, **kwargs):
        movie = get_object_or_404(Movie, id=kwargs.get("pk"))
        serializer = MovieSerializer(movie)
        serializer.is_valid(raise_exception=True)
        serializer.update(movie, request.data)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def delete(self, request, **kwargs):
        movie = get_object_or_404(Movie, id=kwargs.get("pk"))
        serializer = MovieSerializer(movie)
        serializer.is_valid(raise_exception=True)
        movie.delete()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
