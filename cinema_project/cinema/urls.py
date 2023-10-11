from django.urls import path
from .views import MovieListCreateView, MovieRetrieveUpdateDestroyView


urlpatterns = [
    path('api/cinema/movies/', MovieListCreateView.as_view(), name='movie-list-create'),
    path('api/cinema/movies/<int:pk>/', MovieRetrieveUpdateDestroyView.as_view(), name='movie-retrieve-update-destroy'),
]

app_name = "cinema"
