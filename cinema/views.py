from __future__ import annotations
import json

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.shortcuts import get_object_or_404

from cinema.models import Movie
from cinema.serializers import MovieSerializer


@csrf_exempt
def movie_list(request: WSGIRequest) -> HttpResponse:
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        json_data = serializer.data
        return HttpResponse(
            json.dumps(json_data),
            content_type='application/json'
        )

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MovieSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        json_data = serializer.data
        return HttpResponse(
            json.dumps(json_data),
            status=201,
            content_type='application/json'
        )


@csrf_exempt
def movie_detail(
        request: WSGIRequest,
        pk: int
) -> HttpResponse:
    movie = get_object_or_404(Movie, pk=pk)

    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        json_data = serializer.data
        return HttpResponse(
            json.dumps(json_data),
            content_type='application/json'
        )

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MovieSerializer(movie, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        json_data = serializer.data
        return HttpResponse(
            json.dumps(json_data),
            content_type='application/json'
        )

    elif request.method == 'DELETE':
        movie.delete()
        return HttpResponse(status=204)
