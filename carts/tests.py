from django.http import JsonResponse
from django.template.loader import render_to_string
from django.test import RequestFactory, TestCase
from carts.models import Cart
from carts.views import cart_add, cart_change, cart_remove
from goods.models import Products

from users.models import User

# Create your tests here.
class CartViewsTestCase(TestCase):
    def setUp(self):
        # Создаем тестовую фабрику запросов
        self.factory = RequestFactory()
        # Создаем тестового пользователя
        self.user = User.objects.create(username='test_user')
        # Создаем тестовый продукт
        self.product = Products.objects.create(name='Test Product')
        # Создаем тестовую корзину
        self.cart = Cart.objects.create(user=self.user, product=self.product, quantity=1)

    # Тест для представления cart_add
    def test_cart_add(self):
        # Создаем POST запрос с указанием продукта
        request = self.factory.post("/", {"product_id": self.product.id})
        # Устанавливаем пользователя для запроса
        request.user = self.user
        # Вызываем представление cart_add
        response = cart_add(request)

        # Проверяем код состояния ответа
        self.assertEqual(response.status_code, 200)
        # Проверяем содержимое ответа
        self.assertEqual(response.content.decode("utf-8"), JsonResponse({"message": "Товар добавлен в корзину", "cart_items_html": render_to_string("carts/includes/included_cart.html", {"carts": [self.cart]}, request=request)}).content.decode("utf-8"))

    # Тест для представления cart_change
    def test_cart_change(self):
        # Создаем POST запрос с указанием ID корзины и количества
        request = self.factory.post("/", {"cart_id": self.cart.id, "quantity": 2})
        # Вызываем представление cart_change
        response = cart_change(request)

        # Проверяем код состояния ответа
        self.assertEqual(response.status_code, 200)
        # Проверяем содержимое ответа
        self.assertEqual(response.content.decode("utf-8"), JsonResponse({"message": "Количество изменено", "cart_items_html": render_to_string("carts/includes/included_cart.html", {"carts": [self.cart]}, request=request), "quantity": 2}).content.decode("utf-8"))

    # Тест для представления cart_remove
    def test_cart_remove(self):
        # Создаем POST запрос с указанием ID корзины
        request = self.factory.post("/", {"cart_id": self.cart.id})
        # Вызываем представление cart_remove
        response = cart_remove(request)

        # Проверяем код состояния ответа
        self.assertEqual(response.status_code, 200)
        # Проверяем содержимое ответа
        self.assertEqual(response.content.decode("utf-8"), JsonResponse({"message": "Товар удален", "cart_items_html": render_to_string("carts/includes/included_cart.html", {"carts": []}, request=request), "quantity_deleted": 1}).content.decode("utf-8"))