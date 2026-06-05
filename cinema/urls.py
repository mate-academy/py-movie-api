from django.urls import path

from cinema import views

urlpatterns = [
    path("movies/", views.movie_list, name="movie-list"),
    path("movies/<pk>/", views.movie_detail, name="movie-detail"),
]
