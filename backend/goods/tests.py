from django.core.paginator import Paginator
from django.test import RequestFactory, TestCase
from django.urls import reverse

from goods.models import Categories, Products
from goods.views import catalog, product

# Create your tests here.
class CategoriesModelTestCase(TestCase):
    def setUp(self):
        # Создаем тестовую категорию для использования в тестах
        self.category = Categories.objects.create(name='Test Category', slug='test-category')

    # Тест для проверки метода __str__ модели Categories
    def test_category_str_method(self):
        self.assertEqual(str(self.category), 'Test Category')

    # Тест для проверки verbose_name модели Categories
    def test_category_verbose_name(self):
        self.assertEqual(Categories._meta.verbose_name, 'Категорию')

    # Тест для проверки verbose_name_plural модели Categories
    def test_category_verbose_name_plural(self):
        self.assertEqual(Categories._meta.verbose_name_plural, 'Категории')

class ProductsModelTestCase(TestCase):
    def setUp(self):
        # Создаем тестовую категорию и тестовый продукт для использования в тестах
        self.category = Categories.objects.create(name='Test Category', slug='test-category')
        self.product = Products.objects.create(
            name='Test Product',
            slug='test-product',
            description='Test Description',
            image='test.jpg',
            price=10.00,
            discount=0.10,
            quantity=20,
            category=self.category
        )

    # Тест для проверки метода __str__ модели Products
    def test_product_str_method(self):
        self.assertEqual(str(self.product), 'Test Product Количество - 20')

    # Тест для проверки verbose_name модели Products
    def test_product_verbose_name(self):
        self.assertEqual(Products._meta.verbose_name, 'Продукт')

    # Тест для проверки verbose_name_plural модели Products
    def test_product_verbose_name_plural(self):
        self.assertEqual(Products._meta.verbose_name_plural, 'Продукты')

    # Тест для проверки метода get_absolute_url модели Products
    def test_product_get_absolute_url_method(self):
        self.assertEqual(self.product.get_absolute_url(), reverse("catalog:product", kwargs={"product_slug": 'test-product'}))

    # Тест для проверки метода sell_price модели Products
    def test_product_sell_price_method(self):
        self.assertEqual(self.product.sell_price(), 9.99)