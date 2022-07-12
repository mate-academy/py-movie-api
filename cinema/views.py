from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from cinema.models import Cinema
from cinema.serializers import CinemaSerializer
from rest_framework import status


def movie_list(request):
    if request.method == 'GET':
        movies = Cinema.objects.all()
        serializer = CinemaSerializer(movies, many=True)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)


def one_movie(request, pk):
    if request.method == 'GET':
        movie = Cinema.objects.get(id=pk)
        serializer = CinemaSerializer(movie)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)


@api_view(['POST'])
def movie_add(request):
    if request.method == 'POST':
        serializer = CinemaSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def movie_update(request, pk):
    if request.method == 'PUT':
        movie = Cinema.objects.get(id=pk)
        serializer = CinemaSerializer(movie, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def movie_delete(request, pk):
    if request.method == 'DELETE':
        movie = Cinema.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
