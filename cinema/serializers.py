from rest_framework import serializers

from cinema.models import Movie


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()
    duration = serializers.IntegerField(min_value=1)

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for field in validated_data:
            setattr(instance, field, validated_data[field])

        instance.save()
        return instance
