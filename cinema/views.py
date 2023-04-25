from django.shortcuts import render
from django.http import JsonResponse

from cinema.models import Movie
from cinema.serializers import MovieSerializer


def movie_list(request):
    if request.method == "GET":
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)

        return JsonResponse(
            serializer.data,
            status=200,
            safe=False
        )
