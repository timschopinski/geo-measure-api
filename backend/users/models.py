from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from users.managers import UserManager


class BaseUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    objects = UserManager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    USERNAME_FIELD = 'email'

    class Meta:
        abstract = True


class User(BaseUser):
    pass
