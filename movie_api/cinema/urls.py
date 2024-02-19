from django.urls import path

from cinema.views import get_movie_or_movies

urlpatterns = [
    path('movies/', get_movie_or_movies, name='movies-list'),
    path('movies/<int:pk>/', get_movie_or_movies, name='get-movie-by-id'),
]

app_name = 'cinema'
