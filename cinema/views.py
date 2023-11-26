from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from cinema.models import Movie
from cinema.serializers import MovieSerializer


class MovieCRUDView(APIView):
    model = Movie
    serializer_class = MovieSerializer

    def get_object(self, pk: int):
        return get_object_or_404(self.model, pk=pk)

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        if pk is not None:
            movie = self.get_object(pk)
            serializer = self.serializer_class(movie)
        else:
            movies = self.model.objects.all()
            serializer = self.serializer_class(movies, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

    def put(self, request, *args, **kwargs):
        movie = self.get_object(kwargs.get("pk"))
        serializer = self.serializer_class(movie, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        movie = self.get_object(kwargs.get("pk"))
        movie.delete()
        return Response(
            {"message": "Movie deleted successfully."},
            status=status.HTTP_204_NO_CONTENT
        )
