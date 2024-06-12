from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import status

from cinema.models import Movie
from cinema.serializers import MovieSerializer
from user.models import User


@api_view(["GET", "POST"])
def movies_list(request):
    if request.method == "GET":
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == "POST":
        serializer = MovieSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def movies_detail(request, pk):

    instance = get_object_or_404(User, id=pk)

    if request.method == "GET":
        serializer = MovieSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == "PUT":
        serializer = MovieSerializer(data=request.data, instance=instance)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_501_NOT_IMPLEMENTED)

    if request.method == "DELETE":
        operation = instance.delete()
        data = {}
        if operation:
            data["success"] = "delete successful"
        else:
            data["failure"] = "delete failed"

        return Response(data=data, status=status.HTTP_200_OK)
