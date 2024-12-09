from rest_framework import serializers
from cinema.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ["title", "description", "duration"]