from rest_framework import serializers
from cinema.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    description = serializers.CharField()
    duration = serializers.IntegerField()

    class Meta:
        model = Movie
        fields = "__all__"

    def create(self, validated_data):
        movie = Movie.objects.create(**validated_data)
        return movie

    def update(self, instance, validated_data):
        instance.description = validated_data.get("description", instance.description)
        instance.duration = validated_data.get("duration", instance.duration)
        instance.save()
        return instance
