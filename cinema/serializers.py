from rest_framework import serializers

from cinema.models import Movie


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=55)
    description = serializers.CharField(
        required=False,
        allow_blank=True,
        style={"base_template": "textarea.html"}
    )
    duration = serializers.IntegerField()

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_date):
        instance.title = validated_date.get("title", instance.title)
        instance.description = validated_date.get("description", instance.description)
        instance.duration = validated_date.get("duration", instance.duration)

        instance.save()
        return instance
