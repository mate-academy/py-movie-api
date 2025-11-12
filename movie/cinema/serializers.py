from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100, required=True)
    description = serializers.CharField()
    duration = serializers.IntegerField()

    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'duration')


