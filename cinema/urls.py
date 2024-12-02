from django.urls import path

from cinema import views

app_name = "cinema"

urlpatterns = [
    path("movies/", views.movie_list, name="movies"),
    path("movies/<int:pk>/", views.movie_by_id, name="movie_by_id")
]
