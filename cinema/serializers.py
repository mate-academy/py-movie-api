from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, max_length=63)
    description = serializers.CharField(required=False, max_length=255)
    duration = serializers.IntegerField(required=True)