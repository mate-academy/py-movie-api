from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from cinema.models import Movie
from cinema.serializers import MovieSerializer


@api_view(["GET", "POST"])
def cinema_list(request):
    if request.method == "GET":
        cinema_all = Movie.objects.all()
        serializer = MovieSerializer(cinema_all, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == "POST":
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def cinema_detail(request, pk):
    film = Movie.objects.get(pk=pk)
    if request.method == "GET":
        serializer = MovieSerializer(film, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == "PUT":
        serializer = MovieSerializer(film, data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        film.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
