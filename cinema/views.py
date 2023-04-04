from __future__ import annotations

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from cinema.models import Movie
from cinema.serializers import MovieSerializer


@csrf_exempt
def movie_list(request: WSGIRequest) -> JsonResponse:
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MovieSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(serializer.data, status=201)


@csrf_exempt
def movie_detail(
        request: WSGIRequest,
        pk: int
) -> JsonResponse | HttpResponse:
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MovieSerializer(movie, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(serializer.data)

    elif request.method == 'DELETE':
        movie.delete()
        return HttpResponse(status=204)
