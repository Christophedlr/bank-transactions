from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = None
    last_name = None

    class Meta:
        db_table = 'app_user'
        verbose_name = 'Utilisateur'
        verbose_name_plural = 'Utilisateurs'
