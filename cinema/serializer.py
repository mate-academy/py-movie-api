from rest_framework import serializers
from cinema.models import Movie


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    duration = serializers.IntegerField(required=False)

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.info = validated_data.get("title", instance.title)
        instance.info = validated_data.get("description", instance.description)
        instance.info = validated_data.get("duration", instance.duration)

        instance.save()
        return instance
