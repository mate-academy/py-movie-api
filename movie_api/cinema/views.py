from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Movie
from .serializer import MovieSerializer


@api_view(["GET", "POST"])
def movie_list(request):
    if request.method == "GET":
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    serializer = MovieSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "DELETE"])
def movie_one(request, pk):
    movie = Movie.objects.get(id=pk)
    if request.method == "GET":
        serializer = MovieSerializer(movie)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    if request.method == "DELETE":
        movie.delete()
        return Response(status=status.HTTP_200_OK)

    serializer = MovieSerializer(movie, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
