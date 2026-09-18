"""Admin registrations for cinema models."""

from __future__ import annotations

from django.contrib import admin

from cinema.models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    """Admin presentation for Movie records."""

    list_display: tuple[str, ...] = ("id", "title", "duration")
    search_fields: tuple[str, ...] = ("title",)
