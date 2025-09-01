from django.urls import path
from cinema import views

app_name = "cinema"

urlpatterns = [
    path("movies/", views.movie_list, name="movie_list"),
    path("movies/<int:pk>/", views.movie_detail, name="movie_detail"),
]
