from django.urls import path
from .views import movies, movie_detail

urlpatterns = [
    path("", movies, name="movies-list"),
    path("<int:pk>/", movie_detail, name="movies-detail"),
]

app_name = "cinema"
