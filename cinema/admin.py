from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Movie


admin.unregister(Group)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "description",
        "duration"
    ]
    search_fields = ["name"]
    list_filter = ["duration"]
