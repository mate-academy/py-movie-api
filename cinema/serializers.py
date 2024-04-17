from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=200, required=True)
    description = serializers.CharField(max_length=255, required=False)
    duration = serializers.IntegerField(required=False)

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.duration = validated_data.get("duration", instance.duration)
        instance.save()
        return instance

    class Meta:
        model = Movie
        fields = ["id", "title", "description", "duration"]
