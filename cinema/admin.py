from django.contrib import admin

from cinema.models import Movie


# Register your models here.
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "duration"]
