from django.urls import path

from app.views import movies_list_view, movie_detail_view

urlpatterns = [
    path('movies/', movies_list_view, name="movie-list"),
    path('movies/<int:pk>/', movie_detail_view, name="movie-detail")
]

app_name = 'app'
