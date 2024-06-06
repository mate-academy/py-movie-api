from rest_framework import serializers
from cinema.models import Movie


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    description = serializers.CharField(max_length=1000, required=False)
    duration = serializers.IntegerField(required=True)

    def create(self, validated_data: dict) -> Movie:
        return Movie.objects.create(**validated_data)

    def update(self, instance: Movie, validated_data: dict) -> Movie:
        instance.description = validated_data.get(
            "description", instance.description
        )
        instance.duration = validated_data.get("duration", instance.duration)
        instance.save()
        return instance
