from django.urls import path

from core.rest.views.project import ProjectView, ProjectDetail

from tasks.rest.views.tasks import TaskList

urlpatterns = [
    path("/<uuid:project_uid>/tasks", TaskList.as_view(), name="task-lists"),
    path("/<uuid:project_uid>", ProjectDetail.as_view(), name="project-detail"),
    path("", ProjectView.as_view(), name="project-lists"),
]
