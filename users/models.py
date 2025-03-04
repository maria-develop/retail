from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    name = models.CharField(
        max_length=100,
        verbose_name="ФИО",
        help_text="Иванов И.И.",
    )
    email = models.EmailField(unique=True, verbose_name="Почта")
    is_active = models.BooleanField(default=True, verbose_name="Активный")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
