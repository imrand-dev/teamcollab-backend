import uuid

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from autoslug import AutoSlugField

from accounts.managers import CustomUserManager


def full_name(instance):
    if instance.first_name and instance.last_name:
        return f"{instance.first_name} {instance.last_name}".strip()


class User(AbstractBaseUser, PermissionsMixin, models.Model):
    user_name = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from=full_name, editable=False, unique=True)
    email = models.EmailField(unique=True, db_index=True)

    uid = models.UUIDField(
        db_index=True, unique=True, default=uuid.uuid4, editable=False
    )
    date_joined = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["user_name", "first_name", "last_name"]

    # custom manager
    objects = CustomUserManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ["-date_joined"]
