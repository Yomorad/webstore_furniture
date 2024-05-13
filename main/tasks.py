from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.http import BadHeaderError
from django_app import settings

@shared_task
def send_email_feedback_task(subject_letter, body_letter):
    subject = subject_letter
    text_message = body_letter
    receiver = [settings.EMAIL_OWNER_USER]
    email = EmailMultiAlternatives(subject, text_message, settings.EMAIL_HOST_USER, receiver)
    try:
        email.send()
    except BadHeaderError:
        pass