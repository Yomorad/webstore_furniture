# Веб приложение магазина мебели

## Stack 
- Django
- DRF
- PostgreSQL
- Docker-compose
- Redis
- Celery
- RabbitMQ


## Описание
1. backend - основное приложение, онлайн магазин мебели на Django, реализовано:   
   меню, простой поиск и сортировка, редактирование через админку, корзина, оформление заказа   
   Работает через теги, шаблоны django, использованы формы для создания заказов.   
   Прописана прогрузка фикстур.   
   Есть API для работы с продуктами через DRF    
   Приложение запускается через сокет gunicorn на nginx    
   Настройки gunicorn указаны в gunicorn_config.py      
2. Redis - используется для кэширования частозапрашиваемых представлений
3. Сelery + RabbitMQ - для обработки задач, связанных с удалёнными сервисами.
    Как пример: отправка отзыва клиента, автопуши клиенту при регистрации
4. Nginx - отдаёт собранные статические данные Django, проксирует запросы на приложение http://backend:8000
   Настройки указаны в nginx.conf
5. PostgreSQL - хранит бд в томах через docker

## Как развернуть проект:
### 1 Клонируем проект

```bash
git clone <link>
```

### 2 Прописываем свои конфиги в .env
```bash
# генерируем django ключ
SECRET_KEY = 'example'
# почту откуда отправляем письма
EMAIL_HOST_USER = "example"
# сгенерированный пароль от mail
EMAIL_HOST_PASSWORD = "example"
# корпоративная почта для приёма отзывов клиентов
EMAIL_OWNER_USER = "example"
```

### 3 Поднимаем контейнеры
```bash
docker compose up --build
# Заходим http://localhost:8080/
# как вариант, через exec контейнера django создаём суперюзера
docker exec -it django_app_backend python manage.py createsuperuser
# Дальше отладка, можно попробовать аналогично запустить тесты 
docker exec -it django_app_backend python manage.py test
# в конце работы выключаем контейнеры и удаляем привязанные тома
docker compose down -v
```