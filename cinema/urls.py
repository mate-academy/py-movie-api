from django.urls import path
from cinema.views import MovieAPI

urlpatterns = [
    path("movies/", MovieAPI.as_view()),
    path("movies/<int:pk>/", MovieAPI.as_view()),
]

app_name = "cinema"
