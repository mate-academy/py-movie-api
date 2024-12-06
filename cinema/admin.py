from django.contrib import admin

from cinema.models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_filter = ("duration",)
    search_fields = ("title",)
