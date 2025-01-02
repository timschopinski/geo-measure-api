from django.urls import reverse
from rest_framework import status

from common.test import JwtAPITestCase
from users.factories import UserFactory


class TestUpdateUser(JwtAPITestCase):
    def setUp(self):
        self.user = UserFactory(email='user@example.com')

    def test_update_user(self):

        url = reverse('users-me')
        data = {'first_name': 'UpdatedName', 'last_name': 'UpdatedSurname'}

        response = self.request(method='patch', url=url, data=data, user=self.user)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, 'UpdatedName')
        self.assertEqual(self.user.last_name, 'UpdatedSurname')
