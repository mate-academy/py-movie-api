from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from cinema.models import Movie
from cinema.serializers import MovieSerializer


# Create your views here.
@api_view(["GET", "POST"])
def movie_list(request):
    if request.method == "GET":
        movie = Movie.objects.all()
        serializers = MovieSerializer(movie, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    if request.method == "POST":
        serializers = MovieSerializer(data=request.data)

        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "DELETE"])
def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)

    if request.method == "GET":
        serializers = MovieSerializer(movie)
        return Response(serializers.data, status.HTTP_200_OK)

    elif request.method == "PUT":
        serializers = MovieSerializer(movie, data=request.data)

        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data, status.HTTP_201_CREATED)

    elif request.method == "DELETE":
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
