from django.template.defaultfilters import title
from rest_framework import serializers
from cinema.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, max_length=255)
    description = serializers.CharField(required=False)
    duration = serializers.IntegerField(required=True)

    class Meta:
        model = Movie
        fields = ["id", "title", "description", "duration"]

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        title= validated_data.get("title", instance.title)
        instance.description = validated_data.get(
            "description", instance.description
        )
        duration = validated_data.get("duration", instance.duration)
        instance.save()
        return instance
