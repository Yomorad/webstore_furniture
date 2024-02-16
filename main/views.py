from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {
        'title': 'Home',
        'content': 'Главная страница магазина - HOME',
        'list': ['1', '2', '3'],
        'dict': {'a': 1, 'b': 2},
        'bool': True,
    }
    return render(request, 'main/index.html', context)

def about(request):
    return HttpResponse('About page')
