from rest_framework import serializers

from cinema.models import Movie


class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        id = serializers.IntegerField(read_only=True)
        title = serializers.CharField(max_length=50, required=True)
        description = serializers.CharField(max_length=500, required=True)
        duration = serializers.IntegerField(required=True)

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get(
            "description",
            instance.description
        )
        instance.duration = validated_data.get(
            "duration",
            instance.duration
        )
        instance.save()
        return instance
