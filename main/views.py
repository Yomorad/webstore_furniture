from django.contrib import messages
from django.shortcuts import redirect, render

from main.forms import CreateFeedbackForm
from main.tasks import send_email_feedback_task

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
        'text_on_page': 'Текст о нас',
    }
    return render(request, 'main/about.html', context)

def feedback(request):
    if request.method == 'POST':
        form = CreateFeedbackForm(data=request.POST)
        if form.is_valid():
            # отправляем письмо
            subject_letter = request.POST.get('subject_letter')
            body_letter = request.POST.get('body_letter')
            print(subject_letter, body_letter)
            send_email_feedback_task.delay(subject_letter, body_letter)
            messages.success(request, 'Спасибо за отзыв!')
            return redirect('main:index')
    else:
        form = CreateFeedbackForm()
    context = {
        'title': 'Home - Отзыв',
        'form': form
    }
    return render(request, 'main/feedback.html', context)