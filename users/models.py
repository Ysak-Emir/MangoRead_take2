from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
)
from django.db import models
from .managers import MyUserManager


class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True, unique=True)
    profile_picture = models.ImageField(upload_to="user_data/profile_picture", null=True, blank=True)
    username = models.CharField(max_length=50, unique=True, blank=False, null=True)
    nickname = models.CharField(max_length=50, unique=True, blank=False, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = MyUserManager()

    @property
    def get_username(self):
        return f'{self.username}'

    def __str__(self):
        return self.username
