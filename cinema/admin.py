from django.contrib import admin

from cinema.models import Movie


@admin.register(Movie)
class AdminCinema(admin.ModelAdmin):
    pass
