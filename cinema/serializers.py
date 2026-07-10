from rest_framework import serializers

from cinema.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    description = serializers.CharField()
    duration = serializers.IntegerField()

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, old_value, validated_data):
        old_value.title = validated_data.get("title", old_value.title)
        old_value.description = validated_data.get("description", old_value.description)
        old_value.duration = validated_data.get("duration", old_value.duration)
        old_value.save()
        return old_value

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration")
