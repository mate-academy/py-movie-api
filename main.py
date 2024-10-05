from rest_framework.parsers import JSONParser
import io

from rest_framework.renderers import JSONRenderer

from cinema.models import Movie
from cinema.serializer import MovieSerializer


def serialize_car_object(movie: Movie) -> bytes:
    serializer = MovieSerializer(movie)
    json = JSONRenderer().render(serializer.data)
    return json


def deserialize_car_object(json: bytes) -> Movie:
    stream = io.BytesIO(json)
    data = JSONParser().parse(stream)
    serializer = MovieSerializer(data=data)
    if serializer.is_valid():
        return serializer.save()
    else:
        raise ValueError(f"Invalid data: {serializer.errors}")
