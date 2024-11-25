from django.http import JsonResponse
from django.urls import path
from .views import MovieListCreateAPIView, MovieRetrieveUpdateDestroyAPIView

def api_root(request):
    return JsonResponse({
        "movies_list": "/api/cinema/movies/",
        "movie_detail": "/api/cinema/movies/<id>/",
    })

urlpatterns = [
    path('', api_root, name='api-root'),  # Головна сторінка API
    path('movies/', MovieListCreateAPIView.as_view(), name='movie-list-create'),
    path('movies/<int:pk>/', MovieRetrieveUpdateDestroyAPIView.as_view(), name='movie-detail'),
]
