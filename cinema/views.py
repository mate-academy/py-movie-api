from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from cinema.models import Movie
from cinema.serializers import CinemaSerializer


# Create your views here.
@api_view(["GET", "POST"])
def cinema_list(request):
    if request.method == "GET":
        movies = Movie.objects.all()
        serializer = CinemaSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == "POST":
        serializer = CinemaSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def cinema_retrieve(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == "GET":
        serializer = CinemaSerializer(movie)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = CinemaSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
