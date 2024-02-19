from django.urls import path

from cinema.views import movie_api

urlpatterns = [
    path('movies/', movie_api, name='movies-list'),
    path('movies/<int:pk>/', movie_api, name='get-movie-by-id'),
]

app_name = 'cinema'
