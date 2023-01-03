from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from cinema.models import Movie
from cinema.serializers import MovieSerializer


@api_view(["GET", "POST"])
def movies_list(request):

    if request.method == "GET":
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == "POST":
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def movie_instance(request, pk):

    if request.method == "GET":
        movie = Movie.objects.get(id=pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == "PUT":
        movie = Movie.objects.get(id=pk)
        serializer = MovieSerializer(instance=movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        movie = Movie.objects.get(id=pk)
        movie.delete()
        return Response(
            {"message": "Article with id `{}` has been deleted.".format(pk)},
            status=status.HTTP_204_NO_CONTENT
        )
