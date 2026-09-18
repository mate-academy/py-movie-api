"""Cinema admin registration."""
from __future__ import annotations
from django.contrib import admin
from cinema.models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    """Admin display settings for movies."""
    list_display: tuple[str, ...] = ("id", "title", "duration")
    search_fields: tuple[str, ...] = ("title",)
