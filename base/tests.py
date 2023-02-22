from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import *
# Create your tests here.


class RegisterTestCase(TestCase):
    def setUp(self):
        self.register_url = reverse('signup')
        self.login_url = reverse('login')
        self.user = {
            "username": "testuser",
            "password1": "Test.123...",
            "password2": "Test.123..."
        }

    def test_can_view_page_correctly(self):
        """Test that the register page can be rendered correctly"""
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')

    def test_can_register_user(self):
        """Test that a user can be registered"""
        response = self.client.post(
            self.register_url, self.user, format='text/html')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.count(), 1)

    def test_can_login_page_correctly(self):
        """Test that the login page can be rendered correctly"""
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_can_login_user(self):
        """Test that a user can be logged in"""
        response = self.client.post(self.login_url, {
                                    "username": "testuser", "password": "Test.123..."}, format='text/html')
        self.assertEqual(response.status_code, 200)
