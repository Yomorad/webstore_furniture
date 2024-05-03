from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'title': 'Главная',
        'content': 'Главная страница',
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'Текст о нас'
    }
    return render(request, 'main/about.html', context)
