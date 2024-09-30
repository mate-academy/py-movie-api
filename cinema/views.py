from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from cinema.models import Movie
from cinema.serializers import MovieSerializer

@api_view(["GET", "POST"])
def movies(request):
    if request.method == 'GET':
        movies_all = Movie.objects.all()
        serializer = MovieSerializer(movies_all, many=True)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
    serializer = MovieSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def movie_details(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)

    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status=200)

    elif request.method == 'PUT':
        serializer = MovieSerializer(
            movie,
            data=request.data,
            raise_exception=True
        )
        serializer.save()
        return Response(
                serializer.data,
                status=status.HTTP_200_OK
        )

    movie.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
