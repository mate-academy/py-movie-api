from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from cinema.models import Movie
from cinema.serializers import MovieSerializer


@api_view(["GET", "POST"])
def movie_list(request):
    if request.method == "GET":
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=200)

    if request.method == "POST":
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["GET"])
def movie_list_detail(request, pk):
    if request.method == "GET":
        try:
            movie = Movie.objects.get(pk=pk)
            serializer = MovieSerializer(movie, many=False)
            return Response(serializer.data, status=200)
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["PUT"])
def movie_list_update(request, pk):
    if request.method == "PUT":
        try:
            movie = Movie.objects.get(pk=pk)
            movie.update(**request.data)
            serializer = MovieSerializer(movie, many=False)
            return Response(serializer.data, status=200)
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["DELETE"])
def movie_delete(request, pk):
    if request.method == "DELETE":
        try:
            movie = Movie.objects.get(pk=pk)
            movie.delete()
            serializer = MovieSerializer(movie, many=False)

            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
