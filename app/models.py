from django.contrib.auth.models import AbstractUser, Permission
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        related_name='custom_user_set',
        related_query_name='custom_user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        related_name='custom_user_set',
        related_query_name='custom_user',
    )

    # Add any additional fields you want to include for your user

    def __str__(self):
        return self.username
