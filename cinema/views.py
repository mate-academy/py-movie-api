from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from cinema.serializers import CinemaSerializer

from cinema.models import Movie


@api_view(["GET", "POST"])
def movie_list(request):
    movies = Movie.objects.all()
    if request.method == "GET":
        serializer = CinemaSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        serializer = CinemaSerializer(movies, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "DELETE", "PUT"])
def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == "GET":
        serializer = CinemaSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        serializer = CinemaSerializer(movie, data=request)
        if serializer.is_valid():
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
