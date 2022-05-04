from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status

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


@api_view(["PUT", "PATCH", "DELETE", "GET"])
def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)

    if request.method == "PUT" or request.method == "PATCH":
        serializer = MovieSerializer(movie, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)

        return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    if request.method == "GET":
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == "DELETE":
        movie.delete()

    return Response(status=status.HTTP_204_NO_CONTENT)
