from django.urls import reverse_lazy
from rest_framework.test import APITestCase

from shop.models import Category


class TestCategory(APITestCase):

    url = reverse_lazy('category-list')

    def format_datetime(self, value):
        return value.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

    def test_list(self):
        category = Category.objects.create(name='Fruits', active=True)
        Category.objects.create(name='Légumes', active=False)

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

        expected = [
            {
                'id': category.id,
                'name': category.name,
                'date_created': self.format_datetime(category.date_created),
                'date_updated': self.format_datetime(category.date_updated)
            }
        ]
        self.assertEqual(response.json(), expected)

    def test_create(self):
        self.assertFalse(Category.objects.exists())
        response = self.client.post(self.url, data={'name': 'Tentative'})
        self.assertEqual(response.status_code, 405)
        self.assertFalse(Category.objects.exists())
