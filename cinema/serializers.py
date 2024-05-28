from typing import Dict, Any

from rest_framework import serializers

from cinema.models import Movie


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    description = serializers.CharField()
    duration = serializers.IntegerField()

    def create(self, validated_data: Dict[str, Any]) -> Movie:
        return Movie.objects.create(**validated_data)

    def update(self, instance: Movie, validated_data: Dict[str, Any]) -> Movie:
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.duration = validated_data.get("duration", instance.duration)
        instance.save()
        return instance
