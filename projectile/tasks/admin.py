from django.contrib import admin

from tasks.models import Task, Comment


@admin.register(Task)
class TaskModelAdmin(admin.ModelAdmin):
    list_display = ["title", "priority", "status", "assigned_to"]


@admin.register(Comment)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ["content", "owner", "task"]
