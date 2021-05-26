from django.db import models
from django.contrib.auth.models import AbstractUser
from users.utils import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(verbose_name='Email', unique=True)
    first_name = models.CharField(verbose_name='First Name', max_length=150, blank=True)
    last_name = models.CharField(verbose_name='Last Name', max_length=150, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    class Meta:
        ordering = ['-id']
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.email
