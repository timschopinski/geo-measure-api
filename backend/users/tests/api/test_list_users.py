from django.test import override_settings
from django.urls import reverse
from rest_framework import status

from common.test import JwtAPITestCase
from users.factories import UserFactory
from users.models import User


class TestListUsers(JwtAPITestCase):
    def setUp(self):
        self.staff_user = UserFactory(email='staff@example.com', is_staff=True)
        self.regular_user = UserFactory(email='regular@example.com')

    def test_list_users_as_admin(self):
        url = reverse('users-list')

        response = self.request(method='get', url=url, user=self.staff_user)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), User.objects.count())

    @override_settings(HIDE_USERS=True)
    def test_list_users_as_regular_user_with_hide_users_enabled(self):
        url = reverse('users-list')

        response = self.request(method='get', url=url, user=self.regular_user)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['email'], self.regular_user.email)

    @override_settings(HIDE_USERS=False)
    def test_list_users_as_regular_user_with_hide_users_disabled(self):
        url = reverse('users-list')

        response = self.request(method='get', url=url, user=self.regular_user)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), User.objects.count())
