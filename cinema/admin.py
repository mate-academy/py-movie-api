from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Movie


admin.site.register(Movie)

admin.site.register(User, UserAdmin)
