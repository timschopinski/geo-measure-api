import factory

from users.models import User


class UserFactory(factory.django.DjangoModelFactory):
    first_name = factory.LazyAttributeSequence(lambda o, n: f'user{n + 1}')
    last_name = factory.SelfAttribute('first_name')
    email = factory.LazyAttribute(lambda n: f'{n.first_name}@example.com')

    @factory.post_generation
    def set_password(self, create, extracted):
        self.set_password('password')

    class Meta:
        model = User
