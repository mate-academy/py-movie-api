from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from cinema.models import Movie
from cinema.serializers import MovieSerializer


@api_view(["GET", "POST"])
def movie_list(request):
    if request.method == "GET":
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    if request.method == "POST":
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "DELETE"])
def movie_detail(request, pk: int):
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status.HTTP_200_OK)

    if request.method == "PUT":
        serializer = MovieSerializer(movie, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_202_ACCEPTED)

    if request.method == "DELETE":
        movie.delete()
        return Response(status.HTTP_204_NO_CONTENT)
