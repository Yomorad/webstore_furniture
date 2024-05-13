from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.http import BadHeaderError
from django.template.loader import render_to_string
from django_app import settings

@shared_task
def send_email_reg_task(username, receiver):
    subject = f'Welcome to our store, {username}!'
    context = {'content': username}  # Контекст дляшаблона
    html_message  = render_to_string('users/msg_reg.html', context)  # Загрузка HTML-шаблона
    text_message = f" Hello there! \n\
I wanted to personally write an email in order to welcome you to our platform.\n\
 We have worked day and night to ensure that you get the best service.\n I hope \
that you will continue to use our service.\n We send out a newsletter once a \
week. Make sure that you read it.\n It is usually very informative.\n\
Cheers!\n\
~ Yasoob\n\
    "
    email = EmailMultiAlternatives(subject, html_message, settings.EMAIL_HOST_USER, receiver)
    email.content_subtype = 'html'
    email.attach_alternative(text_message, "text/plain")
    try:
        email.send()
    except BadHeaderError:
        pass

    # message = 'Hello there!'
    # send_mail(
    #     subject,
    #     message,
    #     settings.EMAIL_HOST_USER,
    #     receiver
    # )  