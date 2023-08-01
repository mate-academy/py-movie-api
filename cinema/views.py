from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view

from rest_framework.parsers import JSONParser

from cinema.models import Movie
from cinema.serializers import MovieSerializer


@api_view(
    [
        "GET",
        "POST",
    ]
)
def movie_list(request):
    if request.method == "GET":
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        movie_data = JSONParser().parse(request)
        movie_serializer = MovieSerializer(data=movie_data)
        if movie_serializer.is_valid():
            movie_serializer.save()
            return JsonResponse(
                movie_serializer.data, status=status.HTTP_201_CREATED
            )
        return JsonResponse(
            movie_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["GET", "PUT", "DELETE"])
def movie_detail(request, pk):
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return JsonResponse(
            {"message": "The movie does not exist"}, status=status.HTTP_404_NOT_FOUND
        )

    if request.method == "GET":
        serializer = MovieSerializer(movie)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        movie_data = JSONParser().parse(request)
        serializer = MovieSerializer(movie, data=movie_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        movie.delete()
        return JsonResponse(
            {"message": "Movie was deleted successfully!"},
            status=status.HTTP_204_NO_CONTENT,
        )
