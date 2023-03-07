from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from cinema.models import Movie
from cinema.serializes import MovieSerializer


@api_view(["GET"])
def cinema_list(request):
    if request.method == "GET":
        movie = Movie.objects.all()
        serializer = MovieSerializer(
            movie, many=True
        )
        return Response(serializer.data, status=200)
