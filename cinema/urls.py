from django.contrib import admin
from django.urls import path
from cinema.views import (
    create,
    update
)

app_name = "cinema"

urlpatterns = [
    path(""),

]
