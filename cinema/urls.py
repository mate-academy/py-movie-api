from django.urls import path

from cinema import views

urlpatterns = [
    path("movies/", views.movie_list, name="movies-list"),
    path("movies/<pk>/", views.movie_manager, name="movie-manager"),
]

app_name = "cinema"
