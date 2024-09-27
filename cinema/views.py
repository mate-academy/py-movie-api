from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from cinema.models import Movie
from cinema.serializers import MovieSerializer


@api_view(["GET", "POST"])
def movie_list(request):
    if request.method == "GET":
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    if request.method == "POST":
        serializer = MovieSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def movie_detail(request, pk: int):
    instance = get_object_or_404(Movie, pk=pk)

    if request.method == "GET":
        serializer = MovieSerializer(instance)

        return Response(serializer.data, status.HTTP_200_OK)

    if request.method == "PUT":
        serializer = MovieSerializer(instance=instance, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        instance.delete()

        return Response(status.HTTP_204_NO_CONTENT)
