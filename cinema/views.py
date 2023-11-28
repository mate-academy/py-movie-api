from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import status
from cinema.models import Movie
from cinema.serializers import MovieSerializer
from django.shortcuts import get_object_or_404
from django.http import HttpRequest, HttpResponse


@api_view(["GET", "POST"])
def movie_list(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        movie = Movie.objects.all()
        serializers = MovieSerializer(movie, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    if request.method == "POST":
        serializers = MovieSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def movie_detail(request: HttpRequest, pk: int) -> HttpResponse:
    movie = get_object_or_404(Movie, pk=pk)

    if request.method == "GET":
        serializer = MovieSerializer(movie)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = MovieSerializer(movie, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        movie.delete()
        return HttpResponse(status=204)
