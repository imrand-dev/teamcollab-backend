from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from accounts.forms import CustomUserCreationForm, CustomUserChangeForm
from accounts.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ["user_name", "first_name", "last_name", "email", "is_staff"]
    search_fields = ["email"]
    ordering = ["-email"]
    # add_form = CustomUserCreationForm
    # form = CustomUserChangeForm

    # update an existing user
    fieldsets = (
        (None, {"fields": ["email", "password"]}),
        ("Personal Info", {"fields": ["user_name", "first_name", "last_name"]}),
        (
            "Permissions",
            {
                "fields": [
                    "is_staff",
                    "is_verified",
                    "is_active",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ]
            },
        ),
        (
            "Important dates",
            {
                "fields": [
                    "last_login",
                ]
            },
        ),
    )

    # create a new user
    add_fieldsets = (
        (
            None,
            {
                "classes": [
                    "wide",
                ],
                "fields": [
                    "user_name",
                    "first_name",
                    "last_name",
                    "email",
                    "password1",
                    "password2",
                ],
            },
        ),
    )
