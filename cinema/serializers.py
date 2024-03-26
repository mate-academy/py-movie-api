from rest_framework import serializers
from cinema.models import Movie


class MovieSeerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    description = serializers.CharField(max_length=255, required=False)
    duration = serializers.IntegerField(required=True)

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.duration = validated_data.get("duration", instance.duration)
        instance.save()
        return instance