from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cinema.views import MovieViewSet

router = DefaultRouter()
router.register(r"api/cinema/movies", MovieViewSet, basename="movie")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
