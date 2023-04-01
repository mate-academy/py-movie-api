from cinema.models import Movie
from cinema.serializers import MovieSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


@api_view(["GET", "POST", "PUT", "DELETE"])
def movie_list(request, pk=None):
    if request.method == "GET" and pk:
        movie = get_object_or_404(Movie, pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "GET":
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        serializer = MovieSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "PUT":
        movie = get_object_or_404(Movie, pk)
        serializer = MovieSerializer(movie, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        movie = get_object_or_404(Movie, pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



