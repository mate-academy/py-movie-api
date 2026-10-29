import json

from django.http import JsonResponse
from rest_framework.generics import get_object_or_404

from cinema.models import Movie
from cinema.serializer import MovieSerializer


def movie_list(request):
    if request.method == "GET":
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)

        return JsonResponse(serializer.data, status=200, safe=False)
    elif request.method == "POST":
        movie_data = request.body
        movie_dict = json.loads(movie_data)
        serializer = MovieSerializer(data=movie_dict)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({"success": True}, status=200)
        else:
            return JsonResponse(serializer.errors, status=400)


def movie_detail(request, pk):
    if request.method == "GET":
        movie_info = get_object_or_404(Movie, pk=pk)
        serializer = MovieSerializer(movie_info)
        return JsonResponse(data=serializer.data, status=200, safe=False)
    elif request.method == "PUT":
        movie = get_object_or_404(Movie, pk=pk)
        update_info = json.loads(request.body)
        serializer = MovieSerializer(movie, update_info, partial=True)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse(serializer.data, status=200)
        else:
            return JsonResponse(serializer.errors, status=400)
    elif request.method == "DELETE":
        movie = get_object_or_404(Movie, pk=pk)
        movie.delete()
        return JsonResponse({"success": True}, status=200)

