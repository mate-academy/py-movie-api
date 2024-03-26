from django.contrib import admin
from django.urls import path
from cinema.views import (
    create,
    update
)

urlpatterns = [
    path("", admin.site.urls),

]
