from django.core.management.base import BaseCommand
from django.db import transaction

from accounts.services.users import UserService


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        with transaction.atomic():
            user_service = UserService()

            superuser = user_service.create_superuser(
                email="johnsnow@gmail.com",
                password="123456",
                user_name="john",
                first_name="John",
                last_name="Snow",
            )

            self.stdout.write(self.style.SUCCESS("Superuser created successfully."))
