from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from cinema.models import Movie
from cinema.serializers import MovieSerializer


@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == 'GET':
        movies = MovieSerializer(Movie.objects.all(), many=True)
        return Response(movies.data, status=status.HTTP_200_OK)
    else:
        movie = MovieSerializer(request.data)
        if movie.is_valid(raise_exception=True):
            movie.save()
            return Response(movie.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', "PUT"])
def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)

    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
