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
        tutorials = Movie.objects.all()
        serializer = MovieSerializer(tutorials, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = MovieSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(
                tutorial_serializer.data, status=status.HTTP_201_CREATED
            )
        return JsonResponse(
            tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST
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
        tutorial_data = JSONParser().parse(request)
        serializer = MovieSerializer(movie, data=tutorial_data)
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
