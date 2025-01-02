from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User


class MyUserAdmin(UserAdmin):
    list_filter = ['is_staff', 'is_superuser', 'is_active']
    list_display = [
        'email',
        'first_name',
        'last_name',
        'is_superuser',
        'is_active',
    ]
    search_fields = ['email', 'first_name', 'last_name']
    ordering = ['email', 'is_superuser', 'first_name', 'last_name']


admin.site.register(User, MyUserAdmin)
