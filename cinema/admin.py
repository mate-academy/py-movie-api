from django.contrib import admin
from cinema.models import Cinema


@admin.register(Cinema)
class CinemaAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "description",
        "duration"
    ]
