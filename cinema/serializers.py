from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, max_length=255)
    description = serializers.CharField(required=True)
    duration = serializers.IntegerField(required=True)

    class Meta:
        model = Movie
        fields = ["id", "title", "description", "duration"]

    def create(self, validated_data: dict) -> Movie:
        return Movie.objects.create(**validated_data)

    def update(self, instance: Movie, validated_data: dict) -> Movie:
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get(
            "description",
            instance.description
        )
        instance.duration = validated_data.get("duration", instance.duration)
        instance.save()
        return instance
