from django.http import HttpResponse


def home(request):
    return HttpResponse('Olá, Jonecy bem vindo Dev !')
