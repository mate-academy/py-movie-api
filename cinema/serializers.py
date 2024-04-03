from rest_framework import serializers
from cinema.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, max_length=255)
    description = serializers.CharField(required=False, max_length=255)
    duration = serializers.IntegerField(required=True)

    def create(self: Movie, validated_data: dict) -> Movie:
        return Movie.objects.create(**validated_data)

    def update(self: Movie, instance: Movie.objects,
               validated_data: dict) -> Movie:
        instance.title = validated_data.get('title', instance)
        instance.description = validated_data.get(
            'description', instance.description)
        instance.duration = validated_data.get('duration', instance.duration)
        instance.save()
        return instance
