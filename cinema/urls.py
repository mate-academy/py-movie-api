from django.urls import path

from cinema.views import movie_list_view, movie_detail_view

app_name = "cinema"

urlpatterns = [
    path("movies/", movie_list_view, name="list-view"),
    path("movies/<int:pk>/", movie_detail_view, name="detail-view")
]
