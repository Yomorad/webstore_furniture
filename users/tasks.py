from celery import Celery, shared_task
from django.core.mail import EmailMultiAlternatives, send_mail
from django.template.loader import render_to_string
from django_app import settings
# from django_app.celery import app
# Создаем экземпляр Celery
# app = Celery('users_tasks', broker='pyamqp://guest@localhost//')
# Определяем асинхронную задачу с помощью декоратора @app.task


@shared_task
def send_email_task(username, receiver):
    subject = f'Welcome to our store, {username}!'
    
    context = {'content': username}  # Контекст дляшаблона
    # html_content = render_to_string('msg_reg.html', context)  # Загрузка HTML-шаблона
    message = 'Hello there!'
    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        receiver
    )  
#     message = f" Hello there! \n\
# I wanted to personally write an email in order to welcome you to our platform.\n\
#  We have worked day and night to ensure that you get the best service.\n I hope \
# that you will continue to use our service.\n We send out a newsletter once a \
# week. Make sure that you read it.\n It is usually very informative.\n\
# Cheers!\n\
# ~ Yasoob\n\
#     "
    # email = EmailMultiAlternatives(subject, message, settings.EMAIL_HOST_USER, receiver)
    # email.attach_alternative(html_content, 'text/html')
    # email.send()
