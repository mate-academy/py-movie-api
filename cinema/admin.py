from django.contrib import admin
from cinema.models import Movie


@admin.register(Movie)
class CinemaAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "description",
        "duration"
    ]
