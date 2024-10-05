from rest_framework import serializers
from cinema.models import Movie


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, max_length=63)
    description = serializers.CharField(required=False, max_length=255)
    duration = serializers.IntegerField(required=True)

    def create(self, validate_data):
        return Movie.objects.create(**validate_data)

    def update(self, instance, validate_data):
        instance.title = validate_data.get("title", instance.title)
        instance.description = validate_data.get(
            "description",
            instance.description
        )
        instance.duration = validate_data.get("duration", instance.duration)
        instance.save()
        return instance
