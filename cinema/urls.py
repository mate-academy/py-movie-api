from django.urls import path

from cinema.views import movies, movies2

urlpatterns = [
    path('movies/', movies, name="movies"),
    path('movies/<int:pk>', movies2, name="movies2")
]


app_name = "cinema"
