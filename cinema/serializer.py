from rest_framework import serializers
from cinema.models import Movie


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, max_length=63)
    description = serializers.CharField(required=False, max_length=255)
    duration = serializers.DurationField(required=True)

    def create(self, validate_data):
        return Movie.objects.create(**validate_data)

    def update(self, instance, validate_data):
        instance.info = validate_data.get("info", instance.info)
        instance.num_seats = validate_data.get("num_seats", instance.num_seats)
        instance.save()
        return instance
