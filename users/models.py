from django.db import models
from django.contrib.auth.models import AbstractUser
from resources.constant import *
class User(AbstractUser):
    email = models.EmailField(unique=True)
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default=ROLE_MEMBER
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table='user'
