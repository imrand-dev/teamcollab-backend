import uuid

from django.db import models

from autoslug import AutoSlugField

from accounts.models import User

from core.services.choices import RoleChoices


class Project(models.Model):
    uid = models.UUIDField(
        db_index=True, unique=True, default=uuid.uuid4, editable=False
    )
    name = models.CharField(max_length=200)
    description = models.TextField()
    owner = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name="project_owner"
    )
    # owner = models.OneToOneField(to=User, on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from="name", editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Member(models.Model):
    uid = models.UUIDField(
        db_index=True, unique=True, default=uuid.uuid4, editable=False
    )
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE)
    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name="project_member"
    )
    role = models.CharField(
        max_length=15,
        choices=RoleChoices.choices,
        default=RoleChoices.MEMBER,
    )

    class Meta:
        verbose_name = "Project Member"
        verbose_name_plural = "Project Members"

    def __str__(self):
        return self.user.user_name
