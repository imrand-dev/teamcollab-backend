from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(
        self, user_name, first_name, last_name, email, password, **extra_fields
    ):
        if not email:
            raise ValueError(_("Email address is required"))

        if not password:
            raise ValueError(_("Password is required"))

        email = self.normalize_email(email=email)
        user = self.model(user_name=user_name, email=email, **extra_fields)
        user.first_name = first_name.title()
        user.last_name = last_name.title()
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(
        self, user_name, first_name, last_name, email, password, **extra_fields
    ):
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))

        return self.create_user(
            user_name, first_name, last_name, email, password, **extra_fields
        )
