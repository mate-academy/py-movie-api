from rest_framework import serializers

from cinema.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100, required=False)
    description = serializers.CharField(required=False)
    duration = serializers.IntegerField(required=False)

    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'duration')

    def create(self, validated_data) -> Movie:
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data) -> Movie:
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get(
            'description', instance.description
        )
        instance.duration = validated_data.get('duration', instance.duration)
        instance.save()
        return instance
