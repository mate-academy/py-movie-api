from django.urls import path
from cinema.views import bus_list, bus_info


urlpatterns = [
    path("movies/", bus_list, name="bus-list"),
    path("movies/<int:pk>/", bus_info, name="bus-list"),
]

app_name = "cinema"
