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
        instance = get_object_or_404(self.model, pk=pk)
        return instance

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
        title = request.data.get("title")
        if self.model.objects.filter(title=title).exists():
            return Response(
                {"error": f"Object with title '{title}' is already exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        movie = self.get_object(kwargs.get("pk"))
        new_title = request.data.get("title")
        if not new_title == movie.title:
            if self.model.objects.filter(title=new_title).exists():
                return Response(
                    {
                        "error": (f"Object with title '{new_title}' "
                                  f"is already exists")
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
        serializer = self.serializer_class(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        movie = self.get_object(kwargs.get("pk"))
        movie.delete()
        return Response(
            {"message": "Movie deleted successfully."},
            status=status.HTTP_204_NO_CONTENT
        )
