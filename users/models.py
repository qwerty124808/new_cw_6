from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    fio = models.CharField(max_length=150, verbose_name='ФИО')
    comment = models.TextField(verbose_name='коментарий', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

