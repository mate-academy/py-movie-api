from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from cinema.models import Movie
from cinema_service.serializers import MovieSerializer


def index(request: HttpRequest):
    return render(request, "base.html")


@api_view(["GET", "POST", "PUT", "DELETE"])
def movie(request, pk=None):
    if request.method == "GET":
        if pk is not None:
            one_movie = get_object_or_404(Movie, pk=pk)
            serializer = MovieSerializer(one_movie)
            return Response(serializer.data, status=status.HTTP_200_OK)
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == "POST":
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "PUT":
        one_movie = get_object_or_404(Movie, pk=pk)
        serializer = MovieSerializer(one_movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "DELETE":
        one_movie = get_object_or_404(Movie, pk=pk)
        one_movie.delete()
        return Response(status=status.HTTP_200_OK)
