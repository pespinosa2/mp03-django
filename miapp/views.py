from django.http import HttpResponse

def inicio(request):
    return HttpResponse("¡Hola, esta es la primera vista de miapp!")
