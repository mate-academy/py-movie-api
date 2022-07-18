from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from cinema.models import Movie

admin.site.register(Movie)
