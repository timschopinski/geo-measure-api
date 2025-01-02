from django.urls import reverse
from rest_framework import status

from common.test import JwtAPITestCase
from users.factories import UserFactory
from users.models import User


class TestCreateUser(JwtAPITestCase):
    def test_create_user(self):
        url = reverse('users-list')
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john@example.com',
            'password1': 'strongpassword123',
            'password2': 'strongpassword123',
        }

        response = self.request(method='post', url=url, data=data, authenticate=False)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get(email='john@example.com').first_name, 'John')

    def test_create_user_with_invalid_email(self):
        url = reverse('users-list')
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'invalid-email',
            'password1': 'strongpassword123',
            'password2': 'strongpassword123',
        }

        response = self.request(method='post', url=url, data=data, authenticate=False)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)

    def test_create_user_with_existing_email(self):
        UserFactory(first_name="Existing", last_name="User", email="john@example.com", password="existingpassword123")

        url = reverse('users-list')
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john@example.com',
            'password1': 'strongpassword123',
            'password2': 'strongpassword123',
        }

        response = self.request(method='post', url=url, data=data, authenticate=False)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)
        self.assertEqual(response.data['email'][0], 'Invalid email.')

    def test_create_user_with_password_mismatch(self):
        url = reverse('users-list')
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john@example.com',
            'password1': 'strongpassword123',
            'password2': 'mismatchpassword123',
        }

        response = self.request(method='post', url=url, data=data, authenticate=False)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('non_field_errors', response.data)
        self.assertEqual(response.data['non_field_errors'][0], 'The two password fields did not match.')

    def test_create_user_with_weak_password(self):
        url = reverse('users-list')
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john@example.com',
            'password1': 'weakpassword',
            'password2': 'weakpassword',
        }

        response = self.request(method='post', url=url, data=data, authenticate=False)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('password1', response.data)
        self.assertEqual(response.data['password1'][0], 'Password must contain at least one numeral.')
