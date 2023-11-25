from rest_framework import serializers

from cinema.models import Movie


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=60)
    description = serializers.CharField(required=False)
    duration = serializers.IntegerField()

    def create(self, validated_data):
        Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("info", instance)
        instance.description = validated_data.get("description", instance)
        instance.duration = validated_data.get("duration", instance)
        instance.save()
        return instance
