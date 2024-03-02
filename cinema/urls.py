from django.urls import path
from cinema.views import movie_list_view, movie_detail_view, movie_delete_view

urlpatterns = [
    path(
        'movies/',
        movie_list_view,
        name='movie-list'
    ),
    path(
        'movies/<int:pk>/details/',
        movie_detail_view,
        name='movie-detail'
    ),
    path(
        'movies/<int:pk>/delete/',
        movie_delete_view,
        name='movie-delete'
    ),
]

app_name = 'cinema'
