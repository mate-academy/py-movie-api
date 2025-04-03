from rest_framework import serializers
from cinema.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    title = serializers.CharField(read_only=True)
    description = serializers.CharField(required=False, max_length=255)
    duration = serializers.IntegerField(required=True)

    class Meta:
        model = Movie
        fields = ["id", "title", "description", "duration"]

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.description = validated_data.get(
            "description", instance.description
        )
        instance.duration = validated_data.get("duration", instance.duration)
        instance.save()
        return instance
