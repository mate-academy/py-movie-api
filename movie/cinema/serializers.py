from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100, required=True)
    description = serializers.CharField(read_only=True)
    duration = serializers.IntegerField(read_only=True)

    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'duration')


