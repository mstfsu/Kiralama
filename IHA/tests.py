from django.test import TestCase
from django.contrib.auth.models import User
from .models import *
# Create your tests here.


class IHATestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="test")
        self.brand = Brand.objects.create(name="test")
        self.user = User.objects.create_user(username="test", password="test")
        self.client.force_login(self.user)

    def test_view_set(self):
        """ test all actions of iha drf viewset with client"""

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

        self.assertEqual(IHA.objects.last().name, 'aa')

        request = self.client.delete('/iha/1/')
        self.assertEqual(request.status_code, 204)

        self.assertEqual(IHA.objects.count(), 0)

    def test_dashboard_statistics(self):
        """ test dashboard statistics view"""

        request = self.client.get('/iha/dashboard-statics/')
        self.assertEqual(request.status_code, 200)
        self.assertJSONEqual(request.content, {
            'total_iha': 0,
            'total_category': 1,
            'total_brand': 1,
            'total_user': 1
        })


class CategoryTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test", password="test")
        self.client.force_login(self.user)

    def test_view_set(self):
        """ test all actions of category drf viewset with client"""

        request = self.client.post(
            '/iha/category/', {'name': 'deneme', 'slug': 'deneme'})

        self.assertEqual(request.status_code, 201)

        request = self.client.get('/iha/category/')
        self.assertEqual(request.status_code, 200)

        request = self.client.get('/iha/category/1/')
        self.assertEqual(request.status_code, 200)

        request = self.client.put(
            '/iha/category/1/', {'name': 'aa', 'slug': 'aa'}, content_type='application/json')
        self.assertEqual(request.status_code, 200)

        self.assertEqual(Category.objects.last().name, 'aa')

        request = self.client.delete('/iha/category/1/')
        self.assertEqual(request.status_code, 204)

        self.assertEqual(Category.objects.count(), 0)


class BrandTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test", password="test")
        self.client.force_login(self.user)

    def test_view_set(self):
        """ test all actions of brand drf viewset with client"""

        request = self.client.post(
            '/iha/brand/', {'name': 'deneme', 'description': 'deneme'})

        self.assertEqual(request.status_code, 201)

        request = self.client.get('/iha/brand/')
        self.assertEqual(request.status_code, 200)

        request = self.client.get('/iha/brand/1/')
        self.assertEqual(request.status_code, 200)

        request = self.client.put(
            '/iha/brand/1/', {'name': 'aa', 'description': 'aa'}, content_type='application/json')
        self.assertEqual(request.status_code, 200)

        self.assertEqual(Brand.objects.last().name, 'aa')

        request = self.client.delete('/iha/brand/1/')
        self.assertEqual(request.status_code, 204)

        self.assertEqual(Brand.objects.count(), 0)
