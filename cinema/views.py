from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from cinema.models import Movie
from cinema.serializers import MovieSerializer


@api_view(["GET", "POST"])
def movie_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Movie.objects.all()
        serializer = MovieSerializer(snippets, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':

        serializer = MovieSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = MovieSerializer(movie)

        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        movie.delete()

        return HttpResponseRedirect(reverse("cinema:movie_list"))
