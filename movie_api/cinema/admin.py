from django.contrib import admin
from .models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'duration', 'id', 'get_description_preview')
    list_filter = ('duration',)
    search_fields = ('title', 'description')
    list_display_links = ('title', 'duration')
    readonly_fields = ('id',)

    def get_description_preview(self, obj):
        return f'{obj.description[:50]}...' \
            if len(obj.description) > 50 else obj.description
    get_description_preview.short_description = 'Description (View)'
