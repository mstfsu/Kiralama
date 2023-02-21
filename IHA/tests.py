from django.test import TestCase
from IHA.views import IHAViewSet
from rest_framework.test import APIRequestFactory
from .models import *
# Create your tests here.


class IHATestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="test")
        self.brand = Brand.objects.create(name="test")

    def test_view_set(self):
        """ test all actions of drf viewset with RequestFactory"""
        factory = APIRequestFactory()
        request = factory.post('/iha/', {'name': 'deneme', 'model_number': '123', 'description': 'test',
                               'weight': 12.2, 'category': [self.category.id], 'brand': self.brand.id})
        response = IHAViewSet.as_view({'post': 'create'})(request)
        self.assertEqual(response.status_code, 201)
    
        request = factory.get('/iha/')
        response = IHAViewSet.as_view({'get': 'list'})(request)
        self.assertEqual(response.status_code, 200)

        request = factory.get('/iha/1/')
        response = IHAViewSet.as_view({'get': 'retrieve'})(request, pk=1)
        self.assertEqual(response.status_code, 200)

        request = factory.put('/iha/1/', {'name': 'aa', 'model_number': '44', 'description': 'test',
                              'weight': 12.2, 'category': [self.category.id], 'brand': self.brand.id})
        response = IHAViewSet.as_view({'put': 'update'})(request, pk=1)
        self.assertEqual(response.status_code, 200)
       
        IHA.objects.last()
        self.assertEqual(IHA.objects.last().name, 'aa')

        request = factory.delete('/iha/1/')
        response = IHAViewSet.as_view({'delete': 'destroy'})(request, pk=1)
        self.assertEqual(response.status_code, 204)

        self.assertEqual(IHA.objects.count(), 0)
        
