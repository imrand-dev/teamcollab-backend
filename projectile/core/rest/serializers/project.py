from rest_framework import serializers
from rest_framework.exceptions import NotFound

from core.models import Project, Member

from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        read_only_fields = fields = ["uid", "first_name", "last_name", "email"]


class ProjectSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Project
        fields = [
            "uid",
            "created_at",
            "updated_at",
            "name",
            "description",
            "owner",
            "slug",
        ]
        read_only_fields = [
            "uid",
            "created_at",
            "updated_at",
            "slug",
            "owner",
        ]

    def validate_name(self, name):
        if Project.objects.filter(name=name).exists():
            raise serializers.ValidationError(
                "A project with this name already exists."
            )
        return name

    def create(self, validated_data):
        user = self.context["request"].user
        name = validated_data.get("name")
        description = validated_data.get("description")

        project = Project.objects.create(owner=user, name=name, description=description)
        return project


class ProjectMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ["uid", "project", "roles"]
        read_only_fields = [
            "uid",
        ]

    def create(self, validated_data):
        user = self.context["request"].user
        project = validated_data.get("project")
        roles = validated_data.get("roles")

        return Project.objects.create(owner=user, project=project, roles=roles)
