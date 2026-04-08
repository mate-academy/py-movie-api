from rest_framework import serializers
from cinema.models import Movie

# class BusSerializer(serializers.Serializer):
#    id = serializers.IntegerField(read_only=True)
#    info = serializers.CharField(required=True)
#    num_seats = serializers.IntegerField(required=True)
#
#    def create(self, validated_data):
#        return Bus.objects.create(**validated_data)
#
#    def update(self, instance, validated_data):
#        instance.info = validated_data.get("info", instance.info)
#        instance.num_seats = validated_data.get(
#            "num_seats",
#            instance.num_seats
#        )
#        instance.save()
       # return instance

class MovieSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='title', read_only=True)
    description = serializers.CharField(source='description', read_only=True)
    duration = serializers.CharField(source='duration', read_only=True)

