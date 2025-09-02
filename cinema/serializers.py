from rest_framework import serializers

from cinema.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField()
    duration = serializers.IntegerField()

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'duration']
