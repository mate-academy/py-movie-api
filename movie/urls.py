from django.urls import path

from .views import (
    movies_list, movie_get)

urlpatterns = [
    path('movies/', movies_list, name='movies-list'),
    path('movies/<int:pk>', movie_get, name='movies-get'),

]

app_name = 'movie'
