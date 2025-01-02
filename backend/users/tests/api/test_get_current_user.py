from django.urls import reverse
from rest_framework import status

from common.test import JwtAPITestCase
from users.factories import UserFactory


class TestGetCurrentUser(JwtAPITestCase):
    def setUp(self):
        self.user = UserFactory(email='user@example.com')

    def test_get_user(self):
        url = reverse('users-me')

        response = self.request(method='get', url=url, user=self.user)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], self.user.email)
