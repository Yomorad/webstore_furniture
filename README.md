<h1 align="center">Hi there, This is a store on Django
<img src="https://github.com/Yomorad/yomorad/blob/main/icons/pantsu-konosuba.gif" height="90"/></h1>

<h1>Магазин на Django</h1>

<h2>Корень проекта:</h2>
<p>django_app</p>

<h2>База данных</h2>
<p>PostgreSQL</p>

<h2>Инструменты:</h2>
<p>Celery</p>
<p>RabbitMQ</p>
<p>Redis</p>
<p>DRF</p>

<h2>Приложения(к каждому прикреплены тесты):</h2>
<ul class="list-style-type: disc">
    <li><h3>main</h3></li>
    <p>Обрабатывает запросы на "Главную страницу", страницу "О нас"</p>
    <li><h3>goods</h3></li>
    <p>Обрабатывает запросы на страницу каталога(с пагинацией), страницу товара, поиск по каталогу</p>
    <p>Созданы две модели Categories и Products и добавлены в админ-панель</p>   
    <li><h3>users</h3></li>
    <p>Обрабатывает запросы через формы на авторизацию/регистрацию/деавторизацию, страницу "Личный кабинет", страницу "Корзина"</p>
    <p>Отредактирована по форме модель User и добавлена в админ панель</p>   
    <li><h3>carts</h3></li>
    <p>Обрабатывает запросы через формы на добавление/изменение/удаление товара</p>
    <p>Создана модель корзины Cart и добавлена в админ-панель</p>   
    <li><h3>orders</h3></li>
    <p>Обрабатывает запрос на создание заказа через форму</p>
    <p>Созданы две модели общих заказов Order и текущего заказа OrderItem и добавлены в админ-панель</p>   
</ul>

<h2>Celery/RabbitMQ используется для:</h2>
<p>Отправки уведомлений после регистрации в приложении users</p>
<p>Отправки сообщений в телеграмм бот при создании клиентом заказа в приложении orders</p>

<h2>Redis используется для:</h2>
<p>временного сохранения результатов представлений views.py в кэше redis</p>

<h2>DRF используется для:</h2>
<p></p>

<h3>1)клонируй репозиторий</h3>

```bash
git clone 'link'
```

<h3>2)создай виртуальную среду через редактор или virtualenv</h3>

```bash
python -m venv .venv
.venv\Scripts\activate
```
<h3>3)Скачай библиотеки</h3>

```bash
pip install -r requirements
```
<h3>4)Укажи свою бд PostgreSQL в settings.py</h3>
<p>data_base_p: str = 'data_base_p'</p>
<p>user_p: str = 'user_p'</p>
<p>host_p: str = 'host_p'</p>
<p>password_p: str = 'password_p'</p>

<h3>5)База django</h3>

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata fixtures/goods/categories.json
python manage.py loaddata fixtures/goods/products.json
python manage.py createsuperuser
python manage.py runserver
```

