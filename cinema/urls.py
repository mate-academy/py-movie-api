from django.urls import path

urlpatterns = [
    path(
        "cinames/",
        cinema_list,
        name="cinema-list"
    )
]

app_name = "cinema"
