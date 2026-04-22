from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from cinema.serializers import MovieSerializer

from cinema.models import Movie


class MovieListView(APIView):
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


class MovieDetailView(APIView):
    def get(self, request, **kwargs):
        movie = Movie.objects.get(id=kwargs.get("pk"))
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, **kwargs):
        movie = Movie.objects.get(id=kwargs.get("pk"))
        serializer = MovieSerializer(movie)
        serializer.update(movie, request.data)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def delete(self, request, **kwargs):
        movie = Movie.objects.get(id=kwargs.get("pk"))
        serializer = MovieSerializer(movie)
        movie.delete()
        return Response(serializer.data, status=status.HTTP_200_OK)
