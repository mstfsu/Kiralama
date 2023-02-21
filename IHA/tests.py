from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client
from IHA.views import IHAViewSet
from rest_framework.test import APIRequestFactory
from .models import *
# Create your tests here.


class IHATestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="test")
        self.brand = Brand.objects.create(name="test")
        self.user = User.objects.create_user(username="test", password="test")
        self.client.force_login(self.user)

    def test_view_set(self):
        """ test all actions of drf viewset with client"""

        request = self.client.post('/iha/', {'name': 'deneme', 'model_number': '123', 'description': 'test',
                                             'weight': 12.2, 'category': [self.category.id], 'brand': self.brand.id})

        self.assertEqual(request.status_code, 201)

        request = self.client.get('/iha/')
        self.assertEqual(request.status_code, 200)

        request = self.client.get('/iha/1/')
        self.assertEqual(request.status_code, 200)

        request = self.client.put('/iha/1/', {'name': 'aa', 'model_number': '44', 'description': 'test',
                                              'weight': 12.2, 'category': [self.category.id], 'brand': self.brand.id}, content_type='application/json')
        self.assertEqual(request.status_code, 200)

        IHA.objects.last()
        self.assertEqual(IHA.objects.last().name, 'aa')

        request = self.client.delete('/iha/1/')
        self.assertEqual(request.status_code, 204)

        self.assertEqual(IHA.objects.count(), 0)
