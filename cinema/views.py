from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.shortcuts import render, get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status

from cinema.models import Movies
from cinema.serilizers import MoviesSerializer


@api_view(["GET", "POST"])
def movie_list(request):
    if request.method == "GET":
        movies = Movies.objects.all()
        serializer = MoviesSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        serializer = MoviesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "DELETE"])
def movie_detail(request, pk):
    movie = get_object_or_404(Movies, pk=pk)
    if request.method == "GET":
        serializer = MoviesSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        serializer = MoviesSerializer(movie, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
