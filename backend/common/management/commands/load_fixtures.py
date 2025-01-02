from django.core.management.base import BaseCommand

from common.fixtures import DataLoader
from common.performance import measure_time


class Command(BaseCommand):
    """Django command to create fixtures"""

    @measure_time('load_fixtures')
    def handle(self, *args, **options):
        self.stdout.write('loading fixtures...')

        data_loader = DataLoader()
        data_loader.create_users()
        data_loader.create_superuser()

        self.stdout.write(self.style.SUCCESS('Fixtures loaded successfully!'))
