from django.http import JsonResponse

def welcome(_request) -> JsonResponse:
    return JsonResponse({"message": "Welcome to the Cinema API!"})
