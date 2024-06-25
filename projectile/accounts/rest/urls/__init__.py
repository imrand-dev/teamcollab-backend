from django.urls import path, include

urlpatterns = [
    path("", include("accounts.rest.urls.user")),
]
