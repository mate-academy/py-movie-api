from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
from .serializers import MovieSerializer
from cinema.models import Movie


@api_view(["GET", "POST"])
def movie_list(request):
    serializer = MovieSerializer(data=request.data)
    if request.method == "GET":
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status.HTTP_200_OK)
    else:
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == "GET":
        serializer = MovieSerializer(movie)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
