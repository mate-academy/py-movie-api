from rest_framework import serializers
from movie.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(
        max_length=250, required=False, allow_blank=True
    )
    duration = serializers.IntegerField()

    class Meta:
        model = Movie
        fields = ["id", "title", "description", "duration"]

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description",
                                                  instance.description)
        instance.director = validated_data.get("director", instance.director)
        instance.save()
        return instance
