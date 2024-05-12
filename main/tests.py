from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse

class MainViewsTestCase(TestCase):
    def test_index_view(self):
        response = self.client.get(reverse('main:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/index.html')
        self.assertContains(response, 'Главная')
        self.assertContains(response, 'Главная страница')

    def test_about_view(self):
        response = self.client.get(reverse('main:about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/about.html')
        self.assertContains(response, 'Home - О нас')
        self.assertContains(response, 'О нас')
        self.assertContains(response, 'Текст о нас')