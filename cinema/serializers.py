from rest_framework import serializers
from cinema.models import Movie


class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ["id", "title", "description", "duration"]
