from django.urls import path, include
from rest_framework.routers import DefaultRouter


from cinema.views import MovieViewSet

router = DefaultRouter()
router.register(r"movies", MovieViewSet, basename="movie")

app_name = "cinema"


urlpatterns = [
    path("", include(router.urls)),
]
