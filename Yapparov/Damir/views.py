from django.http import HttpResponse

def index(request, name, age, interests):
    return HttpResponse(f"{name}, {age}, {interests} <a href=http://127.0.0.1:8000/about>about</a> <a href=http://127.0.0.1:8000/contacts>contacts</a>")

def about(request):
    return HttpResponse("Приехал из Краснодара, средняя успеваемость в шк, учится интерестно")

def contacts(request):
    return HttpResponse("https://github.com/damirpopo")


