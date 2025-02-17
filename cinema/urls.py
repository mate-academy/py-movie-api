from django.urls import path
from cinema import views

urlpatterns = [
    path("api/movies/", views.movie_list, name="movie-list"),
    path("api/movies/<int:pk>/", views.movie_detail, name="movie-detail"),
    path("api/movies/create/", views.movie_create, name="movie-create"),
    path("api/movies/<int:pk>/update/", views.movie_update, name="movie-update"),
    path("api/movies/<int:pk>/delete/", views.movie_delete, name="movie-delete"),
]

app_name = "cinema"
