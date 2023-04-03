from rest_framework import serializers

from cinema.models import Movie


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, max_length=100)
    description = serializers.CharField(
        max_length=255,
        required=False,
        allow_blank=True,
        default="",
    )
    duration = serializers.IntegerField()

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title")
        instance.description = validated_data.get("description")
        instance.duration = validated_data.get("duration")
        instance.save()
        return instance
