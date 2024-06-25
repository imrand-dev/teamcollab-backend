from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated

from core.rest.serializers.project import ProjectSerializer, ProjectMemberSerializer
from core.models import Project, Member

from common.permissions import IsOwnerOrReadOnly


class ProjectView(ListCreateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Project.objects.filter()


class ProjectDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    http_method_names = ["get", "patch", "delete"]

    def get_object(self):
        project_uid = self.kwargs.get("project_uid")

        try:
            return Project.objects.get(uid=project_uid)
        except Project.DoesNotExist:
            raise NotFound(
                detail="The requested Project doesn't exist or has been removed."
            )
