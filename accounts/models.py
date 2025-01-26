from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CostumUser(AbstractUser):
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']