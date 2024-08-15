from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from cinema.models import Movie
from cinema.serializers import MovieSerializer


@api_view(["GET", "POST"])
def movie_list(request):
    if request.method == "POST":
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == "GET":
        serializer = MovieSerializer(Movie.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET", "PUT", "DELETE"])
def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == "PUT":
        serializer = MovieSerializer(movie, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == "DELETE":
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == "GET":
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)
