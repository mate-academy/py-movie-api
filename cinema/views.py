from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.http import HttpResponse

from cinema.models import Movie
from cinema.serializers import MovieSerializer


@api_view(["GET", "POST"])
def bus_list(request):
    if request.method == "GET":
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == "POST":
        serializer = MovieSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer, status.HTTP_201_CREATED)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def bus_info(request, pk):
    try:
        movie = Movie.objects.get(id=pk)
    except Movie.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status.HTTP_200_OK)

    elif request.method == "PUT":
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)

        return Response(status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        movie.delete()
        return HttpResponse(status=204)
