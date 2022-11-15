from django.urls import path

from cinema.views import movie_list, movie_pk

urlpatterns = [
    path("movies/", movie_list, name="cinema-list"),
    path("movies/<int:pk>/", movie_pk, name="cinema-pk"),
]

app_name = "cinema"
