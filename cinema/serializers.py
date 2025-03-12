from rest_framework import serializers
from cinema.models import Movie


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    description = serializers.CharField()
    duration = serializers.IntegerField()

    def create(self, validated_date):
        return Movie.objects.create(**validated_date)

    def update(self, instance, validated_date):
        instance.title = validated_date.get('title', instance.title)
        instance.description = validated_date.get('description', instance.description)
        instance.duration = validated_date.get('duration', instance.duration)
        instance.save()
        return instance
