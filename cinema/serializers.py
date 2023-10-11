from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    description = serializers.CharField(required=False)
    duration = serializers.IntegerField(required=False)

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get(
            "title", instance.title
        )
        instance.description = validated_data.get(
            "description", instance.title
        )
        instance.duration = validated_data.get(
            "duration", instance.title
        )
        instance.save()
        return instance
