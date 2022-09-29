from http import HTTPStatus

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from cinema.models import Movie
from cinema.serializers import MovieSerializer


@api_view(http_method_names=["POST"])
def cinema_create(request):
    if request.method == "POST":
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=HTTPStatus.CREATED)
        return JsonResponse(serializer.errors, status=HTTPStatus.BAD_REQUEST)


@api_view(http_method_names=["GET", "PUT", "DELETE"])
def cinema_get_put_delete(request, pk):
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return HttpResponse(HTTPStatus.NOT_FOUND)

    if request.method == "GET":
        serializer = MovieSerializer(movie)
        return JsonResponse(serializer.data, status=HTTPStatus.OK)

    if request.method == "PUT":
        serializer = MovieSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=HTTPStatus.ACCEPTED)
        return JsonResponse(serializer.errors, status=HTTPStatus.BAD_REQUEST)

    if request.method == "DELETE":
        pass






