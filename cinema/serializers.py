from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"

    def validate_duration(self, value):
        """Garante que a duração seja um número positivo."""
        if value <= 0:
            # Levanta um erro de validação que o DRF tratará como 400 Bad Request
            raise serializers.ValidationError("A duração do filme deve ser maior que 0 minutos.")
        return value
