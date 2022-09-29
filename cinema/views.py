from http import HTTPStatus

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from cinema.serializers import MovieSerializer


@api_view(http_method_names=["POST"])
def cinema_create(request):
    if request.method == "POST":
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=HTTPStatus.CREATED)
        return JsonResponse(serializer.errors, status=HTTPStatus.BAD_REQUEST)

