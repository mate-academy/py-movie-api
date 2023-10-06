from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from cinema.models import Movie
from cinema.serializers import MovieSerializer


@api_view(["Get", "POST"])
def movie_list(request):
	if request.method == "GET":
		movies = Movie.objects.all()
		serializer = MovieSerializer(movies, many=True)
		return Response(serializer.data, status=200)

	if request.method == "POST":
		serializer = MovieSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
