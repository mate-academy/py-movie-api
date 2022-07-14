from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from cinema.models import Cinema
from cinema.serializers import CinemaSerializer
from rest_framework import status


@api_view(['GET', 'POST'])
def movie_list(request):

    if request.method == 'GET':
        cinemas = Cinema.objects.all()
        serializer = CinemaSerializer(cinemas, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CinemaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail(request, pk):

    cinema = get_object_or_404(Cinema, pk=pk)

    if request.method == 'GET':
        serializer = CinemaSerializer(cinema)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CinemaSerializer(cinema, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        cinema.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
