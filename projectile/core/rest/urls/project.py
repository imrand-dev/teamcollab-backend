from django.urls import path

from core.rest.views.project import ProjectView, ProjectDetail

urlpatterns = [
    path("/<uuid:project_uid>", ProjectDetail.as_view(), name="project-detail"),
    path("", ProjectView.as_view(), name="project-lists"),
]
