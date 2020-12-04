from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


class UserAdmin(BaseUserAdmin):
    model = User


    list_display = (
        'username', 'is_active', 'is_staff', 'is_superuser'
    )

    fieldsets = (
        (None, {
            'fields': ('username', 'password', 'email', 'is_active', 'is_staff', 'is_superuser')
        }
         ),
    )

    add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2', 'email', 'is_active', 'is_staff', 'is_superuser')
        }
         ),
    )


admin.site.register(User, UserAdmin)
