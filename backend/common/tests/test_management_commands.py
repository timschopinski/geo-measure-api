from unittest.mock import MagicMock, patch

from django.apps import apps
from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import TestCase, TransactionTestCase

from common.test import TestManagementCommandMixin
from users.models import User


class TestLoadFixturesCommand(TestCase):
    def setUp(self):
        call_command('load_fixtures')

    def test_create_superuser(self):
        superuser = User.objects.get(email='admin@example.com')
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_active)

    def test_all_models_created(self):
        all_models = apps.get_models()
        excluded_apps = {
            'auth',
            'contenttypes',
            'sessions',
            'admin',
            'rest_framework',
            'silk',
            'authtoken',
        }

        for model in all_models:
            if model._meta.app_label in excluded_apps:
                continue

            with self.subTest(model=model):
                actual_count = model.objects.count()
                self.assertGreater(
                    actual_count, 0, f'Expected at least 1 instance of {model.__name__}, found {actual_count}.'
                )


class TestWaitForDatabaseCommand(TestManagementCommandMixin, TransactionTestCase):
    @patch('django.db.connections')
    def test_wait_for_database(self, mock_connections):
        mock_connections.__getitem__.side_effect = [OperationalError, MagicMock()]
        output, _ = self.call_command('wait_for_db')

        self.assertIn('Database unavailable, waiting 1 second...', output)
        self.assertIn('Database available!', output)
