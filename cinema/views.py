from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404

from cinema.models import Movie
from cinema.serializers import MovieSerialer


@api_view(["GET", "POST"])
def movie_list(request):
    if request.method == "GET":
        movies = Movie.objects.all()
        serializer = MovieSerialer(movies, many=True)
        return Response(serializer.data,
                        status=status.HTTP_200_OK)
    else:
        serializer = MovieSerialer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def movie_detail(request, pk: int):
    movie = get_object_or_404(Movie, id=pk)
    if request.method == "GET":
        serializer = MovieSerialer(movie)
        return Response(serializer.data,
                        status=status.HTTP_200_OK)
    elif request.method == "PUT":
        serializer = MovieSerialer(movie,
                                   data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_200_OK)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
    else:
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
