from rest_framework import serializers

from cinema.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100, required=True)
    duration = serializers.IntegerField(required=True)

    class Meta:
        model = Movie
        fields = '__all__'

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
