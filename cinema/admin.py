from django.contrib import admin
from django.contrib.auth.models import Group

from cinema.models import Movie

admin.site.register(Movie)
admin.site.unregister(Group)
