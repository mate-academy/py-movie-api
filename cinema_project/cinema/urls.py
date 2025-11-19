from django.urls import path
from . import views

urlpatterns = [
    path("api/cinema/movies/", views.movie_list_create),
    path("api/cinema/movies/<int:pk>/", views.movie_retrieve_update_destroy),
]
