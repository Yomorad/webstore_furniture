<h1 align="center">Hi there, This is a store on Django
<img src="https://github.com/Yomorad/yomorad/blob/main/icons/pantsu-konosuba.gif" height="90"/></h1>

<h1>Разворот магазина на Django локально через контейнеры</h1>

<h1>Порядок действий:</h1>

<h2>1 Настраиваем django:</h2>

<p>Добавляем статику</p>

```bash
python manage.py collectstatic
```
<p>Докачиваем gunicorn и обновляем requirements.txt</p>

```bash
pip install gunicorn
pip freeze > requirements.txt
```
<p>Меняем под себя settings.py</p>

```bash
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# указываем имя нашего контейнера а не сервиса, в нашем случае django_app_rabbitmq
CELERY_BROKER_URL = 'amqp://guest:guest@django_app_rabbitmq//' # для RabbitMQ
# аналогично для CACHES
'LOCATION': 'redis://django_app_redis:6379/1', # Имя сервиса контейнера Redis вместо 'localhost'
```
<h2>2 Раскидываем django приложение в папку backend, подписываем для него dockerfile, также для nginx</h2>
<p>Изменяем главные настройки nginx, предварительно подменяя nginx.conf</p>
<p>Указываем proxy_pass http://backend:8000; где backend - имя сервиса в compose</p>
<p>Прописываем статику</p>

<h2>Расписываем compose</h2>
<p>Переписываем под себя .env, он задан у нас везде как env_file: .env</p>
<p>Запуск нашего приложения происходит через gunicorn_config.py</p>

```bash
gunicorn -c gunicorn_config.py django_app.wsgi:application
```
<p>либо можно командой</p>

```bash
gunicorn django_app.wsgi:application --bind 0.0.0.0:8000
```
<h2>Работа с контейнерами:</h2>

```bash
# создаем образы
docker compose build
# поднимаем контейнеры
docker compose up -d
# неважно как, через exec контейнера django создаём суперюзера
# как пример через консоль 
docker exec -it django_app_backend python manage.py createsuperuser
# Дальше отладка, можно попробовать аналогично запустить тесты 
docker exec -it django_app_backend python manage.py test
```
<h2>При измененении django проекта, образ будет пересобран и отпрвален в dockerhub</h2>
<p>Читай main.yml</p>