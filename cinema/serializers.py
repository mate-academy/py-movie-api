from __future__ import annotations
from rest_framework import serializers

from cinema.models import Movie


class MovieSerializer(serializers.Serializer):
    movie_id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, max_length=100)
    description = serializers.CharField(required=True)
    duration = serializers.IntegerField()

    def create(self: MovieSerializer, validated_data: dict) -> Movie:
        return Movie.objects.create(**validated_data)

    def update(
            self: MovieSerializer,
            instance: Movie,
            validated_data: dict
    ) -> Movie:
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get(
            'description', instance.description
        )
        instance.duration = validated_data.get('duration', instance.duration)
        instance.save()
        return instance
