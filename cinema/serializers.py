from django.core.validators import MinValueValidator
from rest_framework import serializers

from cinema.models import Movie


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, max_length=255)
    description = serializers.CharField(required=True)
    duration = serializers.IntegerField(
        required=True,
        validators=[MinValueValidator(1)]
    )

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance)
        instance.description = validated_data.get("description", instance)
        instance.duration = validated_data.get("duration", instance)
        instance.save()
        return instance
