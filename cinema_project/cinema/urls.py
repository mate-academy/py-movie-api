from django.urls import path
from .views import MovieListCreate, MovieRetrieveUpdateDestroy

urlpatterns = [
    path('movies/', MovieListCreate.as_view(), name='movie-list-create'),
    path('movies/<int:pk>/', MovieRetrieveUpdateDestroy.as_view(), name='movie-retrieve-update-destroy'),
]
