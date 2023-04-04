from django.urls import path

from cinema.views import movies_list, movie_details

urlpatterns = [
    path("movies/", movies_list, name="movies_list"),
    path("movies/<int:pk>/", movie_details, name="movie_get_update_delete"),
]


app_name = "cinema"
