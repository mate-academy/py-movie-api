from django.urls import path

from cinema.views import MovieCRUDView

urlpatterns = [
    path("movies/", MovieCRUDView.as_view(), name="create-and-list"),
    path("movies/<pk>/", MovieCRUDView.as_view(), name="RUD"),
]

app_name = "cinema"
