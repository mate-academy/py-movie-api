from django.urls import path

from cinema.views import movie_list, movie_detail

urlpatterns = [
    path('', movie_list, name='movie-list'),
    path('movie/<int:pk>/', movie_detail, name='movie-details'),
]

app_name = 'cinema'
