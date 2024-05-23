from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from cinema.models import Movie
from cinema.serializers import MovieSerializer


@api_view(["GET", "POST"])
def movie_list(request):
    if request.method == "GET":
        buses = Movie.objects.all()
        serializer = MovieSerializer(buses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        serializer = MovieSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def movie_detail(request, pk):
    bus = get_object_or_404(Movie, pk=pk)
    if request.method == "GET":
        serializer = MovieSerializer(bus)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        serializer = MovieSerializer(bus, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "DELETE":
        bus.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
