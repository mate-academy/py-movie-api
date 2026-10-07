from rest_framework import serializers

from cinema.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(required=False)
    duration = serializers.IntegerField()

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration")
