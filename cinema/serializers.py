from rest_framework import serializers

from cinema.models import Movie


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255, required=True)
    description = serializers.CharField(required=True)
    duration = serializers.IntegerField(required=True)

# в validated_data записуються всі поля з моделі Movie
    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # екземпляр Movie
        instance.title = validated_data.get("title", instance.title)
        # якщо не предали нового значення то по дефолту старе значення instance.title
        instance.description = validated_data.get(
            "description",
            instance.description
        )
        instance.duration = validated_data.get(
            "duration",
            instance.duration
        )
        instance.save()
        return instance
