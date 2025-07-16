from django.contrib import admin
from .models import Movie

# Регистрируем модель Movie в админке
admin.site.register(Movie)
