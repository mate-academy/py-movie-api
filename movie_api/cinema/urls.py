from django.urls import path

from cinema.views import movie_api

urlpatterns = [
    path('movies/', movie_api, name='movies-list'),
    path('movies/<int:pk>/', movie_api, name='get-movie-by-id'),
    path('movies/', movie_api, name='create-movie'),
    path('movies/<int:pk>/', movie_api, name='update-movie'),
]

app_name = 'cinema'
