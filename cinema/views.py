from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from cinema.models import Movie
from cinema.serializers import MovieSerializer


@api_view(["GET", "POST"])
def movies_list(request):
    if request.method == "GET":
        movies = Movie.objects.all()
        movies_serializer = MovieSerializer(movies, many=True)
        return Response(movies_serializer.data, status=status.HTTP_200_OK)
    if request.method == "POST":
        movies_serializer = MovieSerializer(data=request.data)
        if movies_serializer.is_valid():
            movies_serializer.save()
            return Response(movies_serializer.data, status=status.HTTP_201_CREATED)
        return Response(movies_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def movies_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)

    if request.method == "GET":
        movie_serializer = MovieSerializer(movie)
        return Response(movie_serializer.data, status=status.HTTP_200_OK)
    if request.method == "PUT":
        movie_serializer = MovieSerializer(instance=movie, data=request.data)
        if movie_serializer.is_valid():
            movie_serializer.save()
            return Response(movie_serializer.data, status=status.HTTP_201_CREATED)
        return Response(movie_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "DELETE":
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
