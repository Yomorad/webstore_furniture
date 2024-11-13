from django.test import Client, TestCase
from django.urls import reverse

from users.models import User

# Create your tests here.
class UserModelTestCase(TestCase):
    # тестим модели
    def test_user_creation(self):
        user = User.objects.create_user(username="testuser", email="test@example.com", password="testpassword")
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "test@example.com")
        self.assertTrue(user.check_password("testpassword"))

    def test_user_string_representation(self):
        user = User.objects.create_user(username="testuser", email="test@example.com", password="testpassword")
        self.assertEqual(str(user), user.username)
    
    # Тест для функции login
    def test_login_view(self):
        client = Client()
        response = client.post(reverse('user:login'), {'username': 'root', 'password': 'root'})
        self.assertEqual(response.status_code, 200)  # Проверяем код ответа

    # Тест для функции registration
    def test_registration_view(self):
        client = Client()
        response = client.post(reverse('user:registration'), {'username': 'newuser', 'password1': 'newpassword', 'password2': 'newpassword', 'email': 'newuser@example.com'})
        self.assertEqual(response.status_code, 200)  # Проверяем код ответа

    # Тест для функции profile
    def test_profile_view(self):
        client = Client()
        user = User.objects.create_user(username='testuser', password='testpassword')
        client.force_login(user)
        response = client.get(reverse('user:profile'))
        self.assertEqual(response.status_code, 200)  # Проверяем код ответа

    # Тест для функции users_cart
    def test_users_cart_view(self):
        client = Client()
        response = client.get(reverse('user:users_cart'))
        self.assertEqual(response.status_code, 200)  # Проверяем код ответа

    # Тест для функции logout
    def test_logout_view(self):
        client = Client()
        user = User.objects.create_user(username='testuser', password='testpassword')
        client.force_login(user)
        response = client.get(reverse('user:logout'))
        self.assertEqual(response.status_code, 302)  # Проверяем перенаправление после выхода