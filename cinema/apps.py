"""Application configuration for the cinema app."""

from __future__ import annotations

from django.apps import AppConfig


class CinemaConfig(AppConfig):
    """Configure the cinema application."""

    default_auto_field: str = "django.db.models.BigAutoField"
    name: str = "cinema"
