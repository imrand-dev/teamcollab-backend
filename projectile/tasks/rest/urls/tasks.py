from django.urls import path

from tasks.rest.views.tasks import TaskDetail, CommentList

urlpatterns = [
    path("/<uuid:task_uid>/comments", CommentList.as_view(), name="comment-lists"),
    path("/<uuid:task_uid>", TaskDetail.as_view(), name="task-detail"),
]
