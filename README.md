<h1 align="center">Hi there, This is a store on Django
<img src="https://github.com/Yomorad/yomorad/blob/main/icons/pantsu-konosuba.gif" height="90"/></h1>

<h1>Магазин на Django</h1>

<h2>Корень проекта:</h2>
<p>django_app</p>

<h2>Базы данных</h2>
<p>PostgreSQL</p>
<p>Redis</p>

<h2>Инструменты:</h2>
<p>Celery</p>
<p>RabbitMQ</p>
<p>DRF</p>
<p>Graphene</p>

<h2>Приложения:</h2>
<ul class="list-style-type: disc">
    <li><h3>main</h3></li>
    <p>Обрабатывает запросы на "Главную страницу", страницу "О нас"</p>
    <li><h3>goods</h3></li>
    <p>Обрабатывает запросы на страницу каталога(с пагинацией), страницу товара, поиск по каталогу</p>
    <p>Созданы две модели Categories и Products и добавлены в админ-панель</p>   
    <p>Настроена к Products REST API(drf) через api_urls, api_views</p>   
    <li><h3>users</h3></li>
    <p>Обрабатывает запросы через формы на авторизацию/регистрацию/деавторизацию, страницу "Личный кабинет", страницу "Корзина"</p>
    <p>Отредактирована по форме модель User и добавлена в админ панель</p>   
    <li><h3>carts</h3></li>
    <p>Обрабатывает запросы через формы на добавление/изменение/удаление товара</p>
    <p>Создана модель корзины Cart и добавлена в админ-панель</p>   
    <li><h3>orders</h3></li>
    <p>Обрабатывает запрос на создание заказа через форму</p>
    <p>Созданы две модели общих заказов Order и текущего заказа OrderItem и добавлены в админ-панель</p>
    <p>Настроены qraphql запросы(graphene) через schema.py</p>
</ul>

<h2>Celery/RabbitMQ:</h2>
<p>Отправка уведомлений после регистрации в приложении users:registration </p>
<p>Отправка отзывов через форму в приложении main:feedback</p>

<h2>Redis:</h2>
<p>временное сохранение результатов представлений views.py в кэше redis</p>

<h2>DRF:</h2>
<p>API для отображения всего каталога товаров Products(в конце статьи)</p>
<p>API обрабатывает: GET, POST, PUT, PATCH, DELETE</p>

<h2>Локальный разворот проекта</h2>
<h3>1) клонируй репозиторий</h3>

```bash
git clone 'link'
```

<h3>2) создай виртуальную среду через редактор или virtualenv</h3>

```bash
python -m venv .venv
.venv\Scripts\activate
```
<h3>3) Скачай библиотеки</h3>

```bash
pip install -r requirements
```
<h3>4) Укажи свои конфиги и бд PostgreSQL в settings.py</h3>
<p>DB_NAME: str = 'DB_NAME'</p>
<p>DB_USER: str = 'DB_USER'</p>
<p>DB_PASSWORD: str = 'DB_PASSWORD'</p>
<p>EMAIL_HOST_USER = "EMAIL_HOST_USER"</p>
<p>EMAIL_OWNER_USER = "EMAIL_OWNER_USER"</p>
<p>EMAIL_HOST_PASSWORD = "EMAIL_HOST_PASSWORD"  здесь указывается не пароль а внешний ключ безопасности mail</p>

<h3>5) RabbitMQ запуск</h3>
<p>скачай и запусти rabbitmq либо просто запусти контейнер. дока: https://hub.docker.com/_/rabbitmq/</p>

```bash
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.13-management
```
<h3>6) Redis запуск</h3>
<p>скачай и запусти redis либо запусти контейнер. дока: https://hub.docker.com/_/rabbitmq/</p>

```bash
sudo service redis-server start
```
<p>админка если надо RabbitMQ http://localhost:15672 Базовый: логин: guest, пароль: guest</p>
<h3>7) База django для локального разворота</h3>
<p>Делаем миграции к подключённой бд, кидаем фикстуры, суперпользователя</p>

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata fixtures/goods/categories.json
python manage.py loaddata fixtures/goods/products.json
python manage.py createcachetable   #создаём таблицу для кэша
python manage.py createsuperuser
```
<p>Запускаем в разных терминалах сайт, очереди, мониторинг</p>

```bash
#Отдельно в разных терминалах:
    python manage.py runserver
    celery -A django_app worker --loglevel=info -P eventlet
    celery -A django_app flower
```
<p>После celery -A django_app flower, будет доступен мониторинг задач и воркеров  http://localhost:5555/workers/</p>
<p>Запросы Graphql доступны по ссылке http://127.0.0.1:8000/graphql/</p>

<h2>Тестирование</h2>

```bash
python manage.py test
```

<h2>API Endpoints for Products</h2>
<ul>
  <li>
    <strong>Список продуктов (GET):</strong><br>
    URL: <a href="http://127.0.0.1:8000/api/products/">http://127.0.0.1:8000/api/products/</a><br>
    Описание: Получить список всех продуктов.
  </li>
  <li>
    <strong>Получение информации о продукте (GET):</strong><br>
    URL: <a href="http://127.0.0.1:8000/api/products/<int:pk>/">http://127.0.0.1:8000/api/products/<int:pk>/</a><br>
    Описание: Получить информацию о конкретном продукте по его идентификатору.
  </li>
  <li>
    <strong>Частичное обновление продукта (PATCH):</strong><br>
    URL: <a href="http://127.0.0.1:8000/api/products/<int:pk>/partupdate/">http://127.0.0.1:8000/api/products/<int:pk>/partupdate/</a><br>
    Описание: Частично обновить информацию о продукте по его идентификатору.
  </li>
  <li>
    <strong>Удаление продукта (DELETE):</strong><br>
    URL: <a href="http://127.0.0.1:8000/api/products/<int:pk>/delete/">http://127.0.1:8000/api/products/<int:pk>/delete/</a><br>
    Описание: Удалить продукт по его идентификатору.
  </li>
  <li>
    <strong>Обновление продукта (PUT):</strong><br>
    URL: <a href="http://127.0.0.1:8000/api/products/<int:pk>/update/">http://127.0.0.1:8000/api/products/<int:pk>/update/</a><br>
    Описание: Полностью обновить информацию о продукте по его идентификатору.
  </li>
  <li>
    <strong>Создание продукта (POST):</strong><br>
    URL: <a href="http://127.0.0.1:8000/api/products/create/">http://127.0.0.1:8000/api/products/create/</a><br>
    Описание: Создать новый продукт.
  </li>
</ul>

<h2>Graphql через graphene http://127.0.0.1:8000/graphql/</h2>
<h2>OrderType</h2>
<p>Этот тип данных представляет модель Order в GraphQL.</p>
<h3>Поля:</h3>
<ul>
  <li>id: ID заказа.</li>
  <li>user: Пользователь, совершивший заказ.</li>
  <li>createdTimestamp: Дата и время создания заказа.</li>
  <li>phoneNumber: Номер телефона покупателя.</li>
  <li>requiresDelivery: Флаг, указывающий на необходимость доставки.</li>
  <li>deliveryAddress: Адрес доставки.</li>
  <li>paymentOnGet: Флаг, указывающий на оплату при получении.</li>
  <li>isPaid: Флаг, указывающий на оплату заказа.</li>
  <li>status: Статус заказа.</li>
</ul>

<h2>OrderItemType</h2>
<p>Этот тип данных представляет модель OrderItem в GraphQL.</p>
<h3>Поля:</h3>
<ul>
  <li>id: ID элемента заказа.</li>
  <li>order: Заказ, к которому относится элемент.</li>
  <li>product: Продукт, который был добавлен в заказ.</li>
  <li>name: Название элемента заказа.</li>
  <li>price: Цена элемента заказа.</li>
  <li>quantity: Количество элементов.</li>
  <li>createdTimestamp: Дата и время создания элемента заказа.</li>
</ul>

<h2>Использование:</h2>

```bash
query {
  orderList {
    id
    user {
      id
      firstName
      lastName
    }
    createdTimestamp
    phoneNumber
    requiresDelivery
    deliveryAddress
    paymentOnGet
    isPaid
    status
  }
  
  orderItemList {
    id
    order {
      id
    }
    product {
      id
      name
    }
    name
    price
    quantity
    createdTimestamp
  }
}
```