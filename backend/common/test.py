from io import StringIO

from django.core.management import call_command
from django.test.runner import DiscoverRunner
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from common.utils import get_all_apps


class CustomTestRunner(DiscoverRunner):
    def build_suite(self, test_labels=None, extra_tests=None, **kwargs):
        """
        Override the default test discovery mechanism here.
        """

        if not test_labels:
            test_labels = [f'{app}.tests' for app in get_all_apps()] or ['users.tests']
        return super().build_suite(test_labels, **kwargs)


class JwtAPITestCase(APITestCase):
    def get_access_token(self, user):
        """Generate JWT token for a given user"""
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)

    def authenticate(self, user):
        """Set the JWT token in the request header for a given user."""
        access_token = self.get_access_token(user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)

    def request(self, method, url, data=None, user=None, authenticate=True, **extra_kwargs):
        """
        A custom request method that adds JWT authentication automatically.

        Params:
        - method: The HTTP method (get, post, put, delete, etc.).
        - url: The endpoint URL.
        - data: The payload (for POST/PUT requests).
        - user: The user to authenticate with (optional, default to self.user).
        - authenticate: Whether to authenticate the request (default: True).
        - extra_kwargs: Any extra parameters for the request (e.g., headers, format).
        """
        if authenticate:
            self.authenticate(user=user)

        method_function = getattr(self.client, method)

        response = method_function(url, data, **extra_kwargs)
        return response


class TestManagementCommandMixin:
    def call_command(self, command, *args, **kwargs):
        stdout = StringIO()
        stderr = StringIO()
        call_command(
            command,
            *args,
            stdout=stdout,
            stderr=stderr,
            **kwargs,
        )
        return stdout.getvalue(), stderr.getvalue()
