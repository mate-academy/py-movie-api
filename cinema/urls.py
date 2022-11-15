from django.urls import path

from cinema import views
from cinema.views import movie_list

urlpatterns = [
    path("movies/", movie_list, name="movie-list"),
    path("movies/<int:pk>/", views.snippet_detail),
]

app_name = "cinema"
