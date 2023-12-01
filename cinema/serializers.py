from rest_framework import serializers

from cinema.models import Movie


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255)
    duration = serializers.IntegerField()

    def create(self, validated_data):
        return Movie.objects.create()

    def update(self, instance, validated_data):
        instance.info = validated_data.get("info", instance.info)
        instance.num_seats = validated_data.get("num_seats", instance.num_seats)
        instance.save()
        return instance
