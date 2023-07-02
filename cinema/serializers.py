from cinema.models import Movie
from django.db.models import QuerySet
from rest_framework import serializers


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True)
    description = serializers.CharField(required=False)
    duration = serializers.DecimalField(
        max_digits=5, decimal_places=2, required=True
    )

    def create(self, validated_data) -> QuerySet:
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data) -> dict:
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get(
            "description", instance.description
        )
        instance.duration = validated_data.get("duration", instance.duration)
        instance.save()
        return instance
