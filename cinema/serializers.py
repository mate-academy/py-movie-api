from rest_framework import serializers
from cinema.models import Movie


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, max_length=255)
    description = serializers.CharField(required=True, max_length=255)
    duration = serializers.IntegerField(required=True)

    def create(self, validated_data: dict) -> Movie:
        return Movie.objects.create(**validated_data)

    def update(self, instance: Movie, validated_data: dict) -> Movie:
        instance_title = validated_data.get(  # noqa: F841
            "title", instance.title)
        instance_description = validated_data.get(  # noqa: F841
            "description", instance.description)
        instance_duration = validated_data.get(  # noqa: F841
            "duration", instance.duration)
        instance.save()
        return instance
