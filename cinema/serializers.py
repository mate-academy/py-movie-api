from rest_framework import serializers
from cinema.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=1000)
    duration = serializers.IntegerField()

    class Meta:
        model = Movie
        fields = ["id", "title", "description", "duration"]
