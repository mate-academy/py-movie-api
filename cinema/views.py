from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from cinema.serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework import status
from cinema.models import Movie


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
        return Response(
            serializers.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["GET", "PUT", "DELETE"])
def movie_detail(request: HttpRequest, pk: int) -> HttpResponse:
    operating_movie = get_object_or_404(Movie, pk=pk)

    if request.method == "GET":
        serializer = MovieSerializer(operating_movie)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == "PUT":
        serializer = MovieSerializer(operating_movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        operating_movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
