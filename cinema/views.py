from django.shortcuts import render
from django.views import generic
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

import io
from rest_framework.parsers import JSONParser

from cinema.models import Movie
from cinema.serializers import MovieSerializer


@api_view(["GET", "POST"])
def movie_list(request):
    if request.method == "GET":
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == "POST":
        serializer = MovieSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def movie(request, pk):
    if request.method == "GET":
        movie_single = Movie.objects.get(id=pk)
        serializer = MovieSerializer(movie_single)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == "PUT":
        movie_single = Movie.objects.get(id=pk)
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.update(movie_single, request.data)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        print(1)
        if pk in str(Movie.objects.all().values_list("id")):
            print(2)
            Movie.objects.get(id=pk).delete()
            return Response(status=status.HTTP_200_OK)

        return Response(status=status.HTTP_400_BAD_REQUEST)






