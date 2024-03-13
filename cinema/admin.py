from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from cinema.models import User, Movie


@admin.register(User)
class UserAdmin(UserAdmin):
    pass


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    pass
