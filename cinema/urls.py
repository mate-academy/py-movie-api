"""
URL configuration for cinema_service project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from cinema.views import index, movie

urlpatterns = [
    path("", index, name="index"),
    path("api/cinema/movies/", movie, name="get"),
    path("api/cinema/movies/<int:pk>/", movie, name="get_one"),
    path("api/cinema/movies/", movie, name="post"),
    path("api/cinema/movies/<int:pk>/", movie, name="put"),
    path("api/cinema/movies/<int:pk>/", movie, name="delete"),
]

app_name = "cinema"
