from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from cinema.models import Movie
from cinema.serializers import MovieSerializer


@api_view(["GET"])
def movies_list(request):
    if request.method == "GET":
        movies = Movie.objects.all()
        movies = MovieSerializer(movies, many=True)
        return Response(movies.data, status=200)

