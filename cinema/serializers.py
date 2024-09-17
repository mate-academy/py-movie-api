from rest_framework import serializers

from cinema.models import Movie


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(required=False, allow_blank=True)
    duration = serializers.IntegerField()

    def validate_title(self, value):
        old_title = None
        if self.instance:
            old_title = self.instance.title
        if value != old_title and Movie.objects.filter(title=value).exists():
            raise serializers.ValidationError(
                f"The movie with title '{value}' is already exists"
            )

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.description = validated_data.get(
            "description",
            instance.description
        )
        instance.duration = validated_data.get("duration", instance.duration)
        instance.save()
        return instance
