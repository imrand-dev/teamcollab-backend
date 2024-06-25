from rest_framework import serializers

from accounts.models import User
from accounts.services.users import UserService


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        style={
            "input_type": "password",
        },
        max_length=32,
        min_length=6,
    )

    class Meta:
        model = User
        fields = [
            "uid",
            "date_joined",
            "updated_at",
            "user_name",
            "first_name",
            "last_name",
            "slug",
            "email",
            "password",
            "is_active",
            "is_staff",
            "is_verified",
        ]
        read_only_fields = [
            "uid",
            "slug",
            "date_joined",
            "updated_at",
            "is_active",
            "is_staff",
            "is_verified",
        ]

    def create(self, validated_data):
        user_service = UserService()
        return user_service.create_user(**validated_data)
