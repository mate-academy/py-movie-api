from django.urls import path

from cinema.views import MovieListCreateView, MovieRetrieveUpdateDeleteView

urlpatterns = [
    path("movies/", MovieListCreateView.as_view(),
         name="movie-list-create"),
    path("movies/<int:pk>/", MovieRetrieveUpdateDeleteView.as_view(),
         name="movie-retrieve-update-delete"),
]

app_name = "cinema"
