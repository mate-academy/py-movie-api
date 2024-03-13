from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.generics import get_object_or_404

from cinema.models import Movie
from cinema.serializers import MovieSerializer


def movie_list(request):
    if request.method == "GET":
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)


def movie_detail(request, movie_id):
    if request.method == "GET":
        movie = get_object_or_404(Movie, pk=movie_id)
        serializer = MovieSerializer(movie)
        return JsonResponse(serializer.data, status=200)
