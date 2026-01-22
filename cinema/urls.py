from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import MovieViewSet

router = DefaultRouter()
# Registra o ViewSet, criando as rotas /movies/ e /movies/<pk>/
router.register(r"movies", MovieViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
