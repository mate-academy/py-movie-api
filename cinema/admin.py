from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from cinema.models import Movie, User


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    list_display = ("title", "description", "duration", )


admin.site.register(User, UserAdmin)