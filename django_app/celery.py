from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

from django_app import settings

	# Указываем Django settings модуль для Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_app.settings')
	# Создаем экземпляр Celery приложения
app = Celery('django_app')
	# Указываем брокер сообщений
app.config_from_object('django.conf:settings', namespace='CELERY')

    # Загружаем задания из Django приложений
app.autodiscover_tasks()