from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from cinema.models import Movie
from cinema.serializers import MovieSerializer
from rest_framework import status


@api_view(["GET", "POST"])
def movie_list(request):
    match request.method:
        case "GET":
            movies = Movie.objects.all()
            serializer = MovieSerializer(movies, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        case "POST":
            serializer = MovieSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "DELETE"])
def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    match request.method:
        case "GET":
            serializer = MovieSerializer(movie)
            return Response(serializer.data, status=status.HTTP_200_OK)
        case "PUT":
            serializer = MovieSerializer(movie, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        case "DELETE":
            movie.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
