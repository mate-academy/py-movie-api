"""
Writing API using class-based views but not use generics
"""
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from cinema.models import Movie
from cinema.serializers import MovieSerializer
from django.shortcuts import get_object_or_404


class MovieList(APIView):
    """Return a list of the all movies & create a new movie based on passed data"""
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieDetail(APIView):
    """Return/Update/Delete a movie with given id"""
    def get(self, request, pk):
        movie = get_object_or_404(Movie, id=pk)
        serializer = MovieSerializer(movie)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        movie = get_object_or_404(Movie, id=pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        movie = get_object_or_404(Movie, id=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
