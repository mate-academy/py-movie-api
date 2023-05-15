from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view

from cinema.models import Movie
from cinema.serializers import MovieSerializer


@api_view(["GET", "POST"])
def movies_list(request):
    if request.method == "GET":
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)

    if request.method == "POST":
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED, safe=False)

        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)


@api_view(["GET", "POST", "PUT", "DELETE"])
def movie_update(request, pk):
    if request.method == "GET":
        movie = get_object_or_404(Movie, pk=pk)
        serializer = MovieSerializer(movie)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)

    if request.method == "PUT":
        movie = get_object_or_404(Movie, pk=pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)

        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)

    if request.method == "DELETE":
        get_object_or_404(Movie, pk=pk).delete()

        return JsonResponse("Deleted", status=status.HTTP_200_OK, safe=False)
