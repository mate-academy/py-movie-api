from http import HTTPStatus

from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view


from cinema.models import Movie
from cinema.serializers import MovieSerializer


@api_view(http_method_names=["POST"])
def cinema_create(request):
    if request.method == "POST":
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=HTTPStatus.CREATED)
        return JsonResponse(serializer.errors, status=HTTPStatus.BAD_REQUEST)


@api_view(http_method_names=["GET", "PUT", "DELETE"])
def cinema_get_put_delete(request, pk):
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return HttpResponse(HTTPStatus.NOT_FOUND)

    if request.method == "GET":
        serializer = MovieSerializer(movie)
        return JsonResponse(serializer.data, status=HTTPStatus.OK)

    if request.method == "PUT":
        serializer = MovieSerializer(movie, request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=HTTPStatus.ACCEPTED)
        return JsonResponse(serializer.errors, status=HTTPStatus.BAD_REQUEST)

    if request.method == "DELETE":
        movie.delete()
        return HttpResponse(status=HTTPStatus.NO_CONTENT)
