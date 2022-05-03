from django.urls import path


from .views import (
    MovieList,
    MovieRetrieveView,
    MovieRetrieveCreateView,
    MovieRetrieveUpdateDestroyView,


)

urlpatterns = [
    path("api/cinema/movies/", MovieList.as_view(), name="movie-list"),
    path("api/cinema/movies/<int:pk>/", MovieRetrieveView.as_view(), name="movie-retrieve"),
    path("api/cinema/movies/", MovieRetrieveCreateView.as_view(), name="movie-create"),
    path("api/cinema/movies/<int:pk>/", MovieRetrieveUpdateDestroyView.as_view(), name="movie-update-delete"),
]