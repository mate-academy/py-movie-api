from rest_framework import serializers

from cinema.models import Movie


class MovieSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.duration = validated_data.get("duration", instance.duration)
        instance.save()
        return instance

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration")
