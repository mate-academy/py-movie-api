from django.urls import path

from cinema.views import movies_list, movies_object

urlpatterns = [
    path("movies/", movies_list),
    path("movies/<int:pk>/", movies_object)
]

app_name = "cinema"
