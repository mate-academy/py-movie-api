from django.urls import path, include
from rest_framework import routers

from cinema.views import MovieView

router = routers.DefaultRouter()
router.register("movies", MovieView)

urlpatterns = [
    path("api/cinema/", include(router.urls)),
]
