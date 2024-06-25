from accounts.models import User


class UserService:
    def create_user(
        self,
        user_name: str,
        first_name: str,
        last_name: str,
        email: str,
        password: str,
        is_staff: bool = False,
        is_active: bool = True,
        is_verified: bool = True,
    ) -> User:
        return User.objects.create_user(
            user_name=user_name,
            first_name=first_name,
            last_name=last_name,
            password=password,
            email=email,
            is_active=is_active,
            is_staff=is_staff,
            is_verified=is_verified,
        )

    def create_superuser(
        self,
        user_name: str,
        first_name: str,
        last_name: str,
        email: str,
        password: str,
        is_staff: bool = True,
        is_active: bool = True,
        is_verified: bool = True,
        is_superuser: bool = True,
    ) -> User:
        return User.objects.create_superuser(
            user_name=user_name,
            first_name=first_name,
            last_name=last_name,
            password=password,
            email=email,
            is_staff=is_staff,
            is_active=is_active,
            is_verified=is_verified,
            is_superuser=is_superuser,
        )

    def get_user_by_email(self, email: str) -> User:
        return User.objects.get(email=email)

    def get_user_by_uid(self, uid: str) -> User:
        return User.objects.get(uid=uid)
