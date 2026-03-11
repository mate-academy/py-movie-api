from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet

router = DefaultRouter()
router.register("movies", MovieViewSet)

urlpatterns = [
    path("cinema/", include(router.urls)),
]
