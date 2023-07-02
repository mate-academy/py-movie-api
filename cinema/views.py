from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status

from cinema.models import Movie
from cinema.serializers import MovieSerializer


@api_view(["GET", "POST"])
def movie_list(request):
    """
    Retrieve a list of movies or create a new movie.
    """
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
def movie_detail(request, pk):
    """
    Retrieve, update or delete a movie by its primary key (pk).
    """
    movie = get_object_or_404(Movie, pk=pk)

    if request.method == "GET":
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = MovieSerializer(movie, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    elif request.method == "DELETE":
        movie.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
