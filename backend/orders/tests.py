from asyncio.windows_events import NULL
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from carts.models import Cart
from goods.models import Products
from orders.models import Order, OrderItem

from users.models import User

# Create your tests here.
class OrderModelTestCase(TestCase):
    def setUp(self):
        # Создаем пользователя для теста
        self.user = User.objects.create(username='testuser', first_name='John', last_name='Doe')
        # Создаем заказ для теста
        self.order = Order.objects.create(user=self.user, phone_number='123456789', requires_delivery=True, is_paid=False)

    def test_order_str_method(self):
        # Проверяем, что метод __str__ модели Order возвращает правильную строку
        self.assertEqual(str(self.order), f"Заказ № {self.order.pk} | Покупатель {self.user.first_name} {self.user.last_name}")

    def test_order_default_status(self):
        # Проверяем, что статус заказа по умолчанию устанавливается правильно
        self.assertEqual(self.order.status, 'В обработке')

    def test_order_created_timestamp(self):
        # Проверяем, что дата создания заказа не позже текущего времени
        self.assertTrue(self.order.created_timestamp <= timezone.now())