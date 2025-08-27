from django.urls import path
from .views import MovieListCreateAPIView, MovieRetrieveUpdateDestroyAPIView
from .info import welcome

urlpatterns = [
    path('', welcome, name='welcome-page'),
    path('movies/', MovieListCreateAPIView.as_view(), name='movie-list-create'),
    path('movies/<int:pk>/', MovieRetrieveUpdateDestroyAPIView.as_view(), name='movie-detail'),
]
