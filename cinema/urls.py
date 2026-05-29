from rest_framework.routers import DefaultRouter

from cinema.views import MovieViewSet

router = DefaultRouter()
router.register("movies", MovieViewSet)

urlpatterns = router.urls
