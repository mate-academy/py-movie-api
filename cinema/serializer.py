from rest_framework import serializers

from cinema.models import Movie


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True)
    duration = serializers.DurationField(required=True)

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.duration = validated_data.get('duration', instance.duration)
        instance.description = validated_data.get(
            'description',
            instance.description
        )
        instance.save()
        return instance
