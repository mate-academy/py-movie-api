import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .models import Movie
from .serializers import MovieSerializer


def movie_list(request):

    if request.method == "GET":
        movies = Movie.objects.all()

        serializer = MovieSerializer(movies, many=True)

        return JsonResponse(
            serializer.data,
            status=200,
            safe=False
        )

    elif request.method == "POST":

        movie_data = json.loads(request.body)

        serializer = MovieSerializer(data=movie_data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return JsonResponse(
            serializer.data,
            status=201
        )


def movie_detail(request, pk):

    movie = get_object_or_404(Movie, pk=pk)

    if request.method == "GET":

        serializer = MovieSerializer(movie)

        return JsonResponse(
            serializer.data,
            status=200
        )

    elif request.method == "PUT":

        update_data = json.loads(request.body)

        serializer = MovieSerializer(
            movie,
            data=update_data,
            partial=True
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return JsonResponse(
            serializer.data,
            status=200
        )

    elif request.method == "DELETE":

        movie.delete()

        return JsonResponse(
            {"success": True},
            status=204
        )
