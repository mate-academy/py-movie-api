from django.contrib import admin
from django.contrib.auth.models import Group

from cinema.models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "duration", ]


admin.site.unregister(Group)
