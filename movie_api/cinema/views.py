from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from cinema.models import Movie
from cinema.serializers import MovieSerializer
from django.shortcuts import get_object_or_404


@api_view(["GET", "POST", "PUT", "DELETE"])
def movies_list(request, pk=None):
    if request.method == "GET":
        if pk:
            movie = get_object_or_404(Movie, pk=pk)
            serializer = MovieSerializer(movie)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            movies = Movie.objects.all()
            serializer = MovieSerializer(movies, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == "POST":
        if not pk:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )

    if request.method == "PUT":
        if not pk:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == "DELETE":
        if not pk:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
