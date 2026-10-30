from rest_framework import serializers
from cinema.models import Movie
from typing import Any

class MovieSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, max_length=255)
    description = serializers.CharField(required=False)
    duration = serializers.IntegerField(required=False)

    def create(self, validated_data: dict[str, Any]) -> Movie:
        return Movie.objects.create(**validated_data)

    def update(self, instance: Movie, validated_data: dict[str, Any]) -> Movie:
        instance.title = validated_data.get("title", instance.title)
        instance.duration = validated_data.get("duration", instance.duration)
        instance.description = validated_data.get(
            "description",
            instance.description
        )
        instance.save()
        return instance

    class Meta:
        model = Movie
        fields = ["id", "title", "description", "duration"]
