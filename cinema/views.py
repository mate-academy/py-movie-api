from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.generics import get_object_or_404
from rest_framework import status

from models import Movie
from serializers import MovieSerializer


@api_view(["GET", "POST"])
def cinema_list(request):
    if request.method == "GET":
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return JsonResponse(serializer.data,
                        status=status.HTTP_200_OK)
    else:
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,
                            status=status.HTTP_201_CREATED)
        return JsonResponse(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["GET", "PUT", "DELETE"])
def cinema_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == "GET":
        serializer = MovieSerializer(movie)
        return JsonResponse(serializer.data,
                            status=200)
    elif request.method == "PUT":
        serializer = MovieSerializer(movie,
                                     data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,
                            status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors,
                               status=status.HTTP_400_BAD_REQUEST)
    else:
        movie.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT)
