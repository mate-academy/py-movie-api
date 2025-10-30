from django.http import HttpResponse

def home(request):
    return HttpResponse("Movie API działa! Sprawdź endpoint /api/cinema/movies/")
