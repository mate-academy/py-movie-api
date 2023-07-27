from rest_framework import serializers
from cinema.models import Movie


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True)
    duration = serializers.IntegerField()

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.info)
        instance.duration = validated_data.get("duration", instance.duration)

        instance.save()
        return instance



# class BusSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     info = serializers.CharField(required=False)
#     num_seats = serializers.IntegerField(required=True)
#
#     # validated_data - хранится инфо для создания Bus по BusSerializers
#     def create(self, validated_data):
#         return Bus.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         # если не передаем значение, то будет старое
#         instance.info = validated_data.get("info", instance.info)
#         instance.num_seats = validated_data.get("num_seats", instance.num_seats)
#         instance.save()
#         return instance