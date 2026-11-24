from rest_framework import serializers
from cinema.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(required=True)
    duration = serializers.IntegerField(required=True)

    class Meta:
        model = Movie
        fields = ["id", "title", "description", "duration"]
