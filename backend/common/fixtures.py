from users.factories import UserFactory


class DataLoader:
    NUMBER_OF_USERS = 20

    def create_users(self):
        print('Creating users...')
        UserFactory.create_batch(self.NUMBER_OF_USERS)
        print(f'{DataLoader.NUMBER_OF_USERS} Users created.')

    @staticmethod
    def create_superuser():
        print('Creating superuser...')
        UserFactory(
            email='admin@example.com',
            first_name='Admin',
            last_name='Adminowski',
            is_staff=True,
            is_superuser=True,
            is_active=True,
        )
        print('Superuser created.')
