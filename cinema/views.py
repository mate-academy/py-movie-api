from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from cinema.models import Movie
from cinema.serializers import MovieSerializer


@api_view(["GET", "POST"])
def movie_list(request):
    if request.method == "GET":
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    if request.method == "POST":
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )


@api_view(["GET", "PUT", "DELETE"])
def movie_by_id(request, pk):
    if request.method == "GET":
        try:
            movie = Movie.objects.get(id=pk)
            serializer = MovieSerializer(movie)
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
        except Movie.DoesNotExist:
            return Response(
                {"error": "Movie not found"},
                status=status.HTTP_404_NOT_FOUND
            )

    if request.method == "PUT":
        movie = Movie.objects.get(id=pk)
        serializer = MovieSerializer(
            movie,
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
