from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True, max_length=255)
    description = serializers.CharField(required=False)
    duration = serializers.IntegerField(required=True, help_text="Duration in minutes")

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'duration']

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.duration = validated_data.get('duration', instance.duration)
        instance.save()
        return instance

    def validate_duration(self, value):
        if value <= 0:
            raise serializers.ValidationError("Duration must be a positive integer.")
        return value
