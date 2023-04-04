from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from . import models
from . import serializers


@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == 'GET':
        movies = models.Movie.objects.all()
        serializer = serializers.MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = serializers.MovieSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail(request, pk):
    try:
        movie = models.Movie.objects.get(pk=pk)
    except models.Movie.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = serializers.MovieSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = serializers.MovieSerializer(movie, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'DELETE':
        movie.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
