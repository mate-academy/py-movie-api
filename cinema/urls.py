from django.urls import path

from cinema import views

urlpatterns = [
    path("api/cinema/movies/", views.movie_list_create, name="movie-list-create"),
    path("api/cinema/movies/<pk>/", views.movie_detail, name="movie-detail"),
]