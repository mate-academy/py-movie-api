from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from cinema.models import Movie


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(
        max_length=100,
        validators=[UniqueValidator(queryset=Movie.objects.all())]
    )
    description = serializers.CharField(max_length=255)
    duration = serializers.IntegerField()

    def create(self, validated_data) -> Movie:
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data) -> Movie:
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.duration = validated_data.get('duration', instance.duration)
        instance.save()
        return instance
