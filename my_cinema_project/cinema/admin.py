from django.contrib import admin

from cinema.models import Movie


class MovieAdmin(admin.ModelAdmin):
    pass


admin.site.register(Movie, MovieAdmin)
