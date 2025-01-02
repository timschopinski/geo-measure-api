from django.urls import reverse
from rest_framework import status

from common.test import JwtAPITestCase
from users.factories import UserFactory
from users.models import User


class TestDeleteUser(JwtAPITestCase):
    def setUp(self):
        self.user = UserFactory(email='user@example.com')

    def test_delete_user(self):
        url = reverse('users-me')
        data = {'current_password': 'password'}
        response = self.request(method='delete', url=url, data=data, user=self.user)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(User.objects.filter(email=self.user.email).exists())

    def test_delete_user_with_incorrect_password(self):
        url = reverse('users-me')
        data = {'current_password': 'wrongpassword'}

        response = self.request(method='delete', url=url, data=data, user=self.user)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('current_password', response.data)
        self.assertEqual(response.data['current_password'][0], 'Invalid password.')
