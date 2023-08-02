from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view

from rest_framework.parsers import JSONParser

from cinema.models import Movie
from cinema.serializers import MovieSerializer


@api_view(
    [
        "GET",
        "POST",
    ]
)
def movie_list(request):
    if request.method == "GET":
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        movie_data = request.data
        movie_serializer = MovieSerializer(data=movie_data)
        movie_serializer.is_valid(raise_exception=True)
        movie_serializer.save()
        return JsonResponse(
            movie_serializer.data, status=status.HTTP_201_CREATED
            )


@api_view(["GET", "PUT", "DELETE"])
def movie_detail(request, pk):

    movie = get_object_or_404(Movie, pk=pk)

    if request.method == "GET":
        serializer = MovieSerializer(movie)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        movie_data = JSONParser().parse(request)
        serializer = MovieSerializer(movie, data=movie_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(serializer.data)


    elif request.method == "DELETE":
        movie.delete()
        return JsonResponse(
            {"message": "Movie was deleted successfully!"},
            status=status.HTTP_204_NO_CONTENT,
        )
