from django.urls import path

from cinema.views import movie_list, movie_update_delete

urlpatterns = [
    path("movies/", movie_list, name="movie_list"),
    path("movies/<int:pk>/", movie_update_delete, name="movie_update_delete"),
]
app_name = "cinema"
