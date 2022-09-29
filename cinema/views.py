from http import HTTPStatus

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from cinema.serializers import MovieSerializer


@csrf_exempt
def cinema_create(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        serializer = MovieSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=HTTPStatus.CREATED)
        return JsonResponse(serializer.errors, status=HTTPStatus.BAD_REQUEST)
