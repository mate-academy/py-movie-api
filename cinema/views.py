from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from cinema.models import Movie
from cinema.serializers import MovieSerializer


@api_view(["GET", "POST"])
def movie_list_view(request) -> Response:
    if request.method == "GET":
        movie_list = Movie.objects.all()
        serializer = MovieSerializer(movie_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == "POST":
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def movie_detail_view(request, pk: int) -> Response:
    movie = get_object_or_404(Movie, id=pk)
    if request.method == "GET":
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == "PUT":
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    movie.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
