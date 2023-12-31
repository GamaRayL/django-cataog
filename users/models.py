from django.db import models
from utils.utils import NULLABLE
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='почта')
    is_active = models.BooleanField(default=False)
    key = models.CharField(max_length=10, **NULLABLE, verbose_name='ключ')
    phone = models.CharField(max_length=35, **NULLABLE, verbose_name='телефон')
    country = models.CharField(max_length=50, **NULLABLE, verbose_name='страна')
    avatar = models.ImageField(**NULLABLE, verbose_name='аватар')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
