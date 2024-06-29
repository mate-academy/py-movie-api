from rest_framework import serializers
from cinema.models import Movies

class MoviesSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, max_length=255)
    description = serializers.CharField(required=False, max_length=255)
    duration = serializers.IntegerField(required=True)

    class Meta:
        model = Movies
        fields = "__all__"

    def create(self, validated_data):
        return Movies.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.duration = validated_data.get("duration", instance.duration)
        instance.save()
        return instance
