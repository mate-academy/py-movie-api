from rest_framework import serializers

from .models import Cinema


class CinemaSeriarizer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(required=False)
    duration = serializers.IntegerField(min_value=1)

    def create(self, validated_data: dict) -> Cinema:
        return Cinema.objects.create(**validated_data)

    def update(self, instance: Cinema, validated_data: dict) -> Cinema:
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get(
            "description",
            instance.description
        )
        instance.duration = validated_data.get("duration", instance.duration)
        instance.save()
        return instance
