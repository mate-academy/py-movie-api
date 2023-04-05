from django.urls import path

from cinema.views import MovieAPI, MovieListAPIView

urlpatterns = [
    path("movies/", MovieListAPIView.as_view()),
    path("movies/<int:pk>/", MovieAPI.as_view()),
]

app_name = "cinema"
