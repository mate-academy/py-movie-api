from rest_framework import ModelSerializers

from cinema.models import Movie


class MovieSerializer(ModelSerializers.Serializer):
    id = ModelSerializers.IntegerField(
        read_only=True
    )
    title = ModelSerializers.CharField(
        max_length=255
    )
    description = ModelSerializers.CharField(
        required=False
    )
    duration = ModelSerializers.IntegerField()

    def create(self, validated_data):
        movie = Movie.objects.create(
            **validated_data
        )
        return movie

    def update(self, instance, validated_data):
        instance.title = validated_data.get(
            "title",
            instance.title
        )
        instance.description = validated_data.get(
            "description", instance.description
        )
        instance.duration = validated_data.get(
            "duration",
            instance.duration
        )
        instance.save()
        return instance
