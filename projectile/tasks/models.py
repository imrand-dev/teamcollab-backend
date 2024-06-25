import uuid

from django.db import models
from django.utils import timezone

from autoslug import AutoSlugField

from tasks.services.choices import TaskPriority, TaskStatus

from accounts.models import User
from core.models import Project


class Task(models.Model):
    uid = models.UUIDField(
        db_index=True, unique=True, default=uuid.uuid4, editable=False
    )
    owner = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="user_tasks",
        null=True,
        blank=True,
    )
    slug = AutoSlugField(
        populate_from="title",
        unique=True,
        editable=False,
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(
        max_length=15, choices=TaskStatus.choices, default=TaskStatus.TO_DO
    )
    priority = models.CharField(
        max_length=7, choices=TaskPriority.choices, default=TaskPriority.LOW
    )
    assigned_to = models.ForeignKey(
        to=User, on_delete=models.CASCADE, null=True, blank=True
    )
    project = models.ForeignKey(
        to=Project, on_delete=models.CASCADE, null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateField(
        default=timezone.now().date() + timezone.timedelta(days=5)
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at"]


class Comment(models.Model):
    uid = models.UUIDField(
        db_index=True, unique=True, default=uuid.uuid4, editable=False
    )
    content = models.TextField()
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    task = models.ForeignKey(to=Task, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

    class Meta:
        ordering = ["-created_at"]
