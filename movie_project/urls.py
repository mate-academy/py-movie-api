from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect


urlpatterns = [
    path('', lambda request: redirect('/api/cinema/movies/'), name='home'),
    path('admin/', admin.site.urls),
    path('', include('cinema.urls')),
]
