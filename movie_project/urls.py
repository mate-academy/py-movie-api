from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    # Endpoint raiz: api/cinema/movies/
    path("api/cinema/", include("cinema.urls")),
]
