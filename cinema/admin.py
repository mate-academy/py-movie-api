from django.contrib import admin

from cinema.models import Movie


@admin.register(Movie)
class AdminMovie(admin.ModelAdmin):
    pass
