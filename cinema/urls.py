from django.urls import path
from cinema.views import (
    movie_list_create,
    movie_detail
)

urlpatterns = [
    path('movies/', movie_list_create, name='movies-list'),
    path('movies/<int:pk>/', movie_detail, name='movie-detail'),
]

app_name = "cinema"
