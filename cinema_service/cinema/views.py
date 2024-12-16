from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.request import Request
from rest_framework.serializers import Serializer
from typing import Any
from .models import Movie
from .serializers import MovieSerializer


class MovieListView(APIView):
    def get(self: 'MovieListView', request: Request) -> Response:
        movies = Movie.objects.all()
        serializer: Serializer[Any] = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self: 'MovieListView', request: Request) -> Response:
        serializer: Serializer[Any] = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieDetailView(APIView):
    def get(self: 'MovieDetailView', request: Request, pk: int) -> Response:
        movie = get_object_or_404(Movie, pk=pk)
        serializer: Serializer[Any] = MovieSerializer(movie)
        return Response(serializer.data)

    def put(self: 'MovieDetailView', request: Request, pk: int) -> Response:
        movie = get_object_or_404(Movie, pk=pk)
        serializer: Serializer[Any] = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self: 'MovieDetailView', request: Request, pk: int) -> Response:
        movie = get_object_or_404(Movie, pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
