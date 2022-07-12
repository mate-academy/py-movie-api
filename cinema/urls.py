from django.urls import path

from cinema.views import movie_list, one_movie, movie_add, movie_update, movie_delete

urlpatterns = [
    path('movies/', movie_list, name='movie-list'),
    path('movies/<int:pk>/', one_movie, name='one-movie'),
    path('movies/create/', movie_add, name='add-movie'),
    path('movies/<int:pk>/update/', movie_update, name='movie-update'),
    path('movies/<int:pk>/delete/', movie_delete, name='movie-delete')
]

app_name = 'cinema'
