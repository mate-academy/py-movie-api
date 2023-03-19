from django.urls import path

from cinema.views import movie_list, movie_detail

urlpatterns = [
    path("", movie_list, name="movie-list"),
    path("<int:pk>/", movie_detail, name="movie-create"),
    path("", movie_list, name="movie-get"),
    path("<int:pk>/", movie_detail, name="movie-update"),
    path("<int:pk>/", movie_detail, name="movie-delete"),
]

app_name = "cinema"
