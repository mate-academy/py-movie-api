from django.urls import path

from cinema.views import movies_list

urlpatterns = [
    path('movies/', movies_list, name='movies-list'),
    path('movies/<int:pk>/', movies_list, name='get-movie-by-id'),
]

app_name = 'cinema'
