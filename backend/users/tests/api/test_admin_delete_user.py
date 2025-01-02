from django.urls import reverse
from rest_framework import status

from common.test import JwtAPITestCase
from users.factories import UserFactory
from users.models import User


class TestAdminDeleteUser(JwtAPITestCase):
    def setUp(self):
        self.staff_user = UserFactory(email='staff@example.com', is_staff=True)
        self.regular_user = UserFactory(email='regular@example.com')

    def test_admin_delete_user(self):
        url = reverse('users-detail', kwargs={'pk': self.regular_user.pk})
        data = {'current_password': 'password'}
        response = self.request(method='delete', url=url, data=data, user=self.staff_user)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(User.objects.filter(email=self.regular_user.email).exists())
