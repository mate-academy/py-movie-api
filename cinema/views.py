from rest_framework import status
from rest_framework.decorators import api_view
from cinema.models import Movie
from cinema.serializers import MovieSerializer
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response


# Create your views here.
@api_view(["GET", "POST"])
def movie_list(request):
    if request.method == "GET":
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(["GET", "PUT", "DELETE"])
def movie_detail(request, pk):
    cinema = get_object_or_404(Movie, pk=pk)
    if request.method == "GET":
        serializer = MovieSerializer(cinema)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == "PUT":
        serializer = MovieSerializer(cinema, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        cinema.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)