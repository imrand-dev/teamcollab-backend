from rest_framework.generics import (
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
)
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated

from django_filters.rest_framework import DjangoFilterBackend

from accounts.models import User
from accounts.rest.serializers.user import UserRegistrationSerializer
from accounts.services.users import UserService
from accounts.permissions import IsOwnerOrReadOnly


class UserRegistration(CreateAPIView):
    serializer_class = UserRegistrationSerializer


class RegisteredUserList(ListAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter, DjangoFilterBackend]
    # search_fields = ["title"]
    # filterset_fields = ["created_at", "due_date", "priority", "status"]

    def get_queryset(self):
        return User.objects.filter()


class UserDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    http_method_names = ["get", "patch", "delete"]

    def get_object(self):
        user_service = UserService()
        user_uid = self.kwargs.get("user_uid", None)

        return user_service.get_user_by_uid(uid=user_uid)
