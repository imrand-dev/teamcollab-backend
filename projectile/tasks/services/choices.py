from django.db import models


class TaskStatus(models.TextChoices):
    TO_DO = "To Do", "To Do"
    IN_PROGRESS = "In Progress", "In Progress"
    DONE = "Done", "Done"


class TaskPriority(models.TextChoices):
    LOW = "Low", "Low"
    HIGH = "High", "High"
    MEDIUM = "Medium", "Medium"
