from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from cinema.models import Movie
from cinema.serializers import MovieSerializer


@api_view(["GET", "POST"])
def movies_list(request):
    if request.method == "GET":
        movies = Movie.objects.all()
        serializers = MovieSerializer(movies, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    if request.method == "POST":
        serializers = MovieSerializer(data=request.data)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)

        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def movies_detail(request, pk):
    if request.method == "GET":
        movie = Movie.objects.get(pk=pk)
        serializers = MovieSerializer(movie)
        return Response(serializers.data, status=status.HTTP_200_OK)

    if request.method == "PUT":
        movie = Movie.objects.get(pk=pk)
        serializers = MovieSerializer(movie, data=request.data)

        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data, status=status.HTTP_200_OK)

    if request.method == "DELETE":
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
