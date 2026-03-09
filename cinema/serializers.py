from rest_framework import serializers

from cinema.models import Movie


class MovieSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, max_length=255)
    description = serializers.CharField()
    duration = serializers.IntegerField(required=True)

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validate_data):
        instance.title = validate_data["title"]
        instance.description = validate_data["description"]
        instance.duration = validate_data["duration"]
        return instance

