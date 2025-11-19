from django.contrib import admin
from .models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "duration"]
    list_display_links = ["id", "title"]
    search_fields = ["title", "description"]
    list_filter = ["duration"]
