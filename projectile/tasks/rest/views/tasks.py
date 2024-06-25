from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated

from common.permissions import IsOwnerOrReadOnly

from core.models import Project

from tasks.models import Task, Comment
from tasks.rest.serializers.tasks import CommentSerializer, TaskSerializer


class TaskList(ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        project_uid = self.kwargs.get("project_uid")
        project = Project.objects.get(uid=project_uid)
        return Task.objects.filter(project=project)


class TaskDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    http_method_names = ["get", "patch", "delete"]

    def get_object(self):
        task_uid = self.kwargs.get("task_uid", None)

        try:
            return Task.objects.get(uid=task_uid)
        except Task.DoesNotExist:
            raise NotFound(
                detail="The requested Task doesn't exist or has been removed."
            )


class CommentList(ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        task_uid = self.kwargs.get("task_uid")

        try:
            task = Task.objects.get(uid=task_uid)
        except Task.DoesNotExist:
            raise NotFound(detail="Task does not exist.")

        return Comment.objects.filter(task=task)


class CommentDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    http_method_names = ["get", "patch", "delete"]

    def get_object(self):
        comment_uid = self.kwargs.get("comment_uid", None)

        try:
            return Comment.objects.get(uid=comment_uid)
        except Comment.DoesNotExist:
            raise NotFound(detail="Comment does not exist.")
