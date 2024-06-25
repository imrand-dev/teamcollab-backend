from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from accounts.models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["user_name", "email", "first_name", "last_name", "password"]


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ["user_name", "email", "first_name", "last_name", "password"]
