from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.http import HttpRequest

from cinema.models import Movie
from cinema.serializers import MovieSerializer


@api_view(["GET", "POST"])
def movies(request: HttpRequest) -> Response:
    if request.method == "GET":
        movie = Movie.objects.all()
        serializer = MovieSerializer(movie, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == "POST":
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def change_movie(request: HttpRequest, pk: int) -> Response:
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == "GET":
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status.HTTP_200_OK)
    if request.method == "PUT":
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "DELETE":
        movie.delete()
        return Response({"message": "Object deleted successfully"})
