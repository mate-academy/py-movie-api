from rest_framework.parsers import JSONParser
import io

from rest_framework.renderers import JSONRenderer

from cinema.models import Movie
from cinema.serializers import MovieSerializer


def serialize_movie_object(movie: Movie) -> bytes:
    serializer = MovieSerializer(movie)
    json = JSONRenderer().render(serializer.data)
    return json


def deserialize_movie_object(json: bytes) -> Movie:
    stream = io.BytesIO(json)
    data = JSONParser().parse(stream)
    serializer = MovieSerializer(data=data)
    if serializer.is_valid():
        return serializer.save()
    else:
        raise ValueError(f"Invalid data: {serializer.errors}")
