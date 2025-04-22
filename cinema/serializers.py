from rest_framework import serializers
from cinema.models import Movie


class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ["id", "title", "description", "duration"]
        read_only_fields = ["id"]
