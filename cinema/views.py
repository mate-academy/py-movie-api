import json

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from cinema.models import Movie
from cinema.serializers import MovieSerializer


def movie_list(request):
    if request.method == "GET":
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return JsonResponse(data=serializer.data, safe=False)
    elif request.method == "POST":
        movie_data = request.body
        movie_dict = json.loads(movie_data)
        serializer = MovieSerializer(data=movie_dict)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"success": True}, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)
    return None


def movie_detail(request, pk):
    if request.method == "GET":
        movie = get_object_or_404(Movie, pk=pk)
        serializer = MovieSerializer(movie)
        return JsonResponse(data=serializer.data)
    elif request.method == "PUT":
        movie = get_object_or_404(Movie, pk=pk)
        update_data = json.loads(request.body)
        serializer = MovieSerializer(movie, data=update_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)
    elif request.method == "DELETE":
        movie = get_object_or_404(Movie, pk=pk)
        movie.delete()
        return JsonResponse({"success": True}, status=204)
    return None
