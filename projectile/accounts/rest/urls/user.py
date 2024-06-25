from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from accounts.rest.views.user import (
    UserDetailView,
    UserRegistration,
    RegisteredUserList,
)

urlpatterns = [
    path("/register", UserRegistration.as_view(), name="user-registation"),
    path("/login", TokenObtainPairView.as_view(), name="user-login-token"),
    path("/token/refresh", TokenRefreshView.as_view(), name="refresh-token"),
    # user detail
    path("/<uuid:user_uid>", UserDetailView.as_view(), name="user-detail"),
    path("", RegisteredUserList.as_view(), name="list-of-users"),
]
