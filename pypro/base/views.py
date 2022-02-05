from django.http import HttpResponse

def home(request):
    return HttpResponse('Olá, Deus é Fiel !')