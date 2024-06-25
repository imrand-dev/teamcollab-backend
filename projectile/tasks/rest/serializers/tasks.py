from django.utils import timezone

from rest_framework import serializers
from rest_framework.exceptions import NotFound

from accounts.models import User

from tasks.models import Task, Comment

from core.rest.serializers.project import UserSerializer

from core.models import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        read_only_fields = fields = [
            "uid",
            "name",
            "description",
        ]


class TaskSerializer(serializers.ModelSerializer):
    user_uids = serializers.ListField(
        child=serializers.UUIDField(),
        required=False,
        write_only=True,
    )
    # project_ = serializers.PrimaryKeyRelatedField(
    #     queryset=Project.objects.all(), required=False
    # )
    project = ProjectSerializer(read_only=True)
    assigned_to = UserSerializer(read_only=True)

    class Meta:
        model = Task
        fields = [
            "uid",
            "slug",
            "created_at",
            "updated_at",
            "title",
            "description",
            "status",
            "priority",
            "assigned_to",
            "due_date",
            "user_uids",
            "project",
        ]

        read_only_fields = [
            "uid",
            "slug",
            "created_at",
            "updated_at",
            "project",
        ]

    def validate(self, attrs) -> dict:
        default_date = timezone.now().date() + timezone.timedelta(days=5)
        due_date = attrs.get("due_date", default_date)

        if due_date < timezone.now().date():
            raise serializers.ValidationError("Due date can't be in the past.")

        user_uids = attrs.pop("user_uids", [])
        users = []
        for uid in user_uids:
            try:
                user = User.objects.get(uid=uid)
            except User.DoesNotExist:
                raise NotFound(detail="User doesn't exist")
            else:
                users.append(user)

        attrs["users"] = users
        return attrs

    def create(self, validated_data):
        user = self.context["request"].user
        project_uid = self.context["view"].kwargs.get("project_uid")

        title = validated_data.get("title")
        description = validated_data.get("description")
        status = validated_data.get("status")
        priority = validated_data.get("priority")
        users = validated_data.pop("users", [])

        project = Project.objects.get(uid=project_uid)
        task = Task.objects.create(
            owner=user,
            title=title,
            description=description,
            status=status,
            priority=priority,
            project=project,
            assigned_to=users[0] if users else None,
        )

        return task


class CommentSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = [
            "content",
            "uid",
            "owner",
            "task",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "uid",
            "owner",
            "created_at",
            "task",
            "updated_at",
        ]

    def create(self, validated_data):
        user = self.context["request"].user
        content = validated_data.get("content")

        task_uid = self.context["view"].kwargs.get("task_uid")
        task = Task.objects.get(uid=task_uid)

        return Comment.objects.create(owner=user, content=content, task=task)
