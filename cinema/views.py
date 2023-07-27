from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from cinema.models import Movie
from cinema.serializers import MovieSerializer


@api_view(["GET", "POST"])
def movie_list(request):
    if request.method == "GET":
        movies = Movie.objects.all()
        movie_serializer = MovieSerializer(movies, many=True)
        return Response(movie_serializer.data, status=status.HTTP_200_OK)

    if request.method == "POST":
        movie_serializer = MovieSerializer(data=request.data)

        if movie_serializer.is_valid():
            movie_serializer.save()
            return Response(movie_serializer.data, status.HTTP_201_CREATED)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def movie_detail(request, pk):
    if request.method == "GET":
        movie = get_object_or_404(Movie, pk=pk)
        movie_serializer = MovieSerializer(movie)
        return Response(movie_serializer.data, status=status.HTTP_200_OK)

    elif request.method == "PUT":
        movie = get_object_or_404(Movie, pk=pk)
        movie_serializer = MovieSerializer(movie, data=request.data)
        if movie_serializer.is_valid():
            movie_serializer.save()
            return Response(movie_serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        movie = get_object_or_404(Movie, pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
