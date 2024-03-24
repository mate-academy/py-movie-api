from rest_framework import serializers

from cinema.models import Movie


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(required=False)
    duration = serializers.IntegerField(min_value=1)

    def create(self, validated_data):
        """
        Create & return a new "Movie` instance, given the validated data.
        """
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update & return an existing "Movie" instance, given the validated data.
        """
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description",
                                                  instance.description)
        instance.duration = validated_data.get("duration", instance.duration)
        instance.save()
        return instance
