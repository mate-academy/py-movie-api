"""Serializers for cinema API resources."""

from __future__ import annotations

from rest_framework import serializers

from cinema.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    """Validate and transform Movie instances for JSON responses."""

    class Meta:
        """Serializer metadata."""

        model = Movie
        fields: tuple[str, ...] = ("id", "title", "description", "duration")
        read_only_fields: tuple[str, ...] = ("id",)
