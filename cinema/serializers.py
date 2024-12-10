from rest_framework import serializers
from cinema.models import Movie


class CinemaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, max_length=255)
    description = serializers.CharField(style={"base_template": "textarea.html"})
    duration = serializers.IntegerField(min_value=0, required=True)

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.duration = validated_data.get("duration", instance.duration)
        instance.save()
        return instance
