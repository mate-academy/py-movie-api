from rest_framework import serializers

from cinema.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    description = serializers.CharField(required=False, max_length=255)
    duration = serializers.IntegerField()

    class Meta:
        model = Movie
        fields = ["id", "title", "description", "duration"]

    def create(self, validated_data) -> Movie:
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.duration = validated_data.get("duration", instance.duration)
        instance.save()
        return instance
