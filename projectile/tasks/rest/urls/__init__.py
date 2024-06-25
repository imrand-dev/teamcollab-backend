from django.urls import path, include

urlpatterns = [
    path("/tasks", include("tasks.rest.urls.tasks")),
    path("/comments", include("tasks.rest.urls.comments")),
]
