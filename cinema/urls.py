from django.urls import path
from cinema import views

urlpatterns = [
    path("movie/", views.movie_list, name="movie-list"),
    path("movie/<int:pk>/", views.movie_detail, name="movie-detail"),
]

app_name = "cinema"
