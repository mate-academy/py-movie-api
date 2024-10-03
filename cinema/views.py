from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from cinema.models import Movie
from cinema.serializer import MovieSerializer


@api_view(["GET", "POST"])
def movies_list_create(request: Request) -> Response:
    if request.method == "GET":
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    serializer = MovieSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(["GET", "PUT", "DELETE"])
def movies_detail(request: Request, pk: int) -> Response:
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == "GET":
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "PUT":
        serializer = MovieSerializer(movie)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    movie.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
